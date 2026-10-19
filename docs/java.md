# Java 25 (LTS)

## Ce que ce projet va te faire travailler

- **Modélisation** : `record` pour la spec, `sealed interface` pour le statut d'une tâche,
  `switch` avec pattern matching et exhaustivité.
- **Concurrence** : `Executors.newVirtualThreadPerTaskExecutor()`, `Semaphore` ou pool borné,
  propagation d'annulation (`Future.cancel`, interruption). `StructuredTaskScope` (JEP 505) est
  encore en **preview** en 25 : il exige `--enable-preview`, donc hors-jeu si tu veux du stable.
- **Processus** : `ProcessBuilder`, lecture concurrente de stdout/stderr (sinon deadlock),
  `Process.destroyForcibly()` et destruction des descendants.
- **JSON** : Jackson sans magie, ou `jakarta.json` si tu veux souffrir volontairement.
- **Tests** : JUnit 5, `@TempDir`, tests paramétrés.

## Bibliothèques utiles (à toi d'ajouter la dépendance)

| Besoin | Choix raisonnable |
|---|---|
| JSON | Jackson (`com.fasterxml.jackson.core:jackson-databind`) |
| CLI | picocli, ou `args` à la main (recommandé pour M0) |
| Tests | JUnit 5 (`org.junit.jupiter`) |
| Assertions fluides | AssertJ (optionnel) |

## Commandes

```bash
mvn -q package                                   # → target/tasklite.jar (jar exécutable, shade)
java -jar target/tasklite.jar run ../../fixtures/tasks.json --json
mvn -q test
```

La conformance attend une commande qui lance ton binaire, par exemple :

```bash
python3 conformance/run.py --cmd "java -jar target/tasklite.jar"
```

## Pièges classiques

1. **`waitFor()` sans vider les flux** : le processus fils bloque quand son buffer stdout est
   plein. Lis stdout/stderr dans des threads séparés (ou redirige vers `INHERIT`).
2. **`destroy()` ne tue pas les petits-enfants** : `sh -c "sleep 10"` lance un `sleep` enfant ;
   il faut `ProcessHandle.descendants()` puis `destroyForcibly()`.
3. **Threads virtuels et `synchronized`** : le pinning. Préfère `ReentrantLock` si tu bloques
   sur du code natif (rare ici, mais bon à savoir).
4. **Exceptions silencieuses dans les `ExecutorService`** : un `submit` sans `get()` avale
   l'exception. Utilise `invokeAll`/`Future.get` ou collecte explicitement.

## Docs officielles

- Java 25 API : https://docs.oracle.com/en/java/javase/25/docs/api/
- `dev.java` (tutoriels modernes) : https://dev.java/learn/
- Threads virtuels (JEP 444, final depuis 21) : https://openjdk.org/jeps/444
- Scoped Values (JEP 506, final en 25) : https://openjdk.org/jeps/506
- `ProcessBuilder` : https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ProcessBuilder.html
- Jackson : https://github.com/FasterXML/jackson-docs
