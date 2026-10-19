package main

import (
	"fmt"
	"os"
)

// Rien n'est implémenté : ce fichier existe pour que le projet compile et que la
// conformance puisse tourner (et échouer proprement, avec le code 3).
// Commence par M0 dans SPEC.md : lire les arguments, lire le fichier, valider,
// sortir 2 avec le bon code d'erreur.
func main() {
	fmt.Fprintln(os.Stderr, "tasklite: not implemented yet — see SPEC.md (M0)")
	os.Exit(3)
}
