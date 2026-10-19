---
name: grill-me
description: Interroger sans relâche un plan, une conception ou une compréhension jusqu'à l'accord explicite. À utiliser quand Guillaume veut être challengé avant de coder, ou dit « grill me ».
---

# Grill me

Interroge-moi sans relâche sur **tous** les aspects de ce plan, jusqu'à ce que nous partagions
la même compréhension. Descends chaque branche de l'arbre de décision, en résolvant les
dépendances entre décisions une par une.

Pour chaque question, **donne ta réponse recommandée** — c'est ce qui me force à argumenter
contre toi plutôt qu'à répondre « oui ».

Pose les questions **une à la fois**. Attends ma réponse avant la suivante.

Si une question peut être tranchée en explorant le repo (`SPEC.md`, `conformance/cases/`,
`docs/`), explore le repo au lieu de me la poser.

## Usage dans ce repo

Quand je démarre un langage, commence par la question la plus structurante, pas la plus facile :

1. Comment je représente les quatre statuts, et où le compilateur m'oblige à traiter les quatre ?
2. Qui possède le graphe de tâches pendant l'exécution ?
3. Comment une tâche apprend qu'elle doit s'arrêter ?
4. Qu'est-ce qui se passe si deux tâches indépendantes écrivent au même endroit ?
5. Qu'est-ce que je vais regretter dans mon architecture au milestone suivant ?

Ne pose jamais deux questions dans le même message. Ne donne pas la réponse sous forme de code.
Tu peux donner un avis en une phrase, puis laisser la décision.

Tu t'arrêtes quand **je** dis que c'est clair, pas quand tu as épuisé tes questions.

---

Adapté du skill `grill-me` de Matt Pocock (github.com/mattpocock/skills), réduit à son os.
