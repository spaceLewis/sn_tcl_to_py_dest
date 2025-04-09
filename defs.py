

package defs

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

const (
	// TestEnvironmentDir is the directory where test environment files are stored
	TestEnvironmentDir = "test-environment"
	// TestEnvironmentFile is the file where test environment settings are stored
	TestEnvironmentFile = "test-environment.json"
)

// GetTestEnvironmentDir returns the path to the test environment directory
func GetTestEnvironmentDir() (string, error) {
	wd, err := os.Getwd()
	if err != nil {
		return "", err
	}
	return filepath.Join(wd, TestEnvironmentDir), nil
}

// GetTestEnvironmentFile returns the path to the test environment file
func GetTestEnvironmentFile() (string, error) {
	dir, err := GetTestEnvironmentDir()
	if err != nil {
		return "", err
	}
	return filepath.Join(dir, TestEnvironmentFile), nil
}

// ValidateTestEnvironment checks if the test environment directory and file exist
func ValidateTestEnvironment() error {
	dir, err := GetTestEnvironmentDir()
	if err != nil {
		return err
	}
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		return errors.New("test environment directory does not exist")
	}
	file, err := GetTestEnvironmentFile()
	if err != nil {
		return err
	}
	if _, err := os.Stat(file); os.IsNotExist(err) {
		return errors.New("test environment file does not exist")
	}
	return nil
}

// InitTestEnvironment initializes the test environment directory and file
func InitTestEnvironment() error {
	dir, err := GetTestEnvironmentDir()
	if err != nil {
		return err
	}
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		if err := os.MkdirAll(dir, 0755); err != nil {
			return err
		}
	}
	file, err := GetTestEnvironmentFile()
	if err != nil {
		return err
	}
	if _, err := os.Stat(file); os.IsNotExist(err) {
		if _, err := os.Create(file); err != nil {
			return err
		}
	}
	return nil
}

func main() {
	if err := ValidateTestEnvironment(); err != nil {
		log.Fatal(err)
	}
	if err := InitTestEnvironment(); err != nil {
		log.Fatal(err)
	}
}