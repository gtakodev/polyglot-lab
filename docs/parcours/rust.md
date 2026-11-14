# Rust — recherche dans les fichiers

[Accueil](../../README.md) · [Mon journal](../../journal/rust.md)

## Contrat minimal

Une CLI cherche un texte littéral dans un fichier UTF-8 et affiche les lignes correspondantes avec leur numéro. Définis les codes de sortie pour résultat, absence et erreur. Commence sensible à la casse, sans regex ni récursion.

## Première session

1. Crée `projects/rust/`. Vérifie les outils du langage et leur version, puis fais compiler un programme minimal et exécuter un test. Si cela bloque, consulte [l’environnement](../../TOOLCHAINS.md).
2. Lis seulement P0 ci-dessous. Écris avec tes mots les entrées, sorties et erreurs attendues ; fixe les choix laissés ouverts par le contrat.
3. Formule ta première question de recherche. Utilise le portail officiel ci-dessous pour trouver une réponse, puis prédis le résultat d’un petit essai avant de l’exécuter.
4. Applique ce que tu as vérifié au projet. Contrôle les cas de la rubrique **À vérifier**.
5. Dans [ton journal](../../journal/rust.md), note la source, la prédiction, la commande et son résultat, puis une prochaine action précise.

Tu peux t’arrêter après une seule expérience. Les essais isolés vont dans `experiments/rust/`.
Si tu travailles avec l’agent, indique « Je commence Rust, P0 » : il te guide une question à la fois, sans écrire ta solution.

## Quand passer à la suite

Passe au palier suivant lorsque les cas demandés fonctionnent et que tu peux expliquer ton choix et une limite. Note ces preuves dans [la progression](../../PROGRESS.md). Lors d’une autre session, essaie la variante proposée sans indice de l’agent ; la documentation reste autorisée.

## Porte d’entrée documentaire

[Documentation officielle](https://doc.rust-lang.org/book/). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

## Étapes du projet

P0 — Lire et échouer → P1 — Posséder ou emprunter → P2 — Parcourir sans tout charger → P3 — Plusieurs fichiers → P4 — Paralléliser avec raison

Lis uniquement le palier en cours.

## P0 — Lire et échouer

**Concepts :** Cargo, String, fonctions, Result, propagation avec ?.

**À rechercher :** Retrouve le chapitre error handling : quelle erreur est récupérable et quel contexte doit rester visible ?

**Expérience avant intégration :** Prédis fichier absent, vide et non UTF-8 ; distingue absence de correspondance et impossibilité de lire.

**À vérifier :** Numéros de lignes exacts ; erreurs explicites selon le contrat ; aucun panic pour ces entrées utilisateur.

**Plus tard, sans aide :** Ajoute une erreur d’argument et conserve des codes de sortie distincts.

## P1 — Posséder ou emprunter

**Concepts :** Ownership, &str, &String, slices et durée de vie.

**À rechercher :** Dans ownership, cherche ce qui fait vivre une vue sur des données. Une annotation de lifetime prolonge-t-elle leur vie ?

**Expérience avant intégration :** Écris deux petits essais : résultat possédé et résultat emprunté ; tente de libérer la source avant de lire le résultat et explique le diagnostic.

**À vérifier :** Recherche sans copie injustifiée de chaque ligne ; explique le propriétaire de chaque résultat et justifie les copies conservées.

**Plus tard, sans aide :** Rends un résultat indépendant du fichier source et explique le coût du changement.

## P2 — Parcourir sans tout charger

**Concepts :** Iterator, closures, BufRead, traits et génériques.

**À rechercher :** Cherche Iterator et BufRead dans la stdlib depuis le Book : où peuvent survenir les erreurs pendant le parcours ?

**Expérience avant intégration :** Compare lecture entière et lecture progressive sur la même entrée ; injecte une erreur via un lecteur de test.

**À vérifier :** Mêmes lignes et numéros ; erreur de lecture propagée ; entrée acceptée depuis un lecteur sans dépendre du disque dans les tests.

**Plus tard, sans aide :** Ajoute une limite de résultats et vérifie quand la lecture s’arrête.

## P3 — Plusieurs fichiers

**Concepts :** Modules, enums d’erreurs, chemins et séparation bibliothèque/CLI.

**À rechercher :** Quels cas d’erreur le consommateur doit-il distinguer ? Cherche les chapitres packages, modules et tests.

**Expérience avant intégration :** Mélange fichier lisible, illisible et répertoire ; prédis la sortie selon une politique d’échec écrite.

**À vérifier :** Recherche multifichier déterministe ; chemins dans les erreurs ; tests de CLI et tests du cœur séparés.

**Plus tard, sans aide :** Accepte une nouvelle source de données et justifie ce qui doit rester public.

## P4 — Paralléliser avec raison

**Concepts :** Threads bornés, Send, Sync, ownership transféré ; comparaison avec la version séquentielle.

**À rechercher :** Cherche fearless concurrency : que garantissent Send et Sync, et que ne garantissent-ils pas ?

**Expérience avant intégration :** Traite des fichiers de tailles différentes avec une limite K ; prédis ordre, mémoire retenue et réaction à une erreur.

**À vérifier :** Même ensemble de résultats ; limite observée ; tous les threads attendus ; mesure avant/après sans promettre un gain.

**Plus tard, sans aide :** Change la politique d’ordre et explique le compromis mémoire/latence.

## Aller plus loin

Explorer Unicode et recherche insensible à la casse ; étudier mmap et ses garanties ; comparer un cas I/O async avec des threads. Pas de unsafe ou runtime async ajouté sans question concrète.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
