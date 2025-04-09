

package cmd_MOD

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func MODCommand() {
	// Define the MOD command functions
	modFunctions := map[string]func(){
		"create": createMOD,
		"update": updateMOD,
		"delete": deleteMOD,
	}

	// Get the command-line arguments
	args := os.Args[1:]

	// Check if the command is valid
	if len(args) < 1 {
		log.Fatal("Invalid command")
	}

	// Get the command
	command := args[0]

	// Check if the command is supported
	if _, ok := modFunctions[command]; !ok {
		log.Fatal("Unsupported command")
	}

	// Validate user input
		if len(args) < 2 {
			log.Fatal("Invalid number of arguments")
		}

		// Execute the command
		modFunctions[command]()
	}

	func createMOD() {
		// Create a new MOD file
		modFile := "mod.txt"

		// Check if the MOD file already exists
		if _, err := os.Stat(modFile); err == nil {
			log.Fatal("MOD file already exists")
		}

		file, err := os.Create(modFile)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		// Write the MOD file contents
		_, err = file.WriteString("MOD file created")
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println("MOD file created successfully")
	}

	func updateMOD() {
		// Update an existing MOD file
		modFile := "mod.txt"

		// Check if the MOD file exists
		if _, err := os.Stat(modFile); os.IsNotExist(err) {
			log.Fatal("MOD file does not exist")
		}

		file, err := os.OpenFile(modFile, os.O_RDWR, 0644)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		// Read the existing MOD file contents
		var contents string
		_, err = fmt.Fscanf(file, "%s", &contents)
		if err != nil {
			log.Fatal(err)
		}

		// Update the MOD file contents
		contents += "\nMOD file updated"

		// Write the updated MOD file contents
		_, err = file.WriteString(contents)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println("MOD file updated successfully")
	}

	func deleteMOD() {
		// Delete an existing MOD file
		modFile := "mod.txt"

		// Check if the MOD file exists
		if _, err := os.Stat(modFile); os.IsNotExist(err) {
			log.Fatal("MOD file does not exist")
		}

		err := os.Remove(modFile)
		if err != nil {
			log.Fatal(err)
		}

		// Check if the file was successfully deleted
		if _, err := os.Stat(modFile); err == nil {
			log.Fatal("Failed to delete MOD file")
		}

		fmt.Println("MOD file deleted successfully")
	}

	func main() {
		MODCommand()
	}