# TypeScript (Node)

## Ce que ce projet va te faire travailler

- **Types à l'exécution** : un `interface` ne valide rien. Ton JSON arrive tel quel ; il faut un
  schéma runtime (zod) et une union discriminée pour le statut.
- **Unions discriminées** : `type TaskStatus = { kind: "success" } | { kind: "failed"; exitCode: number } | …`
  puis `switch` avec `never` pour l'exhaustivité.
- **Concurrence** : boucle d'événements, `Promise.all` borné (pool maison ou `p-limit`),
  `AbortController` pour les timeouts, `child_process.spawn` (pas `exec` : pas de buffer).
- **Erreurs** : pas de types d'erreur en TS ; il faut les modéliser soi-même ou utiliser des
  retours `Result` explicites (c'est un choix de conception, pas une obligation).
- **Tests** : Vitest, `tmpdir` + `fs.mkdtemp`, tests de CLI via `execa`.

## Bibliothèques utiles

| Besoin | Choix raisonnable |
|---|---|
| Validation | `zod` (schéma = type dérivé) |
| CLI | `commander`, ou `node:util.parseArgs` (stdlib) |
| Processus | `node:child_process` (`spawn`) ou `execa` |
| Tests | `vitest` |
| Exécution TS | `tsx` en dev, `tsc` pour le build |

## Commandes

```bash
npm install
npm run dev -- run ../../fixtures/tasks.json --json
npm test
npm run build && node dist/main.js run ../../fixtures/tasks.json
```

Conformance :

```bash
python3 conformance/run.py --cmd "npx tsx src/main.ts"
```

## Pièges classiques

1. **`any` et `as`** : chaque `as` est une promesse non vérifiée. Si tu en as besoin pour lire le
   JSON, c'est que la validation manque.
2. **`Promise.all` n'est pas une limite de concurrence** : il lance tout. Pour `--workers N`,
   il faut une file et N workers, ou `p-limit`.
3. **`exec` bufferise** : `exec` accumule la sortie en mémoire et a une limite par défaut.
   `spawn` + streams est le bon outil.
4. **Tuer un enfant** : `child.kill()` ne tue pas le groupe (`sh -c`). Il faut `detached: true`
   puis `process.kill(-child.pid)`.
5. **`setTimeout` non annulé** : fuite de timer et exécution après la fin logique. `clearTimeout`
   dans un `finally`.
6. **Les types disparaissent** : ton `switch` exhaustif sur une union ne protège que si la donnée
   a été validée à l'entrée. Sinon, tu types des mensonges.

## Docs officielles

- TypeScript : https://www.typescriptlang.org/docs/
- Narrowing / unions discriminées : https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- Node `child_process` : https://nodejs.org/api/child_process.html
- Node `util.parseArgs` : https://nodejs.org/api/util.html#utilparseargsconfig
- Zod : https://zod.dev/
- Vitest : https://vitest.dev/guide/
