# Go — vérificateur de services HTTP

[Accueil](../../README.md) · [Mon journal](../../journal/go.md)

## Contrat minimal

Une CLI vérifie une liste d’URL et rapporte réponse HTTP, erreur de transport ou expiration. Commence avec un serveur HTTP de test sur la machine, sans dépendre d’Internet. Écris la règle de santé (par exemple les codes admis) avant de coder.

## Première session

1. Crée `projects/go/`. Vérifie les outils du langage et leur version, puis fais compiler un programme minimal et exécuter un test. Si cela bloque, consulte [l’environnement](../../TOOLCHAINS.md).
2. Lis seulement P0 ci-dessous. Écris avec tes mots les entrées, sorties et erreurs attendues ; fixe les choix laissés ouverts par le contrat.
3. Formule ta première question de recherche. Utilise le portail officiel ci-dessous pour trouver une réponse, puis prédis le résultat d’un petit essai avant de l’exécuter.
4. Applique ce que tu as vérifié au projet. Contrôle les cas de la rubrique **À vérifier**.
5. Dans [ton journal](../../journal/go.md), note la source, la prédiction, la commande et son résultat, puis une prochaine action précise.

Tu peux t’arrêter après une seule expérience. Les essais isolés vont dans `experiments/go/`.
Si tu travailles avec l’agent, indique « Je commence Go, P0 » : il te guide une question à la fois, sans écrire ta solution.

## Quand passer à la suite

Passe au palier suivant lorsque les cas demandés fonctionnent et que tu peux expliquer ton choix et une limite. Note ces preuves dans [la progression](../../PROGRESS.md). Lors d’une autre session, essaie la variante proposée sans indice de l’agent ; la documentation reste autorisée.

## Porte d’entrée documentaire

[Documentation officielle](https://go.dev/doc/). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

## Étapes du projet

P0 — Un contrôle explicite → P1 — Dépendre du minimum → P2 — Borner et annuler → P3 — Servir et arrêter → P4 — Diagnostiquer

Lis uniquement le palier en cours.

## P0 — Un contrôle explicite

**Concepts :** Packages, structs, fonctions, error, zéro des valeurs.

**À rechercher :** Comment distinguer une réponse HTTP d’une erreur de transport ? Cherche net/http dans la bibliothèque standard.

**Expérience avant intégration :** Teste une réponse admise, une réponse refusée et une connexion impossible ; prédis si une réponse existe dans chaque cas.

**À vérifier :** Un rapport par URL et aucune erreur silencieuse ; entrée invalide traitée avant la requête.

**Plus tard, sans aide :** Ajoute une erreur de lecture du corps et conserve son contexte.

## P1 — Dépendre du minimum

**Concepts :** Interfaces satisfaites implicitement, composition, io, defer.

**À rechercher :** Qui doit déclarer une petite interface ? Quand defer s’exécute-t-il dans une boucle ?

**Expérience avant intégration :** Remplace le client par un double contrôlé ; observe la fermeture des corps de réponse sur succès et erreur.

**À vérifier :** Tests sans réseau externe ; ressources fermées ; l’interface ne demande que les comportements utilisés.

**Plus tard, sans aide :** Fournis une autre source d’URL sans changer le contrôle HTTP.

## P2 — Borner et annuler

**Concepts :** Goroutines, channels, context, propriété de la fermeture.

**À rechercher :** Retrouve les contrats de context et de fermeture de channel. Qui peut encore envoyer au moment où tu fermes ?

**Expérience avant intégration :** Bloque volontairement un serveur local puis annule ; compte les requêtes actives et les résultats produits.

**À vérifier :** Au plus K requêtes en cours ; une annulation termine le contrôle dans un délai écrit ; aucun envoi sur canal fermé.

**Plus tard, sans aide :** Annule avant le premier envoi puis au milieu ; explique les résultats attendus.

## P3 — Servir et arrêter

**Concepts :** net/http côté serveur, partage d’état, synchronisation, arrêt gracieux.

**À rechercher :** Que garantit Shutdown pour les requêtes en cours ? Cherche comment le handler accède au contexte.

**Expérience avant intégration :** Expose le dernier rapport localement, lis-le pendant une mise à jour et déclenche un arrêt.

**À vérifier :** Rapport cohérent sous accès concurrent ; tester avec go test -race ; fermeture avec requête en cours et limite de temps.

**Plus tard, sans aide :** Ajoute une lecture lente et explique ce que l’arrêt peut garantir ou non.

## P4 — Diagnostiquer

**Concepts :** Tests tabulaires, fuzzing du parsing, benchmarks et profils.

**À rechercher :** Quelle différence entre benchmark et profil ? Quelle entrée un fuzz test doit-il pouvoir réduire ?

**Expérience avant intégration :** Mesure une charge locale reproductible ; conserve la référence avant de modifier une seule hypothèse.

**À vérifier :** Un test fuzz cible le parsing sans réseau ; benchmark avec allocations et contexte ; correction vérifiée après optimisation.

**Plus tard, sans aide :** Reproduis la mesure sur une autre taille de données et explique si la conclusion tient.

## Aller plus loin

Explorer retries avec budget global, exposition de métriques ou protocole streaming. Écris d’abord le comportement en cas d’arrêt et d’échec ; ne transforme pas ce laboratoire en infrastructure de production.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
