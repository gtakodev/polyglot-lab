# SPEC — tasklite

Version de la spec : **1.0** · S'applique à toutes les implémentations, quel que soit le langage.

`tasklite` exécute un ensemble de tâches shell dont les dépendances forment un graphe orienté
acyclique (DAG). C'est un `make` minimal, mais avec de la concurrence, des timeouts et un
rapport machine-lisible.

L'objectif de cette spec est d'être **suffisamment précise pour être testable à l'aveugle** :
`conformance/` ne connaît que la CLI, les fichiers et les codes de sortie. Aucune implémentation
n'est privilégiée.

---

## 1. CLI

```
tasklite run <spec-file> [--workers N] [--json] [--dry-run]
```

| Option | Défaut | Effet |
|---|---|---|
| `<spec-file>` | — | chemin du fichier de tâches (JSON, voir §2) |
| `--workers N` | `1` | nombre maximum de tâches exécutées simultanément ; `N >= 1` |
| `--json` | off | écrit **un seul** objet JSON sur stdout (voir §5), rien d'autre |
| `--dry-run` | off | valide et affiche l'ordre d'exécution prévu, sans rien lancer |

Sans `--json`, la sortie humaine est libre (couleurs, lignes, emojis : à toi de jouer).
Avec `--json`, **stdout ne contient que le JSON** ; les logs éventuels vont sur stderr.

### Codes de sortie

| Code | Signification |
|---|---|
| `0` | toutes les tâches ont réussi (ou `--dry-run` valide) |
| `1` | au moins une tâche a échoué, a expiré, ou a été ignorée à cause d'un échec |
| `2` | spec invalide (JSON illisible, cycle, dépendance inconnue, id dupliqué…) ou usage incorrect |

Un `--dry-run` sur une spec invalide sort en `2`.

---

## 2. Format du fichier de tâches

JSON uniquement en v0. Un objet racine :

```json
{
  "version": 1,
  "defaults": { "timeout_ms": 30000, "retries": 0 },
  "tasks": [
    { "id": "build", "run": "echo build" },
    { "id": "test",  "run": "echo test", "depends_on": ["build"], "retries": 1 },
    { "id": "lint",  "run": "echo lint", "depends_on": ["build"], "timeout_ms": 5000 }
  ]
}
```

### Champs

| Champ | Requis | Type | Règles |
|---|---|---|---|
| `version` | oui | entier | doit valoir `1` |
| `defaults` | non | objet | `timeout_ms` et `retries`, appliqués aux tâches qui ne les redéfinissent pas |
| `tasks` | oui | tableau | au moins une tâche |
| `tasks[].id` | oui | chaîne | unique, non vide, `[a-z0-9_-]+` |
| `tasks[].run` | oui | chaîne | commande passée à un shell POSIX : `sh -c "<run>"` |
| `tasks[].depends_on` | non | tableau de chaînes | défaut `[]` ; chaque id doit exister |
| `tasks[].retries` | non | entier | `>= 0`, défaut `defaults.retries` ou `0` |
| `tasks[].timeout_ms` | non | entier | `> 0`, défaut `defaults.timeout_ms` ou `0` (= pas de timeout) |

Champs inconnus : ignorés (pas une erreur) en v0.

### Validations (toutes → sortie `2`)

| Code d'erreur | Cas |
|---|---|
| `invalid_json` | fichier absent, illisible, ou JSON malformé |
| `invalid_field` | `version != 1`, `tasks` vide, id absent/vide/mal formé, `retries` ou `timeout_ms` invalides |
| `duplicate_id` | deux tâches avec le même `id` |
| `unknown_dependency` | une entrée de `depends_on` ne correspond à aucune tâche |
| `cycle` | le graphe contient un cycle |

---

## 3. Sémantique d'exécution

1. Une tâche ne démarre que si **toutes** ses dépendances ont le statut `success`.
2. Dès qu'une dépendance est `failed`, `timed_out` ou `skipped`, la tâche devient `skipped`
   (sans être exécutée, `attempts = 0`).
3. Au plus `--workers` tâches s'exécutent simultanément. L'ordre entre tâches indépendantes
   n'est pas spécifié — sauf en `--workers 1`, où il doit être un ordre topologique valide.
4. Chaque exécution de `run` :
   - hérite de l'environnement du processus parent ;
   - reçoit en plus `TASKLITE_TASK_ID=<id>` ;
   - s'exécute dans le répertoire courant de `tasklite`.
