# Java — catalogue de livres

[Accueil](../../README.md) · [Mon journal](../../journal/java.md)

## Contrat minimal

Une CLI ajoute et liste des livres en mémoire. Chaque livre a un identifiant et un titre non vides ; un identifiant déjà présent est refusé sans modifier le catalogue. Pas de framework, réseau ou base de données au départ.

## Première session

1. Crée `projects/java/`. Vérifie les outils du langage et leur version, puis fais compiler un programme minimal et exécuter un test. Si cela bloque, consulte [l’environnement](../../TOOLCHAINS.md).
2. Lis seulement P0 ci-dessous. Écris avec tes mots les entrées, sorties et erreurs attendues ; fixe les choix laissés ouverts par le contrat.
3. Formule ta première question de recherche. Utilise le portail officiel ci-dessous pour trouver une réponse, puis prédis le résultat d’un petit essai avant de l’exécuter.
4. Applique ce que tu as vérifié au projet. Contrôle les cas de la rubrique **À vérifier**.
5. Dans [ton journal](../../journal/java.md), note la source, la prédiction, la commande et son résultat, puis une prochaine action précise.

Tu peux t’arrêter après une seule expérience. Les essais isolés vont dans `experiments/java/`.
Si tu travailles avec l’agent, indique « Je commence Java, P0 » : il te guide une question à la fois, sans écrire ta solution.

## Quand passer à la suite

Passe au palier suivant lorsque les cas demandés fonctionnent et que tu peux expliquer ton choix et une limite. Note ces preuves dans [la progression](../../PROGRESS.md). Lors d’une autre session, essaie la variante proposée sans indice de l’agent ; la documentation reste autorisée.

## Porte d’entrée documentaire

[Documentation officielle](https://dev.java/learn/). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

## Étapes du projet

P0 — Une entrée, une erreur → P1 — Modéliser des opérations → P2 — Rechercher et transformer → P3 — Sauvegarder sans perdre → P4 — Enrichir en concurrence

Lis uniquement le palier en cours.

## P0 — Une entrée, une erreur

**Concepts :** Arguments, types, méthodes, exceptions ; distinguer erreur utilisateur et erreur de programmation.

**À rechercher :** Comment signaler une entrée invalide sans perdre sa cause ? Retrouve les sections sur les exceptions et le lancement d’un programme.

**Expérience avant intégration :** Prédis le résultat avec un titre vide, puis un identifiant dupliqué. Observe aussi l’état du catalogue après le refus.

**À vérifier :** Ajouter et lister deux livres ; refuser les deux erreurs sans altérer les livres existants.

**Plus tard, sans aide :** Ajoute une nouvelle règle sur un champ et explique où elle doit être vérifiée.

## P1 — Modéliser des opérations

**Concepts :** Records, égalité, collections et états de prêt ; explorer les interfaces scellées lorsque plusieurs formes sont nécessaires.

**À rechercher :** Que garantit réellement un record si un composant est une collection mutable ? Cherche records, equals et copies de collections.

**Expérience avant intégration :** Compare égalité et identité ; modifie une collection utilisée pour construire une valeur et prédis ce que cette valeur expose.

**À vérifier :** Emprunter puis rendre un livre ; refuser un second emprunt et un retour impossible. Explique les états que ton modèle autorise.

**Plus tard, sans aide :** Ajoute une réservation en définissant ses transitions avant de choisir sa représentation.

## P2 — Rechercher et transformer

**Concepts :** Collections, Comparator, Stream, Optional ; coût et lisibilité des transformations.

**À rechercher :** Quelles opérations de Stream sont intermédiaires et terminales ? Quelle garantie sur l’ordre utilises-tu ?

**Expérience avant intégration :** Compare une boucle et un pipeline sur les mêmes données : catalogue vide, égalités de titres, filtre sans résultat.

**À vérifier :** Recherche par titre et tri déterministe selon une règle écrite ; mêmes résultats pour les deux versions.

**Plus tard, sans aide :** Ajoute un regroupement par auteur et justifie la collection de sortie.

## P3 — Sauvegarder sans perdre

**Concepts :** Path, fichiers, encodage, try-with-resources, erreurs d’I/O.

**À rechercher :** Quand une ressource se ferme-t-elle si la lecture échoue ? Quelles garanties offre le remplacement d’un fichier sur ton système ?

**Expérience avant intégration :** Provoque fichier absent, contenu invalide et échec d’écriture dans un dossier temporaire.

**À vérifier :** Aller-retour sauvegarde/lecture ; une lecture invalide conserve le catalogue courant ; une sauvegarde échouée ne détruit pas la précédente.

**Plus tard, sans aide :** Fais évoluer le format et traite explicitement une ancienne version.

## P4 — Enrichir en concurrence

**Concepts :** ExecutorService, Future, threads virtuels selon JDK, limites de ressources ; pas de preview nécessaire.

**À rechercher :** Un thread virtuel borne-t-il le nombre de requêtes ? Où sont attendues les erreurs et comment arrête-t-on le travail ?

**Expérience avant intégration :** Avec un fournisseur local simulé, compare séquentiel et concurrent ; compte les opérations actives au lieu de supposer la limite respectée.

**À vérifier :** Enrichir N livres avec au plus K opérations actives ; tester erreur et annulation, puis vérifier qu’aucune opération ne continue après la fermeture.

**Plus tard, sans aide :** Change la politique d’échec et explique quels résultats partiels restent utilisables.

## Aller plus loin

Profiler une recherche avec JFR ; comparer deux collections sur des données mesurées ; explorer modules et packaging. Choisis un seul axe et une question mesurable.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
