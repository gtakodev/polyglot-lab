# TypeScript — explorateur de rapports JSON

[Méthode commune](../methode.md) · [Progression](../../PROGRESS.md)

## Contrat minimal

Une CLI lit un fichier JSON contenant des rapports avec id, titre et état, valide les entrées puis affiche un résumé. Commence avec deux états que tu définis et un fichier local. Pas de serveur ou interface graphique au départ.

## Préparer le terrain

Travail dans `projects/typescript/` ; expériences dans `experiments/typescript/`.
Vérifie le compilateur, le build et un test minimal avant P0. Choisis les versions avec
[TOOLCHAINS.md](../../TOOLCHAINS.md) et consigne-les. Les tests ci-dessous sont à écrire.

## Porte d’entrée documentaire

[Documentation officielle](https://www.typescriptlang.org/docs/handbook/intro.html). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

Pour le runtime : [documentation Node](https://nodejs.org/api/). Vérifie la version et la prise en charge des API utilisées.

## P0 — Faire entrer une donnée

**Concepts :** unknown, narrowing, validation runtime, strict.

**À rechercher :** Retrouve narrowing dans le Handbook : quelle garantie existe encore après compilation en JavaScript ?

**Expérience avant intégration :** Donne au même point d’entrée un objet valide, null et un champ du mauvais type ; compare un cast à une validation.

**Preuve de fonctionnement :** Les entrées invalides sont rejetées avec leur emplacement ; les données valides ont un type précis après validation.

**Transfert lors d’une autre session :** Ajoute un champ facultatif et distingue absence, null et valeur invalide.

## P1 — Représenter les états

**Concepts :** Unions discriminées, exhaustivité, never, propriétés propres à un état.

**À rechercher :** Quelles formes ta représentation permet-elle de construire ? Où veux-tu être averti lorsqu’un état apparaît ?

**Expérience avant intégration :** Ajoute un état dans un essai isolé et constate quels consommateurs le compilateur signale.

**Preuve de fonctionnement :** Résumé pour chaque état ; impossibilités métier rejetées à l’entrée ; traitement exhaustif démontré par un essai de compilation.

**Transfert lors d’une autre session :** Introduis un état avec ses propres données sans multiplier les champs facultatifs.

## P2 — Réutiliser une relation

**Concepts :** Génériques, keyof, types indexés, inférence ; types structuraux.

**À rechercher :** Dans generics et keyof, quelle relation entre entrée et sortie veux-tu préserver ? Une union suffirait-elle ?

**Expérience avant intégration :** Compare deux usages concrets d’une transformation ; teste à la compilation une clé valide puis une clé incompatible.

**Preuve de fonctionnement :** Une opération réutilisée préserve les types utiles sans cast aveugle ; tests runtime plus cas de compilation attendus.

**Transfert lors d’une autre session :** Ajoute un second format de rapport et identifie ce qui mérite réellement d’être commun.

## P3 — Charger plusieurs sources

**Concepts :** Promise, async/await, erreurs, AbortSignal selon API, limites de concurrence.

**À rechercher :** Dans la documentation Node correspondant à ta version, cherche l’annulation de l’API utilisée. Rejeter une Promise arrête-t-il le travail ?

**Expérience avant intégration :** Utilise des sources locales simulées, lentes ou défaillantes ; compte opérations actives et opérations encore en cours après annulation.

**Preuve de fonctionnement :** Limite K observée ; erreurs partielles selon contrat ; arrêt attendu des opérations ; aucune rejection non traitée.

**Transfert lors d’une autre session :** Change la politique de résultat partiel et vérifie l’effet sur le type public.

## P4 — Publier une frontière claire

**Concepts :** Modules ESM, exports, déclarations de types et séparation bibliothèque/CLI.

**À rechercher :** Cherche modules et module resolution : quel code résout le compilateur, quel code charge Node ?

**Expérience avant intégration :** Utilise le build depuis un petit consommateur séparé ; teste un import public et une entrée runtime invalide.

**Preuve de fonctionnement :** Consommateur exécuté avec Node ; types disponibles ; aucun effet de CLI au simple import ; tests depuis le build.

**Transfert lors d’une autre session :** Utilise la bibliothèque depuis JavaScript et explique quelles protections restent actives.

## Aller plus loin

Ajouter un petit visualiseur web pour explorer DOM et événements typés ; étudier un schéma de validation et ses types inférés ; explorer streams avec consommateur lent. Un axe à la fois.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
Tu peux aussi choisir un jalon de [tasklite](../../SPEC.md) pour tester le transfert vers un autre domaine.
