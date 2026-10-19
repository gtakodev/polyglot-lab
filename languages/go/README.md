# Go

```bash
go run . run ../../fixtures/tasks.json --json
go build -o tasklite .
go test ./...
```

Conformance (depuis ce dossier) :

```bash
go build -o tasklite .
python3 ../../conformance/run.py --cmd "./tasklite"
```

Le squelette sort `3` (« pas implémenté »). Aucune dépendance pour M0 : la stdlib suffit.

Docs du langage : `docs/go.md`. Spec : `SPEC.md`.