5. `attempts` = nombre d'exécutions réelles. Une tâche sans retry a `attempts = 1` si elle a
   démarré. Une tentative est relancée tant que `attempts <= retries` et que la tentative a
   échoué (code de sortie non nul **ou** timeout).
   Exemple : `retries = 2` → jusqu'à 3 tentatives.
6. `timeout_ms > 0` : au-delà, le processus **et ses enfants** sont tués, la tentative compte
   comme échouée, et si le budget de retries est épuisé le statut final est `timed_out`.
7. Une tâche réussit si sa dernière tentative sort avec le code `0`.
8. `--dry-run` : valide la spec, n'exécute rien, et affiche (humain) ou écrit (JSON) l'ordre
   topologique prévu. Tous les statuts valent `skipped`, `attempts = 0`.

---

## 4. Rapport JSON (`--json`)

Succès ou échec d'exécution :

```json
{
  "status": "success",
  "tasks": [
    { "id": "build", "status": "success",   "attempts": 1, "exit_code": 0,   "duration_ms": 12 },
    { "id": "test",  "status": "failed",    "attempts": 2, "exit_code": 1,   "duration_ms": 34 },
    { "id": "lint",  "status": "skipped",   "attempts": 0, "exit_code": null, "duration_ms": 0 },
    { "id": "docs",  "status": "timed_out", "attempts": 1, "exit_code": null, "duration_ms": 5001 }
  ]
}
```

- `status` global : `success` | `failed` | `invalid` (valeur `invalid` également en §2).
- statut de tâche : `success` | `failed` | `skipped` | `timed_out`.
- `exit_code` : code de la dernière tentative ; `null` si la tâche n'a pas démarré ou a été tuée
  par un timeout.
- `duration_ms` : durée murale de la tâche, entière, `>= 0`. Non comparée par la conformance ;
  c'est pour toi et pour tes benchmarks.
- L'ordre du tableau `tasks` n'est pas imposé ; la conformance compare par `id`.

Spec invalide :

```json
{ "status": "invalid", "errors": [ { "code": "cycle", "message": "..." } ] }
```

`message` est libre. `code` doit être l'un des cinq codes de §2. Sortie `2`.

---

## 5. Milestones

Chaque milestone est un état **testable**. La conformance indique quels cas elle couvre.

### M0 — Squelette qui parle
- lit les arguments, lit le fichier, valide la structure, sort `2` avec le bon `code` sur spec invalide.
- Cas : `04-cycle`, `05-unknown-dep`, `06-duplicate-id`.
- À ce stade, une spec valide peut encore sortir `3` (« pas implémenté ») ; c'est accepté.

### M1 — Exécution séquentielle
- ordre topologique, `--workers 1`, statuts `success` / `failed` / `skipped`, rapport JSON.
- Cas : `01-simple`, `03-failure`, `10-ordering`.

### M2 — Concurrence
- `--workers N` respecté, indépendance des tâches, pas de deadlock.
- Cas : `02-independent`, `09-concurrency`.

### M3 — Retries et timeouts
- `attempts` correct, timeout qui tue bien l'arbre de processus.
- Cas : `07-retries`, `08-timeout`.

À ce stade **v0 est terminée** : toute la suite est du bonus.

### M4 (v1) — Confort
- `--dry-run` complet, entrée YAML, `env` par tâche, `--keep-going` (ne pas ignorer les
  dépendants d'une tâche échouée mais continuer les branches indépendantes).
- Ajoute les cas de conformance correspondants **avant** de coder.

### M5 (v2) — Intelligence
- cache incrémental : une tâche dont `run` et l'empreinte des entrées déclarées n'ont pas changé
  est `cached` (nouveau statut à spécifier) ;
- `--only <id>` et `--impacted <fichier>` pour ne rejouer qu'une sous-partie du graphe.

### M6 (v3) — Observabilité
- rapport JSON enrichi (durées par tentative, sortie capturée sur option), export Prometheus,
  log structuré. À spécifier ici avant implémentation.

---

## 6. Ce qui est hors spec

- Pas de réseau, pas de base de données, pas de scheduling différé.
- Pas de parallélisme *inter-processus* au-delà de `--workers`.
- Pas de Windows natif : `sh -c` est le contrat. Si tu veux le supporter, c'est une extension
  qui doit apparaître dans cette spec.
