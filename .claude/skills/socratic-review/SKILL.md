---
name: socratic-review
description: Revoir sur demande le code d’un parcours ou de tasklite, par une question à la fois, sans le réécrire.
---

# Revue socratique

1. Lire `AGENTS.md`, puis le contrat du palier actif et les preuves disponibles.
2. Pour `projects/`, utiliser les critères de `docs/parcours/<langage>.md` et les tests de l’apprenant.
   Pour `languages/`, utiliser `SPEC.md` et la conformance tasklite. Identifier le dossier et la
   commande exacte avant de lancer. Une commande indisponible est une limite, pas un succès.
3. Vérifier le cas visé, puis examiner le point le plus important : contrat, modèle, erreurs,
   durée de vie des ressources ou concurrence selon ce palier.
4. Indiquer le résultat observé et poser UNE question localisée dans le code, sans correction.
   Attendre la réponse avant toute autre remarque. Un bug peut être décrit par son symptôme.
5. Après l’explication, demander une petite variante permettant de vérifier la compréhension.
   Appliquer les critères F/C/A de `docs/methode.md` ; un test passant ne suffit pas pour C ou A.

Ne pas éditer l’implémentation ni fournir un extrait correctif. Juger les constructions dans leur
contexte : un clone, un cast ou un verrou ne prouve pas à lui seul un mauvais modèle.
