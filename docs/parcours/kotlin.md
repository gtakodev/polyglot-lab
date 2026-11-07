# Kotlin — agrégateur de bulletins

[Méthode commune](../methode.md) · [Progression](../../PROGRESS.md)

## Contrat minimal

Une CLI lit des bulletins locaux (source, titre, date) et affiche une sélection. Commence par une liste en mémoire, puis des fichiers. Un titre absent est refusé ; un auteur absent est accepté. Les sources lentes sont simulées localement avant tout réseau.

## Préparer le terrain

Travail dans `projects/kotlin/` ; expériences dans `experiments/kotlin/`.
Vérifie le compilateur, le build et un test minimal avant P0. Choisis les versions avec
[TOOLCHAINS.md](../../TOOLCHAINS.md) et consigne-les. Les tests ci-dessous sont à écrire.

## Porte d’entrée documentaire

[Documentation officielle](https://kotlinlang.org/docs/home.html). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

Pour la partie asynchrone : [guide officiel des coroutines](https://kotlinlang.org/docs/coroutines-guide.html).

## P0 — Absence et validité

**Concepts :** Types nullables, smart casts, data class, expressions.

**À rechercher :** Quelle différence entre valeur absente et chaîne vide ? Retrouve les sections null safety et data classes.

**Expérience avant intégration :** Prédis le comportement avec auteur absent, titre vide et titre absent ; confronte compilation et exécution.

**Preuve de fonctionnement :** Afficher un bulletin valide avec ou sans auteur ; refuser un titre absent ou vide avec une erreur explicite.

**Transfert lors d’une autre session :** Ajoute un champ facultatif sans inventer une valeur trompeuse.

## P1 — Transformer une collection

**Concepts :** Fonctions d’ordre supérieur, extensions, collections et Sequence.

**À rechercher :** Quand une transformation est-elle exécutée ? Les extensions ajoutent-elles réellement des membres à une classe ?

**Expérience avant intégration :** Compte les appels d’une transformation eager puis lazy sur une sélection limitée ; observe aussi une collection vide.

**Preuve de fonctionnement :** Filtrer, dédupliquer et trier des bulletins selon des règles écrites ; mêmes résultats avec les deux approches.

**Transfert lors d’une autre session :** Ajoute un regroupement par source sans recopier une boucle existante.

## P2 — Décrire les résultats

**Concepts :** Sealed interface, when, erreurs de domaine et parsing aux frontières.

**À rechercher :** Où le compilateur vérifie-t-il les cas de when ? Que perd-on avec une branche générale ?

**Expérience avant intégration :** Ajoute un résultat possible à une expérience isolée et observe les usages signalés par le compilateur.

**Preuve de fonctionnement :** Distinguer source vide, illisible et valide ; une entrée malformée suit une politique écrite et testée.

**Transfert lors d’une autre session :** Introduis un résultat partiel et explique qui doit décider de l’afficher.

## P3 — Charger et annuler

**Concepts :** suspend, coroutineScope, dispatchers, annulation coopérative ; bibliothèque kotlinx.coroutines à étudier puis ajouter toi-même.

**À rechercher :** Dans le guide officiel des coroutines, retrouve cancellation and timeouts : suspend signifie-t-il exécuter sur un autre thread ?

**Expérience avant intégration :** Simule deux sources lentes et une qui échoue. Prédis quels traitements survivent dans chaque politique de scope.

**Preuve de fonctionnement :** Charger avec une limite explicite ; annuler pendant l’attente ; vérifier fermeture des ressources et absence de travail résiduel.

**Transfert lors d’une autre session :** Passe d’une politique tout-ou-rien à une politique partielle et justifie la frontière de supervision.

## P4 — Produire un flux

**Concepts :** Flow, flux froid, collecte, buffer et pression du consommateur.

**À rechercher :** Dans le guide Flow, cherche ce qui démarre réellement un flux et ce qui se passe avec deux collecteurs.

**Expérience avant intégration :** Compte les productions avec zéro, un puis deux collecteurs ; ralentis le consommateur et prédis les valeurs reçues.

**Preuve de fonctionnement :** Afficher progressivement les bulletins ; tester arrêt du collecteur et politique explicite de conservation ou de perte des valeurs.

**Transfert lors d’une autre session :** Introduis le partage d’un flux et explique sa durée de vie.

## Aller plus loin

Construire un petit DSL de sélection seulement après deux usages réels ; tester le temps virtuel des coroutines ; étudier interop Java et platform types. Une extension à la fois.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
Tu peux aussi choisir un jalon de [tasklite](../../SPEC.md) pour tester le transfert vers un autre domaine.
