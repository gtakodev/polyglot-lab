# Glossaire

Les concepts que ce kata va te faire rencontrer, avec la question à te poser dans chaque langage.

## Graphe

- **DAG** — graphe orienté sans cycle. Les tâches sont des nœuds, `depends_on` des arêtes.
- **Tri topologique** — ordre où chaque nœud vient après ses dépendances. Il n'est pas unique :
  c'est pour ça que la spec ne fixe pas l'ordre entre tâches indépendantes.
- **Cycle** — a dépend de b qui dépend de a. Doit être détecté **avant** d'exécuter quoi que ce soit.

## Concurrence

- **Concurrence vs parallélisme** — la concurrence est une structure (plusieurs tâches en vol),
  le parallélisme une exécution simultanée. Un `--workers 4` sur une machine à 2 cœurs fait les deux.
- **Concurrence structurée** — la durée de vie des tâches enfants est bornée par le bloc parent
  (`coroutineScope`, `errgroup`, `thread::scope`). Sans elle, une tâche orpheline survit à son
  parent et fuit.
- **Annulation coopérative** — la tâche doit *vérifier* qu'on lui demande d'arrêter
  (`isActive`, `ctx.Done()`, `AbortSignal`). Un `sleep` ne s'annule pas tout seul.
- **Process group / session** — `sh -c "sleep 10"` crée un processus fils. Tuer le `sh` ne tue pas
  le `sleep` ; il faut tuer le groupe (`killpg`, `Setpgid`, `setsid`).
- **Backpressure** — ne pas lancer plus de travail qu'on ne peut en suivre. `--workers N` en est
  une forme simple.

## Types

- **Type somme (union taguée)** — une valeur qui est *exactement une* de plusieurs formes.
  Java : `sealed interface` + records. Kotlin : `sealed interface`. Rust : `enum` avec données.
  TS : union discriminée. Go : rien de natif — d'où la question de conception.
- **Exhaustivité** — le compilateur vérifie que tous les cas sont traités. Le `_ =>` et le `default:`
  la cassent.
- **Type fantôme / value class** — distinguer `TaskId` de `String` sans coût à l'exécution.
- **Validation runtime** — en TS (et dans tout JSON), les types n'existent pas à l'exécution.
  Un schéma (zod, Jackson, serde, `encoding/json`) est la seule garantie.

## Erreurs

- **Erreur vs exception** — une exception est un saut non local ; un `Result`/`error` est une valeur
  qui se propage explicitement. Le second rend les chemins d'échec visibles dans la signature.
- **Wrapping** — ajouter du contexte sans perdre la cause (`%w` en Go, `source` en Rust,
  `cause` en Java).
- **Fail fast vs fail safe** — ici, une spec invalide s'arrête avant toute exécution (fail fast) ;
  une tâche échouée n'empêche pas les branches indépendantes de tourner (fail safe).

## Système

- **Exit code** — contrat avec le shell. `0` succès, `1` échec d'exécution, `2` usage/spec.
  Ne jamais confondre « mon programme a échoué » et « la tâche a échoué ».
- **stdout vs stderr** — stdout est le contrat machine (`--json`), stderr est pour l'humain.
  Mélanger les deux casse tous les pipelines.
- **Signal** — `SIGTERM` demande, `SIGKILL` impose. Un timeout propre commence par `SIGTERM`.
