# Java

```bash
mvn -q compile
mvn -q exec:java -Dexec.mainClass=lab.tasklite.Main -- run ../../fixtures/tasks.json --json
```

Conformance (depuis ce dossier) :

```bash
mvn -q compile
python3 ../../conformance/run.py --cmd "java -cp target/classes lab.tasklite.Main"
```

Le squelette sort `3` (« pas implémenté ») : la conformance échouera tant que M0 n'est pas fait.
C'est normal, et c'est le point de départ.

Docs du langage : `docs/java.md`. Spec : `SPEC.md`.
