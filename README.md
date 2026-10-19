# Polyglot Lab

Un même outil, cinq langages, zéro copier-coller.

Ce repo est un **terrain d'entraînement**, pas un projet livrable. Le premier kata s'appelle
**tasklite** : un petit exécuteur de tâches en graphe (DAG). Tu l'implémentes une fois en Java,
puis tu le réécris en Kotlin, Go, Rust et TypeScript — en écrivant chaque fois le code *idiomatique
de ce langage*, pas une traduction du précédent.

## La règle du jeu

1. **Une spec, cinq implémentations.** `SPEC.md` est la seule source de vérité fonctionnelle.
   Elle est volontairement indépendante du langage.
2. **Pas de portage mécanique.** Si tu te surprends à recopier la structure de ton code Java
   en Rust, arrête : demande-toi comment un Rustacé modéliserait ça, puis vérifie dans la doc.
3. **Les tests de conformité sont fournis.** `conformance/` exécute ton binaire comme un
   utilisateur le ferait (CLI, fichiers, codes de sortie, JSON). C'est le juge commun aux cinq
   langages — pas tes tests unitaires, que tu écris toi-même.
4. **L'agent est un prof, pas un assistant.** Voir `AGENTS.md`. Il ne code pas à ta place ;
   il te guide, te questionne et t'envoie vers la bonne page de doc.

## Démarrer ici — la première session

Tout est déjà installé (voir `TOOLCHAINS.md`) : aucune installation, aucune dépendance à récupérer.
On travaille **un langage à la fois**, et on commence par Java.

### Étape 0 — lire avant de taper (20 min, pas plus)

1. `SPEC.md` **§1** (CLI et codes de sortie), **§2** (format + validations), **§5 → M0**.
2. Les trois cas que M0 doit faire passer : `conformance/cases/04-cycle`, `05-unknown-dep`,
   `06-duplicate-id` — le `case.json` dit exactement ce qui est attendu.
3. `AGENTS.md` — ce que l'agent a le droit de faire (peu de choses).

### Étape 1 — vérifier que le squelette tourne

```bash
cd languages/java
mvn -q package
java -jar target/tasklite.jar; echo "exit=$?"
```

Attendu : `tasklite: not implemented yet — see SPEC.md (M0)` puis `exit=3`. Si tu vois autre
chose, le support a un problème : arrête-toi et signale-le.

### Étape 2 — mesurer l'écart

```bash
python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar" --upto M0
```

Attendu : `0/3 case(s) passed.` — c'est le point de départ, pas un échec. À la fin de M0 : `3/3`.

### Étape 3 — coder

Le fichier : `languages/java/src/main/java/lab/tasklite/Main.java`.

**Tu écris tout.** L'agent ne produira jamais l'implémentation. Si tu lui colles ton code, il
le lit et le commmente ; si tu lui demandes la solution, il refuse une fois, puis te propose de
réduire le problème.

Après chaque modification, la boucle est :

```bash
mvn -q package && python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar" --upto M0
```

Un cas qui échoue s'affiche avec `-v` : `--upto M0 -v` montre stdout, stderr et l'attendu.

### Étape 4 — la boucle d'une session

| # | Toi | L'agent |
|---|---|---|
| 1 | Relis le milestone, reformule-le en une phrase | corrige la reformulation si elle est floue |
| 2 | Écris la sortie que tu attends pour un cas du milestone (`04-cycle` en M0) | compare avec la fixture |
| 3 | Annonce tes structures de données et l'ordre des étapes | pose **une** question sur le point le plus fragile |
| 4 | Code | ne regarde pas avant que tu demandes une revue |
| 5 | Demande une revue | commente par questions, max 3 remarques, jamais de code |
| 6 | Lance la conformance | lit la sortie avec toi, sans l'interpréter à ta place |
| 7 | Remplis `journal/java.md` | deux questions dessus |

### Étape 5 — clore le milestone

- `PROGRESS.md` : coche `M0` pour Java **seulement si** `3/3` passe.
- `journal/java.md` : ce qui a coincé, ce que tu as appris, le temps passé.

Puis M1 (`01-simple`, `03-failure`, `10-ordering`), et ainsi de suite jusqu'à M3 = fin de la v0.

### Si tu es bloqué

Dis-le avec le message d'erreur exact. L'aide monte d'un niveau à la fois : question sur
l'invariant → nom du concept + lien officiel → forme de la solution en prose. Jamais de code.
Si tu insistes, l'agent te proposera une session `grill-me` plutôt que de céder.

### Changer de langage

Même spec, même suite, autre dossier (`languages/kotlin|go|rust|typescript`). Chaque dossier a
son `README.md` avec les commandes. La commande de conformance change, la suite non :

```bash
# Go           --cmd "./tasklite"
# Rust         --cmd "./target/debug/tasklite"
# TypeScript   --cmd "node dist/main.js"
# Kotlin       --cmd "java -jar target/tasklite.jar"
```

Les cas ne se lancent **jamais** avec `go run .` ou `cargo run` : la suite exécute le binaire
dans un répertoire temporaire, donc l'artefact doit être construit avant.

## Structure

```
SPEC.md                    la spec fonctionnelle (v0 → v3)
AGENTS.md                  le mode professeur (règles pour l'agent)
PROGRESS.md                où tu en es, langage par langage
docs/                      notes par langage, glossaire, matrice de comparaison
TOOLCHAINS.md              versions installées + commandes vérifiées, langage par langage
conformance/               suite noire commune + fixtures
languages/<lang>/          squelette minimal (build + main vide) — à toi de jouer
journal/                   ton carnet de bord DX, un fichier par langage
.claude/skills/            grill-me, socratic-review, verify-tasklite
```

## Ce que tu es censé en retirer

- **Modéliser un domaine** dans cinq systèmes de types différents (sealed classes, sum types,
  discriminated unions, interfaces + structs).
- **Gérer la concurrence** dans cinq modèles : threads + executor, coroutines, goroutines,
  threads OS / tokio, boucle d'événements.
- **Propager des erreurs** sans exceptions, avec exceptions, avec `Result`, avec des unions.
- **Manipuler des processus** et des timeouts correctement (tuer un arbre de processus, ce que
  presque tout le monde rate au premier essai).
- **Comparer les DX** : build, dépendances, tests, debug, formatage, outillage — et le noter
  dans `journal/`.

## Ordre suggéré

| # | Langage | Pourquoi dans cet ordre |
|---|---------|--------------------------|
| 1 | Java | ton langage quotidien : tu mesures l'écart entre « je sais faire » et « je fais proprement » |
| 2 | Kotlin | mêmes concepts, autre expressivité : tu vois ce que la JVM permet d'autre |
| 3 | Go | l'anti-abstract : peu de features, beaucoup de discipline |
| 4 | Rust | le coût réel de la propriété et des types algébriques |
| 5 | TypeScript | le plus proche de ton quotidien web, mais avec un système de types qui joue dans une autre catégorie |

Tu n'es pas obligé de finir v0 dans un langage avant de passer au suivant. En revanche, ne passe
jamais à un langage **sans avoir rempli la ligne correspondante du journal** : c'est là que
l'apprentissage se fixe.

## Crédits

- `grill-me` est adapté du skill éponyme de **Matt Pocock** (mattpocock/skills), réduit à son os :
  interviewer jusqu'à l'accord explicite, une question à la fois.
- `verify-tasklite` suit la structure du `create-verification-skill` de **Lauren Tan (poteto)** :
  lancer, docteur, piloter, preuves, nettoyage — appliquée ici à une CLI.

Licence MIT (voir `LICENSE`).
