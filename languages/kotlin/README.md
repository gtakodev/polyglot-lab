# Kotlin

```bash
mvn -q compile
mvn -q exec:java -Dexec.mainClass=lab.tasklite.MainKt -- run ../../fixtures/tasks.json --json
```

Conformance (depuis ce dossier) :

```bash
mvn -q compile
python3 ../../conformance/run.py --cmd "java -cp target/classes lab.tasklite.MainKt"
```

Le squelette sort `3` (« pas implémenté »). Les dépendances (JSON, coroutines, tests) sont à
ajouter dans `pom.xml` quand le milestone en a besoin.

Docs du langage : `docs/kotlin.md`. Spec : `SPEC.md`.
