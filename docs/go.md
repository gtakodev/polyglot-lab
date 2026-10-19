# Go

## Ce que ce projet va te faire travailler

- **Modélisation sans types somme** : un statut de tâche en Go, c'est un `string` typé ou une
  interface — et c'est là que tu apprends ce que `sealed` t'apportait.
- **Erreurs** : `error`, `fmt.Errorf("...: %w", err)`, `errors.Is/As`. Pas d'exception : chaque
  chemin d'échec est visible.
- **Concurrence** : goroutines + channels, `sync.WaitGroup`, `errgroup` (`golang.org/x/sync`),
  `context.WithTimeout` et annulation propagée.
- **Processus** : `exec.CommandContext`, `cmd.WaitDelay`, lecture des pipes, `Setpgid` pour tuer
  le groupe.
- **Tests** : tests tabulaires, `t.TempDir()`, `go test -race`.

## Bibliothèques utiles

| Besoin | Choix raisonnable |
|---|---|
| CLI | `flag` de la stdlib (recommandé pour M0), cobra si tu veux |
| Concurrence | `golang.org/x/sync/errgroup` |
| Tests | stdlib `testing` |
| JSON | `encoding/json` |

## Commandes

```bash
go build -o tasklite .
go run . run ../fixtures/tasks.json --json
go test ./...
go vet ./...
go test -race ./...
```

Conformance :

```bash
python3 conformance/run.py --cmd "go run ."
```

## Pièges classiques

1. **Goroutine qui fuit** : personne ne lit le channel, ou personne ne le ferme. `errgroup` +
   `ctx` règlent 90 % des cas.
2. **`exec.CommandContext` ne tue que le processus direct** : `sh -c "sleep 10"` laisse un
   `sleep` orphelin. Il faut `SysProcAttr{Setpgid: true}` puis tuer `-pid`.
3. **`cmd.Wait()` avant d'avoir lu les pipes** : même deadlock qu'en Java.
4. **`time.After` dans une boucle** : fuite de timers. `time.NewTimer` + `Stop`.
5. **Variables de boucle** : avant Go 1.22, la variable était partagée entre itérations.
   Tu es en 1.22+ probablement, mais sache pourquoi c'était un piège historique.
6. **`panic` pour une erreur attendue** : en Go, `panic` n'est pas un `throw`. Si la spec dit
   « sortie 2 », c'est un `error` remonté et un `os.Exit(2)`, pas un panic.

## Docs officielles

- Documentation Go : https://go.dev/doc/
- Tour de Go : https://go.dev/tour/
- `os/exec` : https://pkg.go.dev/os/exec
- `context` : https://pkg.go.dev/context
- `errgroup` : https://pkg.go.dev/golang.org/x/sync/errgroup
- Effective Go : https://go.dev/doc/effective_go
