# Matrice de comparaison

Remplis cette matrice **au fur et à mesure**, pas à la fin. Les cellules vides sont des questions,
pas des trous à combler avec du texte généré : chaque case que tu remplis doit venir d'une chose
que tu as réellement écrite et ressentie.

## Faits (vérifiables, à maintenir)

| | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Build | `mvn package` | `mvn package` | `go build` | `cargo build` | `npm run build` |
| Dépendances | `pom.xml` | `pom.xml` | `go.mod` | `Cargo.toml` | `package.json` |
| Tests | `mvn test` | `mvn test` | `go test ./...` | `cargo test` | `npm test` |
| Lint/format | (à toi de choisir) | (à toi de choisir) | `go vet` | `clippy` + `fmt` | (à toi de choisir) |
| Binaire | JVM | JVM | natif | natif | Node |
| Démarrage à froid | ? | ? | ? | ? | ? |

## Conception

| Question | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Comment représenter un statut à 4 cas ? | | | | | |
| Où l'exhaustivité est-elle garantie par le compilateur ? | | | | | |
| Combien de fichiers pour le même domaine ? | | | | | |
| Qu'est-ce qui est vérifié à la compilation, et qu'est-ce qui ne l'est pas ? | | | | | |

## Erreurs

| Question | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Comment une erreur de validation remonte-t-elle jusqu'à la sortie 2 ? | | | | | |
| Que se passe-t-il si j'oublie un cas d'erreur ? | | | | | |
| Combien de lignes de « plomberie » pour propager une erreur ? | | | | | |

## Concurrence

| Question | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Mécanisme utilisé pour `--workers N` | | | | | |
| Comment une tâche est-elle annulée ? | | | | | |
| Que se passe-t-il si une tâche lève/panic/throw ? | | | | | |
| Comment détecter une fuite (goroutine, coroutine, thread) ? | | | | | |

## Processus

| Question | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Comment éviter le deadlock des buffers ? | | | | | |
| Comment tuer l'arbre de processus au timeout ? | | | | | |
| Comment récupérer le code de sortie ? | | | | | |

## DX (à chaud, pas à froid)

| Question | Java | Kotlin | Go | Rust | TypeScript |
|---|---|---|---|---|---|
| Temps entre « je code » et « je vois le résultat » | | | | | |
| Qualité des messages du compilateur | | | | | |
| Douleur de l'outillage (build, format, debug) | | | | | |
| Ce qui m'a manqué de mon langage principal | | | | | |
| Ce que je voudrais garder dans mon langage principal | | | | | |

## Verdict personnel (une phrase par langage)

- Java :
- Kotlin :
- Go :
- Rust :
- TypeScript :
