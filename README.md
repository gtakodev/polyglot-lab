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

## Démarrer

```bash
git clone <ce-repo> polyglot-lab && cd polyglot-lab
cat SPEC.md                      # ce que doit faire tasklite
cat docs/choose-your-language.md # par où commencer, et pourquoi
```

Puis, pour le langage choisi :

```bash
cd languages/java        # ou kotlin, go, rust, typescript
# lire le README.md du dossier (build/run/test)
```

Et à chaque milestone :

```bash
python3 conformance/run.py --cmd "<commande qui lance ton binaire>"
# ex. depuis languages/go : --cmd "go run ."
# ex. depuis languages/rust : --cmd "cargo run --quiet --"
```

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
