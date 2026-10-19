# Java

```bash
mvn -q package                                       # → target/tasklite.jar
java -jar target/tasklite.jar run ../../fixtures/tasks.json --json
```

Conformance (depuis ce dossier) :

```bash
mvn -q package
python3 ../../conformance/run.py --cmd "java -jar target/tasklite.jar"
```

Le squelette sort `3` (« pas implémenté ») : la conformance échouera tant que M0 n'est pas fait.
C'est normal, et c'est le point de départ.

Docs du langage : `docs/java.md`. Spec : `SPEC.md`.
