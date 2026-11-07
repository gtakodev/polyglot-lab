# Java — catalogue de livres

[Méthode commune](../methode.md) · [Progression](../../PROGRESS.md)

## Contrat minimal

Une CLI ajoute et liste des livres en mémoire. Chaque livre a un identifiant et un titre non vides ; un identifiant déjà présent est refusé sans modifier le catalogue. Pas de framework, réseau ou base de données au départ.

## Préparer le terrain

Travail dans `projects/java/` ; expériences dans `experiments/java/`.
Vérifie le compilateur, le build et un test minimal avant P0. Choisis les versions avec
[TOOLCHAINS.md](../../TOOLCHAINS.md) et consigne-les. Les tests ci-dessous sont à écrire.

## Porte d’entrée documentaire

[Documentation officielle](https://dev.java/learn/). Cherche toi-même la section mentionnée dans le palier.
Note la page précise et la garantie trouvée avant de demander une explication.
Lis un seul palier à la fois ; les suivants donnent une direction, pas une architecture à anticiper.

## P0 — Une entrée, une erreur

**Concepts :** Arguments, types, méthodes, exceptions ; distinguer erreur utilisateur et erreur de programmation.

**À rechercher :** Comment signaler une entrée invalide sans perdre sa cause ? Retrouve les sections sur les exceptions et le lancement d’un programme.

**Expérience avant intégration :** Prédis le résultat avec un titre vide, puis un identifiant dupliqué. Observe aussi l’état du catalogue après le refus.

**Preuve de fonctionnement :** Ajouter et lister deux livres ; refuser les deux erreurs sans altérer les livres existants.

**Transfert lors d’une autre session :** Ajoute une nouvelle règle sur un champ et explique où elle doit être vérifiée.

## P1 — Modéliser des opérations

**Concepts :** Records, égalité, collections et états de prêt ; explorer les interfaces scellées lorsque plusieurs formes sont nécessaires.

**À rechercher :** Que garantit réellement un record si un composant est une collection mutable ? Cherche records, equals et copies de collections.

**Expérience avant intégration :** Compare égalité et identité ; modifie une collection utilisée pour construire une valeur et prédis ce que cette valeur expose.

**Preuve de fonctionnement :** Emprunter puis rendre un livre ; refuser un second emprunt et un retour impossible. Explique les états que ton modèle autorise.

**Transfert lors d’une autre session :** Ajoute une réservation en définissant ses transitions avant de choisir sa représentation.

## P2 — Rechercher et transformer

**Concepts :** Collections, Comparator, Stream, Optional ; coût et lisibilité des transformations.

**À rechercher :** Quelles opérations de Stream sont intermédiaires et terminales ? Quelle garantie sur l’ordre utilises-tu ?

**Expérience avant intégration :** Compare une boucle et un pipeline sur les mêmes données : catalogue vide, égalités de titres, filtre sans résultat.

**Preuve de fonctionnement :** Recherche par titre et tri déterministe selon une règle écrite ; mêmes résultats pour les deux versions.

**Transfert lors d’une autre session :** Ajoute un regroupement par auteur et justifie la collection de sortie.

## P3 — Sauvegarder sans perdre

**Concepts :** Path, fichiers, encodage, try-with-resources, erreurs d’I/O.

**À rechercher :** Quand une ressource se ferme-t-elle si la lecture échoue ? Quelles garanties offre le remplacement d’un fichier sur ton système ?

**Expérience avant intégration :** Provoque fichier absent, contenu invalide et échec d’écriture dans un dossier temporaire.

**Preuve de fonctionnement :** Aller-retour sauvegarde/lecture ; une lecture invalide conserve le catalogue courant ; une sauvegarde échouée ne détruit pas la précédente.

**Transfert lors d’une autre session :** Fais évoluer le format et traite explicitement une ancienne version.

## P4 — Enrichir en concurrence

**Concepts :** ExecutorService, Future, threads virtuels selon JDK, limites de ressources ; pas de preview nécessaire.

**À rechercher :** Un thread virtuel borne-t-il le nombre de requêtes ? Où sont attendues les erreurs et comment arrête-t-on le travail ?

**Expérience avant intégration :** Avec un fournisseur local simulé, compare séquentiel et concurrent ; compte les opérations actives au lieu de supposer la limite respectée.

**Preuve de fonctionnement :** Enrichir N livres avec au plus K opérations actives ; tester erreur et annulation, puis vérifier qu’aucune opération ne continue après la fermeture.

**Transfert lors d’une autre session :** Change la politique d’échec et explique quels résultats partiels restent utilisables.

## Aller plus loin

Profiler une recherche avec JFR ; comparer deux collections sur des données mesurées ; explorer modules et packaging. Choisis un seul axe et une question mesurable.

Avant une extension, écris le besoin, la notion à explorer et la preuve de fin.
Tu peux aussi choisir un jalon de [tasklite](../../SPEC.md) pour tester le transfert vers un autre domaine.
