# Kotlin — agrégateur de bulletins

[Accueil](../../README.md) · [Mon journal](../../journal/kotlin.md)

## Contrat minimal

Une CLI lit des bulletins locaux (source, titre, date) et affiche une sélection. Commence par une liste en mémoire, puis des fichiers. Un titre absent est refusé ; un auteur absent est accepté. Les sources lentes sont simulées localement avant tout réseau.

## Première session

1. Crée `projects/kotlin/`. Vérifie les outils du langage et leur version, puis fais compiler un programme minimal et exécuter un test. Si cela bloque, consulte [l’environnement](../../TOOLCHAINS.md).
2. Lis seulement P0 ci-dessous. Écris avec tes mots les entrées, sorties et erreurs attendues ; fixe les choix laissés ouverts par le contrat.
3. Formule ta première question de recherche. Utilise le portail officiel ci-dessous pour trouver une réponse, puis prédis le résultat d’un petit essai avant de l’exécuter.
4. Applique ce que tu as vérifié au projet. Contrôle les cas de la rubrique **À vérifier**.
5. Dans [ton journal](../../journal/kotlin.md), note la source, la prédiction, la commande et son résultat, puis une prochaine action précise.

Tu peux t’arrêter après une seule expérience. Les essais isolés vont dans `experiments/kotlin/`.
Si tu travailles avec l’agent, indique « Je commence Kotlin, P0 » : il te guide une question à la fois, sans écrire ta solution.

## Quand passer à la suite

Passe au palier suivant lorsque les cas demandés fonctionnent et que tu peux expliquer ton choix et une limite. Note ces preuves dans [la progression](../../PROGRESS.md). Lors d’une autre session, essaie la variante proposée sans indice de l’agent ; la documentation reste autorisée.

## Porte d’entrée documentaire

[Documentation officielle](https://kotlinlang.org/docs/home.html). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

Pour la partie asynchrone : [guide officiel des coroutines](https://kotlinlang.org/docs/coroutines-guide.html).

## Étapes du projet

P0 — Absence et validité → P1 — Transformer une collection → P2 — Décrire les résultats → P3 — Charger et annuler → P4 — Produire un flux

Lis uniquement le palier en cours.

## P0 — Absence et validité

**Concepts :** Types nullables, smart casts, data class, expressions.

**À rechercher :** Quelle différence entre valeur absente et chaîne vide ? Retrouve les sections null safety et data classes.

**Expérience avant intégration :** Prédis le comportement avec auteur absent, titre vide et titre absent ; confronte compilation et exécution.

**À vérifier :** Afficher un bulletin valide avec ou sans auteur ; refuser un titre absent ou vide avec une erreur explicite.

**Plus tard, sans aide :** Ajoute un champ facultatif sans inventer une valeur trompeuse.

## P1 — Transformer une collection

**Concepts :** Fonctions d’ordre supérieur, extensions, collections et Sequence.

**À rechercher :** Quand une transformation est-elle exécutée ? Les extensions ajoutent-elles réellement des membres à une classe ?

**Expérience avant intégration :** Compte les appels d’une transformation eager puis lazy sur une sélection limitée ; observe aussi une collection vide.

**À vérifier :** Filtrer, dédupliquer et trier des bulletins selon des règles écrites ; mêmes résultats avec les deux approches.

**Plus tard, sans aide :** Ajoute un regroupement par source sans recopier une boucle existante.

## P2 — Décrire les résultats

**Concepts :** Sealed interface, when, erreurs de domaine et parsing aux frontières.

**À rechercher :** Où le compilateur vérifie-t-il les cas de when ? Que perd-on avec une branche générale ?

**Expérience avant intégration :** Ajoute un résultat possible à une expérience isolée et observe les usages signalés par le compilateur.

**À vérifier :** Distinguer source vide, illisible et valide ; une entrée malformée suit une politique écrite et testée.

**Plus tard, sans aide :** Introduis un résultat partiel et explique qui doit décider de l’afficher.

## P3 — Charger et annuler

**Concepts :** suspend, coroutineScope, dispatchers, annulation coopérative ; bibliothèque kotlinx.coroutines à étudier puis ajouter toi-même.

**À rechercher :** Dans le guide officiel des coroutines, retrouve cancellation and timeouts : suspend signifie-t-il exécuter sur un autre thread ?

**Expérience avant intégration :** Simule deux sources lentes et une qui échoue. Prédis quels traitements survivent dans chaque politique de scope.

**À vérifier :** Charger avec une limite explicite ; annuler pendant l’attente ; vérifier fermeture des ressources et absence de travail résiduel.

**Plus tard, sans aide :** Passe d’une politique tout-ou-rien à une politique partielle et justifie la frontière de supervision.

## P4 — Produire un flux

**Concepts :** Flow, flux froid, collecte, buffer et pression du consommateur.

**À rechercher :** Dans le guide Flow, cherche ce qui démarre réellement un flux et ce qui se passe avec deux collecteurs.

**Expérience avant intégration :** Compte les productions avec zéro, un puis deux collecteurs ; ralentis le consommateur et prédis les valeurs reçues.

**À vérifier :** Afficher progressivement les bulletins ; tester arrêt du collecteur et politique explicite de conservation ou de perte des valeurs.

**Plus tard, sans aide :** Introduis le partage d’un flux et explique sa durée de vie.

## Aller plus loin

Construire un petit DSL de sélection seulement après deux usages réels ; tester le temps virtuel des coroutines ; étudier interop Java et platform types. Une extension à la fois.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
