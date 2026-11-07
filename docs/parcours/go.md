# Go — vérificateur de services HTTP

[Méthode commune](../methode.md) · [Progression](../../PROGRESS.md)

## Contrat minimal

Une CLI vérifie une liste d’URL et rapporte réponse HTTP, erreur de transport ou expiration. Commence avec un serveur HTTP de test sur la machine, sans dépendre d’Internet. Écris la règle de santé (par exemple les codes admis) avant de coder.

## Préparer le terrain

Travail dans `projects/go/` ; expériences dans `experiments/go/`.
Vérifie le compilateur, le build et un test minimal avant P0. Choisis les versions avec
[TOOLCHAINS.md](../../TOOLCHAINS.md) et consigne-les. Les tests ci-dessous sont à écrire.

## Porte d’entrée documentaire

[Documentation officielle](https://go.dev/doc/). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

## P0 — Un contrôle explicite

**Concepts :** Packages, structs, fonctions, error, zéro des valeurs.

**À rechercher :** Comment distinguer une réponse HTTP d’une erreur de transport ? Cherche net/http dans la bibliothèque standard.

**Expérience avant intégration :** Teste une réponse admise, une réponse refusée et une connexion impossible ; prédis si une réponse existe dans chaque cas.

**Preuve de fonctionnement :** Un rapport par URL et aucune erreur silencieuse ; entrée invalide traitée avant la requête.

**Transfert lors d’une autre session :** Ajoute une erreur de lecture du corps et conserve son contexte.

## P1 — Dépendre du minimum

**Concepts :** Interfaces satisfaites implicitement, composition, io, defer.

**À rechercher :** Qui doit déclarer une petite interface ? Quand defer s’exécute-t-il dans une boucle ?

**Expérience avant intégration :** Remplace le client par un double contrôlé ; observe la fermeture des corps de réponse sur succès et erreur.

**Preuve de fonctionnement :** Tests sans réseau externe ; ressources fermées ; l’interface ne demande que les comportements utilisés.

**Transfert lors d’une autre session :** Fournis une autre source d’URL sans changer le contrôle HTTP.

## P2 — Borner et annuler

**Concepts :** Goroutines, channels, context, propriété de la fermeture.

**À rechercher :** Retrouve les contrats de context et de fermeture de channel. Qui peut encore envoyer au moment où tu fermes ?

**Expérience avant intégration :** Bloque volontairement un serveur local puis annule ; compte les requêtes actives et les résultats produits.

**Preuve de fonctionnement :** Au plus K requêtes en cours ; une annulation termine le contrôle dans un délai écrit ; aucun envoi sur canal fermé.

**Transfert lors d’une autre session :** Annule avant le premier envoi puis au milieu ; explique les résultats attendus.

## P3 — Servir et arrêter

**Concepts :** net/http côté serveur, partage d’état, synchronisation, arrêt gracieux.

**À rechercher :** Que garantit Shutdown pour les requêtes en cours ? Cherche comment le handler accède au contexte.

**Expérience avant intégration :** Expose le dernier rapport localement, lis-le pendant une mise à jour et déclenche un arrêt.

**Preuve de fonctionnement :** Rapport cohérent sous accès concurrent ; tester avec go test -race ; fermeture avec requête en cours et limite de temps.

**Transfert lors d’une autre session :** Ajoute une lecture lente et explique ce que l’arrêt peut garantir ou non.

## P4 — Diagnostiquer

**Concepts :** Tests tabulaires, fuzzing du parsing, benchmarks et profils.

**À rechercher :** Quelle différence entre benchmark et profil ? Quelle entrée un fuzz test doit-il pouvoir réduire ?

**Expérience avant intégration :** Mesure une charge locale reproductible ; conserve la référence avant de modifier une seule hypothèse.

**Preuve de fonctionnement :** Un test fuzz cible le parsing sans réseau ; benchmark avec allocations et contexte ; correction vérifiée après optimisation.

**Transfert lors d’une autre session :** Reproduis la mesure sur une autre taille de données et explique si la conclusion tient.

## Aller plus loin

Explorer retries avec budget global, exposition de métriques ou protocole streaming. Écris d’abord le comportement en cas d’arrêt et d’échec ; ne transforme pas ce laboratoire en infrastructure de production.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
Tu peux aussi choisir un jalon de [tasklite](../../SPEC.md) pour tester le transfert vers un autre domaine.
