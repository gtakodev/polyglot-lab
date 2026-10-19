# TypeScript (Node)

```bash
npm install
npm run dev -- run ../../fixtures/tasks.json --json
npm run build && node dist/main.js run ../../fixtures/tasks.json --json
npm test
```

Conformance (depuis ce dossier) :

```bash
npm run build
python3 ../../conformance/run.py --cmd "node dist/main.js"
```

Le squelette sort `3` (« pas implémenté »). `strict` est activé dans `tsconfig.json` : si tu dois
écrire `as` ou `any` pour compiler, c'est le signe qu'il manque une validation ou une union.

Docs du langage : `docs/typescript.md`. Spec : `SPEC.md`.
