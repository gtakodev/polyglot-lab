---
name: verify-tasklite
description: Piloter la CLI tasklite comme un utilisateur et produire des preuves (build, conformance, transcript) pour une implémentation de languages/. À utiliser avant de dire qu'un milestone est terminé.
---

# Vérifier tasklite

Cette skill existe pour une seule raison : **une implémentation n'est pas « finie » parce qu'elle
compile**. Elle est finie quand la CLI, lancée comme un utilisateur la lancerait, produit les
sorties de `SPEC.md` — et qu'il reste une trace de la preuve.

Elle s'applique aux cinq langages. L'agent qui la lit n'a jamais vu le code : tout doit être
explicite.

## 1. Launch — construire et lancer

Depuis `languages/<lang>/` :

| Langage | Build | Lancement |
|---|---|---|
| Java | `mvn -q compile` | `java -cp target/classes lab.tasklite.Main` |
| Kotlin | `mvn -q compile` | `java -cp target/classes lab.tasklite.MainKt` |
| Go | `go build -o tasklite .` | `./tasklite` |
| Rust | `cargo build` | `./target/debug/tasklite` |
| TypeScript | `npm install && npm run build` | `node dist/main.js` |

Le binaire doit être **construit avant** la conformance : le runner exécute chaque cas dans un
répertoire temporaire, donc `go run .` ou `cargo run` n'y trouveraient pas le projet. Les chemins
relatifs de `--cmd` sont résolus depuis le dossier d'invocation.

« Prêt » ne veut pas dire « la commande existe » : elle doit répondre **avec la spec de test** :

```bash
<cmd> run ../../fixtures/tasks.json --json
```

Si cette commande sort `3`, l'implémentation n'a pas commencé : ne va pas plus loin, dis-le.

## 2. Doctor — est-ce que ça vaut le coup de tester ?

Une seule commande, en lecture seule :

```bash
python3 ../../conformance/run.py --cmd "<cmd>" --list   # les cas voient-ils bien l'implémentation ?
<cmd> run ../../fixtures/tasks.json --json | head -c 400
```

Vérifie trois choses : la commande existe, la sortie est **du JSON seul sur stdout**, et le code de
sortie correspond à ce que la spec attend pour cette fixture (`0`).

Si le JSON est mélangé à des logs, **arrête** : aucun cas ne pourra passer, et le vrai problème est
la séparation stdout/stderr.

## 3. Drive — la conformance, milestone par milestone

```bash
python3 conformance/run.py --cmd "<cmd>" --upto M0   # M0 d'abord, pas tout d'un coup
python3 conformance/run.py --cmd "<cmd>" --upto M3
```

Règles :

- Un échec se lit **dans l'ordre** : code de sortie → statut global → statuts de tâches → temps mural.
- Ne modifie jamais `conformance/` pour faire passer une implémentation. Si un cas te semble faux,
  c'est `SPEC.md` qu'on discute, pas la suite qu'on ajuste.
- `-v` pour voir stdout/stderr quand un cas échoue.
- Un cas de concurrence (`09`) peut être instable sur une machine chargée : relance-le une fois
  avant de conclure, et note le temps mesuré.

## 4. Evidence — ce qui prouve le résultat

Chaque vérification laisse une trace dans `evidence/<langage>/<AAAAMMJJ-HHMM>/` :

```
build.log            sortie de la commande de build (code de sortie inclus)
conformance.txt      sortie complète du runner (le résumé X/Y est la preuve)
fixture.txt          la sortie de `run ../../fixtures/tasks.json --json`
meta.txt             langage, milestone, commit, date, commande exacte
```

Règles de preuve :

- **Piloter la vraie CLI**, jamais un test unitaire ni un endpoint interne.
- Capturer **l'action et l'état résultant** : la commande lancée *et* le JSON produit.
- Vérifier les effets de bord quand la spec en promet (fichiers écrits par une tâche, compteur
  de retries) — pas seulement la sortie.
- Ne jamais coller dans le transcript un résultat fabriqué ou reconstitué de mémoire.

## 5. Cleanup

- Supprimer les répertoires temporaires créés par les cas (le runner le fait seul).
- Ne jamais tuer de processus « par nom » : tuer ce qu'on a lancé, par PID (ou groupe).
- Ne pas supprimer `evidence/` : c'est la preuve, elle survit au nettoyage.

## 6. Rapport final (le format attendu)

```
Langage : <x>   Milestone : <M0..M3>   Commit : <sha court>
Build : OK/FAIL (code <n>)
Conformance : <p>/<total> (--upto <Mx>)
Échecs : <cas> — <raison en une ligne>
Preuves : evidence/<langage>/<horodatage>/
Verdict : terminé / pas terminé (et ce qui manque, en une phrase)
```

Sans ce bloc, la vérification n'a pas eu lieu.

---

Structure inspirée du `create-verification-skill` de Lauren Tan (poteto) : lancer, docteur,
piloter, preuves, nettoyage — appliquée ici à une CLI multi-langages.
