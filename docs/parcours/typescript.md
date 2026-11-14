# TypeScript — explorateur de rapports JSON

[Accueil](../../README.md) · [Mon journal](../../journal/typescript.md)

## Contrat minimal

Une CLI lit un fichier JSON contenant des rapports avec id, titre et état, valide les entrées puis affiche un résumé. Commence avec deux états que tu définis et un fichier local. Pas de serveur ou interface graphique au départ.

## Première session

1. Crée `projects/typescript/`. Vérifie les outils du langage et leur version, puis fais compiler un programme minimal et exécuter un test. Si cela bloque, consulte [l’environnement](../../TOOLCHAINS.md).
2. Lis seulement P0 ci-dessous. Écris avec tes mots les entrées, sorties et erreurs attendues ; fixe les choix laissés ouverts par le contrat.
3. Formule ta première question de recherche. Utilise le portail officiel ci-dessous pour trouver une réponse, puis prédis le résultat d’un petit essai avant de l’exécuter.
4. Applique ce que tu as vérifié au projet. Contrôle les cas de la rubrique **À vérifier**.
5. Dans [ton journal](../../journal/typescript.md), note la source, la prédiction, la commande et son résultat, puis une prochaine action précise.

Tu peux t’arrêter après une seule expérience. Les essais isolés vont dans `experiments/typescript/`.
Si tu travailles avec l’agent, indique « Je commence TypeScript, P0 » : il te guide une question à la fois, sans écrire ta solution.

## Quand passer à la suite

Passe au palier suivant lorsque les cas demandés fonctionnent et que tu peux expliquer ton choix et une limite. Note ces preuves dans [la progression](../../PROGRESS.md). Lors d’une autre session, essaie la variante proposée sans indice de l’agent ; la documentation reste autorisée.

## Porte d’entrée documentaire

[Documentation officielle](https://www.typescriptlang.org/docs/handbook/intro.html). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

Pour le runtime : [documentation Node](https://nodejs.org/api/). Vérifie la version et la prise en charge des API utilisées.

## Étapes du projet

P0 — Faire entrer une donnée → P1 — Représenter les états → P2 — Réutiliser une relation → P3 — Charger plusieurs sources → P4 — Publier une frontière claire

Lis uniquement le palier en cours.

## P0 — Faire entrer une donnée

**Concepts :** unknown, narrowing, validation runtime, strict.

**À rechercher :** Retrouve narrowing dans le Handbook : quelle garantie existe encore après compilation en JavaScript ?

**Expérience avant intégration :** Donne au même point d’entrée un objet valide, null et un champ du mauvais type ; compare un cast à une validation.

**À vérifier :** Les entrées invalides sont rejetées avec leur emplacement ; les données valides ont un type précis après validation.

**Plus tard, sans aide :** Ajoute un champ facultatif et distingue absence, null et valeur invalide.

## P1 — Représenter les états

**Concepts :** Unions discriminées, exhaustivité, never, propriétés propres à un état.

**À rechercher :** Quelles formes ta représentation permet-elle de construire ? Où veux-tu être averti lorsqu’un état apparaît ?

**Expérience avant intégration :** Ajoute un état dans un essai isolé et constate quels consommateurs le compilateur signale.

**À vérifier :** Résumé pour chaque état ; impossibilités métier rejetées à l’entrée ; traitement exhaustif démontré par un essai de compilation.

**Plus tard, sans aide :** Introduis un état avec ses propres données sans multiplier les champs facultatifs.

## P2 — Réutiliser une relation

**Concepts :** Génériques, keyof, types indexés, inférence ; types structuraux.

**À rechercher :** Dans generics et keyof, quelle relation entre entrée et sortie veux-tu préserver ? Une union suffirait-elle ?

**Expérience avant intégration :** Compare deux usages concrets d’une transformation ; teste à la compilation une clé valide puis une clé incompatible.

**À vérifier :** Une opération réutilisée préserve les types utiles sans cast aveugle ; tests runtime plus cas de compilation attendus.

**Plus tard, sans aide :** Ajoute un second format de rapport et identifie ce qui mérite réellement d’être commun.

## P3 — Charger plusieurs sources

**Concepts :** Promise, async/await, erreurs, AbortSignal selon API, limites de concurrence.

**À rechercher :** Dans la documentation Node correspondant à ta version, cherche l’annulation de l’API utilisée. Rejeter une Promise arrête-t-il le travail ?

**Expérience avant intégration :** Utilise des sources locales simulées, lentes ou défaillantes ; compte opérations actives et opérations encore en cours après annulation.

**À vérifier :** Limite K observée ; erreurs partielles selon contrat ; arrêt attendu des opérations ; aucune rejection non traitée.

**Plus tard, sans aide :** Change la politique de résultat partiel et vérifie l’effet sur le type public.

## P4 — Publier une frontière claire

**Concepts :** Modules ESM, exports, déclarations de types et séparation bibliothèque/CLI.

**À rechercher :** Cherche modules et module resolution : quel code résout le compilateur, quel code charge Node ?

**Expérience avant intégration :** Utilise le build depuis un petit consommateur séparé ; teste un import public et une entrée runtime invalide.

**À vérifier :** Consommateur exécuté avec Node ; types disponibles ; aucun effet de CLI au simple import ; tests depuis le build.

**Plus tard, sans aide :** Utilise la bibliothèque depuis JavaScript et explique quelles protections restent actives.

## Aller plus loin

Ajouter un petit visualiseur web pour explorer DOM et événements typés ; étudier un schéma de validation et ses types inférés ; explorer streams avec consommateur lent. Un axe à la fois.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
