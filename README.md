# Polyglot Lab

Apprendre à chercher, expérimenter et concevoir dans cinq langages.

Le but est de résoudre un problème nouveau sans dépendre d'une réponse de l'agent.
Chaque langage a un petit projet qui grandit avec les concepts étudiés. Tu écris le code,
recherches les garanties dans la documentation officielle et confrontes tes idées à des expériences.

## Choisir un parcours

| Langage | Projet | Concepts centraux |
|---|---|---|
| [Java](docs/parcours/java.md) | Catalogue de livres en CLI | Domaine, collections, contrats, fichiers, concurrence JVM |
| [Kotlin](docs/parcours/kotlin.md) | Agrégateur de bulletins locaux | Nullabilité, transformations, coroutines, annulation, Flow |
| [Go](docs/parcours/go.md) | Vérificateur de services HTTP | Erreurs, interfaces, HTTP, contextes, goroutines |
| [Rust](docs/parcours/rust.md) | Recherche dans des fichiers | Ownership, emprunts, Result, itérateurs, traits, mémoire |
| [TypeScript](docs/parcours/typescript.md) | Explorateur de rapports JSON | Validation runtime, unions, génériques, modules, asynchronisme |

Les projets sont indépendants. Commence par celui qui t'attire ; Java est un point de départ
naturel si tu le pratiques déjà. Chaque parcours va d'un noyau utilisable à des extensions
facultatives. On ajoute une difficulté lorsqu'on sait quel besoin elle résout.

## Première session

1. Lis le contrat minimal et P0 du parcours choisi.
2. Vérifie [l'environnement](TOOLCHAINS.md) : les anciens chemins Linux ne prouvent pas que cette machine est prête.
3. Lis [la méthode](docs/methode.md) et ouvre le [modèle de journal](journal/TEMPLATE.md).
4. Formule une question, trouve une source officielle, prédis un résultat, puis expérimente.

Une session de 30 à 60 minutes peut se terminer par une preuve ou un blocage précis.
Il n'est pas nécessaire de finir un palier à chaque session.

## Se repérer

- [Méthode](docs/methode.md) : recherche, expériences, aide et validation.
- [Progression](PROGRESS.md) : fonctionnement, compréhension et autonomie séparés.
- [Comparaison](docs/comparison.md) : rapprocher des expériences réellement vécues.
- `journal/` : prédictions, sources, résultats et reprises sans aide.
- `evidence/` : commandes et sorties réelles, reliées au journal.
- [AGENTS.md](AGENTS.md) : contrat pédagogique de l'agent.

## Où écrire le code

Les nouveaux projets se développent dans `projects/<langage>/`, à créer au premier palier.
Tu choisis et initialises toi-même le build avec la documentation. Les fiches fournissent les
comportements à vérifier ; elles ne fournissent ni implémentation ni suite de tests exécutable.
Les essais isolés peuvent vivre dans `experiments/<langage>/`.

## Tasklite : atelier facultatif de transfert

Le kata initial reste disponible pour appliquer tes acquis ou comparer un même comportement
entre deux langages. Son contrat est [SPEC.md](SPEC.md), ses squelettes sont dans `languages/`
et sa suite dédiée dans [conformance/](conformance/README.md). Les jalons M0–M6 ne concernent
que tasklite. Les guides `docs/<langage>.md` restent des références pour ce kata.

Licence MIT. Les skills locaux sont adaptés des travaux de Matt Pocock (`grill-me`)
et Lauren Tan (`verify-tasklite`).
