# Apprendre à se débrouiller

## Une boucle courte

1. **Question.** Décris le comportement voulu et une chose que tu ne sais pas encore.
2. **Recherche.** Pars du portail officiel du parcours. Trouve la section pertinente. Note
   l'URL, la version concernée et la garantie utile avec tes mots.
3. **Prédiction.** Écris le résultat attendu pour un cas normal et un cas qui peut échouer.
4. **Expérience.** Écris un programme minuscule dans `experiments/<langage>/`. Fais varier
   une seule condition et compare l'observation avec ta prédiction.
5. **Application.** Intègre le concept au projet et écris des tests de comportement.
6. **Explication.** Documentation fermée, explique ton choix et une limite. Rouvre ensuite
   la source pour vérifier ce que tu avais mal retenu.
7. **Transfert.** Lors d'une autre session, traite une variante sans indice de l'agent.
   La documentation reste autorisée : l'autonomie n'est pas la mémorisation des API.

Une URL seule ne prouve rien. Relie question, passage trouvé, prédiction, observation et décision.
Change l'exemple d'un tutoriel avant de l'utiliser et explique ce qui doit rester vrai.
Pour une garantie trouvée dans un article, remonte à la référence officielle.

## Chercher sans errer

Essaie pendant environ 10 à 15 minutes. Note tes mots-clés et ce qui manque. Ce délai est un
repère pour demander une piste, pas un examen chronométré. Pour une API, cherche sa signature,
ses erreurs et sa durée de vie ; pour une notion, une définition et un contre-exemple.
Vérifie la version utilisée et distingue expérimental, preview et stable.

| Aide | Agent | Apprenant |
|---|---|---|
| 0 | Demande la question, la tentative et l'observation | Décrit précisément le manque |
| 1 | Donne un mot-clé ou une question plus petite | Trouve la section pertinente |
| 2 | Indique une section officielle sans sa conclusion | Lit, reformule et prédit |
| 3 | Explique avec un petit exemple hors projet | Conçoit l'expérience et l'application |

On monte d'un niveau après une tentative. L'agent peut corriger directement une idée fausse,
puis poser une nouvelle question. Une question à la fois, sans interrogatoire interminable.

## Valider un palier

Chaque palier P0–P4 a trois états indépendants dans `PROGRESS.md` :

- **F — fonctionne** : critères exécutés, commandes, sorties et codes de sortie conservés.
- **C — compris** : source retrouvée, prédiction confrontée au résultat, choix et limite expliqués.
- **A — autonome** : variante réalisée lors d'une autre session sans indice de l'agent,
  avec documentation autorisée. Après une aide, réessaie une autre variante plus tard.

Passe au palier suivant après F et C ; A peut être vérifié ultérieurement. Si un blocage persiste,
note-le et choisis une expérience indépendante. Le tableau n'est pas une note scolaire.
Un échec attendu doit être expliqué : toute commande qui échoue n'est pas une preuve.

## Contrat avant le code

Les fiches donnent le périmètre et les cas à vérifier. Avant chaque palier, consigne les entrées,
sorties, erreurs et décisions ouvertes (format, ordre, politique d'échec). Fixe ces choix avant
les tests. Note explicitement toute évolution du contrat.
Les tests des nouveaux projets sont à écrire ; `conformance/` est exclusivement pour tasklite.
Pour les mesures, note machine, données et répétitions : changer de technique ne prouve pas un gain.

## Fin et reprise

Utilise `journal/<langage>.md` et `evidence/<langage>/<date>-<palier>/`. Conserve la commande,
le dossier, les versions, le code de sortie et la révision Git ou les modifications concernées.
Ne conserve aucun secret. Termine par la prochaine expérience précise.
À la reprise, commence par prédire ce qu'elle produira.

Les extensions sont un menu : choisis-en une, définis un comportement observable et un critère
de sortie, puis reprends cette boucle. Un petit projet peut porter une étude profonde.
