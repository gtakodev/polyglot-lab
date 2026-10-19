# Choisir son langage (et ce que chacun va te coûter)

Tu vas écrire **le même programme cinq fois**. Ce qui change n'est pas la difficulté du problème,
mais l'endroit où le langage te fait réfléchir et l'endroit où il te laisse tranquille.
Ce fichier sert à choisir l'ordre et à savoir ce que tu viens chercher à chaque étape.

## Java 25 — la référence

**Tu viens chercher :** la propreté. Tu connais déjà la syntaxe ; ici tu travailles la modélisation
(records, interfaces scellées, pattern matching), la concurrence structurée avec les threads
virtuels, et la gestion d'un `ProcessBuilder` correctement (flux, timeout, destruction de l'arbre).

**Ce qui va te coûter :** la verbosité de la sérialisation JSON sans framework, et le piège
classique du `Process.waitFor()` qui ignore les buffers et bloque quand le programme écrit beaucoup.

**Bonne boussole :** si ta solution Java ressemble à un cours de 2012 (getters/setters,
hiérarchie de classes abstraites), c'est l'occasion de la réécrire en 2026.

## Kotlin — la même JVM, une autre grammaire de pensée

**Tu viens chercher :** la différence entre « moins de code » et « plus d'expressivité ».
`sealed interface` + `when` exhaustif, `data class`, coroutines et annulation coopérative.

**Ce qui va te coûter :** les coroutines ne sont pas des threads — comprendre `suspend`,
`coroutineScope`, la propagation d'annulation, et pourquoi un `runBlocking` au mauvais endroit
annule tout le bénéfice.

**Piège de portage :** ne copie pas ton Java « en plus court ». Demande-toi ce que l'exhaustivité
du `when` t'oblige à traiter que ton `switch` Java ne t'obligeait pas à traiter.

## Go — l'anti-abstraction

**Tu viens chercher :** la discipline. Peu de features, des choix explicites, des erreurs qui se
propagent à la main, des goroutines et des channels qui se voient dans le code.

**Ce qui va te coûter :** l'absence de types somme. Tu vas devoir modéliser un statut de tâche
sans `sealed class` — et découvrir que c'est là que se joue la vraie conception. Puis les
goroutines qui fuitent si personne ne ferme le channel, et le `context.Context` qu'on oublie
de propager.

**Bonne boussole :** si ton code Go ressemble à du Java avec des `interface{}`, tu es passé à côté.

## Rust — le prix de la correction

**Tu viens chercher :** la propriété, les types algébriques (`enum` avec données), le pattern
matching exhaustif, `Result`/`?`, et la différence entre « ça compile » et « c'est juste ».

**Ce qui va te coûter :** le borrow checker, si tu essaies de transposer une architecture à
références partagées. La première version sera probablement à base de `clone()` ; la deuxième,
à base de `Arc<Mutex<…>>` ; la troisième, la bonne, ne fera ni l'un ni l'autre.

**Piège de portage :** un `Arc<Mutex<T>>` posé par défaut est un aveu que tu n'as pas encore
compris qui possède quoi.

## TypeScript — les types qui s'effacent

**Tu viens chercher :** les unions discriminées, les génériques, et la frontière entre le type
statique et la validation runtime (les types disparaissent à l'exécution : ton JSON arrive non
validé, quoi que dise ton `interface`).

**Ce qui va te coûter :** la tentation du `any`, et la gestion de la concurrence sur une boucle
d'événements mono-thread — `Promise.all` n'est pas du parallélisme CPU, et un `exec` de processus
n'est pas une tâche annulable sans `AbortController`.

**Bonne boussole :** si tu écris `as` pour faire taire le compilateur, tu as un bug de conception,
pas un bug de typage.

## Suggestions d'ordre

- **Apprentissage maximal** : Java → Kotlin → Go → Rust → TypeScript.
- **Frustration minimale** : TypeScript → Java → Kotlin → Go → Rust.
- **Si tu as peu de temps** : Java → Go → Rust. C'est là que les trois modèles de pensée
  (objets, simplicité, propriété) se contrastent le plus.

Dans tous les cas : **un langage à la fois jusqu'à M3**, puis journal, puis suivant.
