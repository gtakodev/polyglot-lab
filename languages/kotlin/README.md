# Kotlin

```bash
mvn -q package                                       # → target/tasklite.jar (stdlib incluse)
java -jar target/tasklite.jar run ../../fixtures/tasks.json --json
```

Conformance (depuis ce dossier) :

```bash
mvn -q package
python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar"
```

Le squelette sort `3` (« pas implémenté »). Les dépendances (JSON, coroutines, tests) sont à
ajouter dans `pom.xml` quand le milestone en a besoin.

Docs du langage : `docs/kotlin.md`. Spec : `SPEC.md`.
