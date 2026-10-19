# Rust

```bash
cargo run -- run ../../fixtures/tasks.json --json
cargo build --release
cargo test
cargo clippy -- -D warnings
```

Conformance (depuis ce dossier) :

```bash
cargo build
python3 ../../conformance/run.py --cmd "./target/debug/tasklite"
```

Le squelette sort `3` (« pas implémenté »). Aucune dépendance pour M0.

Docs du langage : `docs/rust.md`. Spec : `SPEC.md`.
