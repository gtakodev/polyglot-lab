# Conformance suite

Une seule suite pour les cinq langages. Elle ne regarde que ce que la spec promet :
la commande, les arguments, le code de sortie, l'objet JSON sur stdout, et pour un cas
particulier le temps mural.

## Usage

Depuis la racine du repo, en pointant la commande qui lance **ton** binaire **déjà construit** :

```bash
# Java / Kotlin (après `mvn -q compile`)
python3 conformance/run.py --cmd "java -cp target/classes lab.tasklite.Main"

# Go (après `go build -o tasklite .`)
python3 conformance/run.py --cmd "./tasklite"

# Rust (après `cargo build`)
python3 conformance/run.py --cmd "./target/debug/tasklite"

# TypeScript (après `npm run build`)
python3 conformance/run.py --cmd "node dist/main.js"
```

Les chemins relatifs de `--cmd` sont résolus depuis le dossier où tu lances le runner, puis
exécutés dans un répertoire temporaire : un `go run .` ou un `cargo run` ne fonctionnera donc pas
(le binaire doit être construit avant). C'est voulu — on teste l'artefact, pas la commande de build.

Options :

- `--upto M1` : ne lance que les cas des milestones ≤ M1 (utile pendant le développement).
- `--only 07-retries` : un seul cas (répétable).
- `-v` : affiche stdout/stderr en cas d'échec.
- `--list` : liste les cas.

Code de sortie : `0` si tout passe, `1` sinon. C'est **le** juge : un milestone n'est coché dans
`PROGRESS.md` que lorsque la conformance passe.

## Ce que la suite ignore volontairement

- `duration_ms` (le temps varie trop d'une machine à l'autre) ;
- l'ordre du tableau `tasks` → la comparaison se fait par `id` ;
- la sortie humaine sans `--json` → c'est là que chaque langage peut être joli.

## Ajouter un cas

1. Crée `cases/<NN-nom>/`.
2. Dedans : les fichiers de la spec (`tasks.json`) et `case.json`.
3. `case.json` :

```json
{
  "title": "ce que le cas vérifie",
  "milestone": "M2",
  "args": ["run", "tasks.json", "--json"],
  "expect": {
    "exit_code": 0,
    "status": "success",
    "tasks": {
      "a": { "status": "success", "attempts": 1, "exit_code": 0 }
    }
  }
}
```

Champs d'attente disponibles :

| Champ | Effet |
|---|---|
| `exit_code` | code de sortie attendu de la CLI |
| `status` | `status` global du rapport |
| `tasks` | attentes par id : `status`, `attempts`, `exit_code` |
| `exact_tasks` | `false` pour tolérer des tâches non listées (défaut `true`) |
| `error_codes` | ensemble exact de `errors[].code` sur une spec invalide |
| `max_duration_ms` | temps mural maximal (cas de concurrence) |

Les fichiers du dossier sont copiés dans un répertoire temporaire avant chaque exécution :
un cas peut écrire des fichiers sans polluer le repo.
