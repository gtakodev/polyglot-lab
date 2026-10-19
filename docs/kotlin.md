# Kotlin

## Ce que ce projet va te faire travailler

- **Modélisation** : `sealed interface` + `when` exhaustif, `data class`, `value class` si tu veux
  typer les identifiants.
- **Concurrence** : `coroutineScope`, `async`/`await`, `Semaphore(n)` de `kotlinx.coroutines.sync`,
  annulation coopérative (`ensureActive`, `withTimeout`).
- **Nullabilité** : `String?` et le refus du `!!` — c'est le cœur de la DX Kotlin.
- **Processus** : `ProcessBuilder` (même API que Java), avec `destroyForcibly` + descendants.
- **JSON** : `kotlinx.serialization` (compile-time, pas de réflexion).
- **Tests** : `kotlin.test` + JUnit 5, `runTest` pour les coroutines.

## Bibliothèques utiles

| Besoin | Choix raisonnable |
|---|---|
| JSON | `kotlinx-serialization-json` |
| Coroutines | `kotlinx-coroutines-core` |
| CLI | Clikt, ou parsing manuel pour M0 |
| Tests | `kotlin-test-junit5` + `kotlinx-coroutines-test` |

## Commandes

```bash
mvn -q compile
mvn -q exec:java -Dexec.mainClass=lab.tasklite.MainKt -- run ../../fixtures/tasks.json
mvn -q test
```

Conformance :

```bash
python3 conformance/run.py --cmd "java -cp target/classes lab.tasklite.MainKt"
```

## Pièges classiques

1. **`runBlocking` au mauvais niveau** : il bloque le thread appelant et sérialise tout.
   Le point d'entrée peut l'utiliser une fois ; à l'intérieur, `coroutineScope`/`suspend`.
2. **Annulation ignorée** : une coroutine qui fait `Thread.sleep` ne s'annule pas.
   Il faut `delay` ou vérifier `isActive` / `ensureActive()`.
3. **`GlobalScope`** : la porte ouverte aux coroutines orphelines. `coroutineScope` borne la durée
   de vie ; c'est ce que tu veux pour un run.
4. **`!!`** : chaque `!!` est une exception qui attend son heure. Si le compilateur te force à en
   mettre un, c'est que ton modèle de données est incomplet.
5. **Sérialisation** : `@Serializable` sur les sealed hierarchies fonctionne, mais l'ordre des
   sous-classes et le polymorphisme demandent un `@SerialName` explicite.

## Docs officielles

- Kotlin : https://kotlinlang.org/docs/home.html
- Coroutines (guide) : https://kotlinlang.org/docs/coroutines-guide.html
- Annulation et timeouts : https://kotlinlang.org/docs/cancellation-and-timeouts.html
- `kotlinx.serialization` : https://kotlinlang.org/docs/serialization.html
- Sealed classes : https://kotlinlang.org/docs/sealed-classes.html
