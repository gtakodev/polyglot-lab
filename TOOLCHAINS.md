# Environnement de travail

## Avant un nouveau parcours

Choisis un seul langage. Vérifie l’exécutable réellement utilisé, sa version, la compilation d’un
programme minimal et l’exécution d’un test. Note les résultats dans le journal. L’existence d’une
commande dans le PATH ne prouve ni la présence d’un compilateur ni le bon fonctionnement du build.
Pour Java, vérifier `javac` autant que `java`. Choisis ensuite les versions du build et des bibliothèques
compatibles en consultant leur documentation officielle.

Sur cette machine Windows, le relevé du 7 novembre 2026 a trouvé Java via un chemin de JRE,
Rust/Cargo, Node/npm et Python dans le PATH ; Maven, Kotlin, Go et `sh` n’y ont pas été trouvés.
WSL est détecté, mais aucune distribution ni toolchain WSL n’a été vérifiée. Ce relevé n’est pas
une validation de build. Les nouveaux parcours n’imposent pas un shell POSIX ; tasklite l’impose
via `SPEC.md`. Choisir et vérifier un environnement POSIX avant de lancer ce kata.

## Ancien environnement Linux — archive non validée sur ce poste

Les versions et commandes ci-dessous décrivent l’environnement initial. Elles ne sont ni des
versions recommandées ni une preuve d’installation locale. Les affirmations de vérification
s’appliquent uniquement à cet ancien environnement.


Versions installées et **vérifiées** (dernier contrôle : octobre 2026). Toutes sont sur le
`PATH` des sessions de travail ; rien à installer pour commencer à coder.

| Langage | Outil | Version | Emplacement |
|---|---|---|---|
| Java | Temurin JDK | **25.0.4.1** (LTS) | `/opt/data/.local/jdk` |
| Java | Maven | **3.9.16** | `/opt/data/.local/maven` |
| Kotlin | kotlinc (JVM) | **2.4.21** | `/opt/data/.local/kotlinc` |
| Go | go | **1.27.2** | `/opt/data/.local/go` |
| Rust | rustc / cargo | **1.99.1** (édition 2024) | `/opt/data/.local/cargo` |
| TypeScript | Node.js | **26.7.0** | `/usr/local/bin/node` |
| TypeScript | TypeScript | **7.0.2** | `node_modules` du projet |
| — | Python (runner de conformance) | **3.x** | `/usr/local/bin/python3` |

Java 25 est la dernière LTS (prochaine : Java 29, septembre 2027). Aucune feature preview
n'est activée : `StructuredTaskScope` reste hors d'atteinte sans `--enable-preview`, et c'est
volontaire.

## Commandes vérifiées

Chaque squelette compile et sort `3` (« pas implémenté ») ; la conformance tourne sur les cinq
et échoue proprement.

| Langage | Construire | Lancer | Conformance (depuis `languages/<lang>`) |
|---|---|---|---|
| Java | `mvn -q package` | `java -jar target/tasklite.jar` | `python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar"` |
| Kotlin | `mvn -q package` | `java -jar target/tasklite.jar` | `python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar"` |
| Go | `go build -o tasklite .` | `./tasklite` | `python3 ../../conformance/run.py --cmd "./tasklite"` |
| Rust | `cargo build` | `./target/debug/tasklite` | `python3 ../../conformance/run.py --cmd "./target/debug/tasklite"` |
| TypeScript | `npm install && npm run build` | `node dist/main.js` | `python3 ../../conformance/run.py --cmd "node dist/main.js"` |

Java et Kotlin produisent un **jar exécutable** (`maven-shade-plugin`) : quand tu ajouteras
Jackson ou `kotlinx-serialization`, la commande de conformance ne changera pas — c'est la raison
d'être de ce choix.

## Ajouter une dépendance

- Java / Kotlin : dans `pom.xml`, puis `mvn -q package` — le jar embarque la dépendance.
- Go : `go get <module>` puis `go mod tidy`.
- Rust : `cargo add <crate>`.
- TypeScript : `npm install <pkg>` puis `npm run build`.

## Ce que la conformance ne couvre pas

Les tests unitaires que tu écriras toi-même. La suite est un juge boîte noire : elle ne voit que
la CLI, les fichiers, le JSON et les codes de sortie.
