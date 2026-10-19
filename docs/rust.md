# Rust

## Ce que ce projet va te faire travailler

- **Types algébriques** : `enum` avec données (`TaskStatus::Failed { exit_code: i32 }`) et
  `match` exhaustif — la version la plus directe de ce que tu cherchais avec `sealed`.
- **Erreurs** : `Result<T, E>`, `?`, `thiserror` pour les erreurs de domaine, `anyhow` pour le
  contexte applicatif. Pas d'exception : chaque `?` est un chemin de sortie.
- **Propriété** : qui possède la spec ? qui possède le `JoinHandle` ? pourquoi un `&str` suffit ici.
- **Concurrence** : `std::thread::scope` (le plus simple et le plus sous-estimé), ou `tokio` si tu
  veux comparer avec les coroutines Kotlin. `Arc<Mutex<_>>` seulement quand c'est justifié.
- **Processus** : `std::process::Command`, `try_wait`, `kill`, et le problème du groupe de
  processus (pas de `setsid` dans la stdlib : il faut `libc` ou un wrapper).
- **Tests** : `#[test]`, `assert_eq!`, `tempfile`, `insta` pour les snapshots.

## Bibliothèques utiles

| Besoin | Choix raisonnable |
|---|---|
| JSON | `serde` + `serde_json` |
| CLI | `clap` (derive), ou parsing manuel pour M0 |
| Erreurs | `thiserror` (domaine), `anyhow` (binaire) |
| Concurrence | std `thread::scope` (recommandé), `crossbeam` si besoin, `tokio` pour comparer |
| Tests | std + `tempfile` |
| Process group | `libc` ou `nix` (si tu veux tuer l'arbre proprement) |

## Commandes

```bash
cargo build
cargo run -- run ../fixtures/tasks.json --json
cargo test
cargo clippy -- -D warnings
cargo fmt
```

Conformance :

```bash
python3 conformance/run.py --cmd "cargo run --quiet --"
```

## Pièges classiques

1. **`clone()` en réflexe** : ça compile, ça cache le problème. Avant chaque `clone`, demande-toi
   qui devrait posséder la valeur.
2. **`Arc<Mutex<Vec<T>>>` par défaut** : souvent remplaçable par un channel (`mpsc`) ou par un
   retour de `thread::scope`. Le partage de mémoire mutable est le dernier recours, pas le premier.
3. **`unwrap()` sur une entrée utilisateur** : c'est un `panic` déguisé en code court.
4. **Lifetime dans une structure** : si tu te bats, c'est souvent que la structure devrait
   posséder ses données (`String` au lieu de `&str`).
5. **Timeout** : tuer un enfant ne tue pas ses petits-enfants. `sh -c "sleep 10"` recrée le
   problème Go/Java ; `nix::sys::signal::killpg` ou `setsid` est la vraie réponse.
6. **`match` avec `_ =>`** : si tu écris un bras `_` sur ton enum de statut, tu perds l'exhaustivité
   qui fait la valeur du type. Supprime-le et laisse le compilateur te parler.

## Docs officielles

- The Rust Book : https://doc.rust-lang.org/book/
- Rust by Example : https://doc.rust-lang.org/rust-by-example/
- `std::process` : https://doc.rust-lang.org/std/process/
- `std::thread::scope` : https://doc.rust-lang.org/std/thread/fn.scope.html
- docs.rs (toutes les crates) : https://docs.rs/
- API guidelines : https://rust-lang.github.io/api-guidelines/
