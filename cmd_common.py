

package cmd_common

import (
	"errors"
	"fmt"
	"os"
	"path/filepath"
)

func GetTestEnvironmentPath() (string, error) {
	currentDir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	return filepath.Join(currentDir, "test_environment"), nil
}

func CreateTestEnvironmentDirIfNotExists() error {
	testEnvironmentPath, err := GetTestEnvironmentPath()
	if err != nil {
		return err
	}
	if _, err := os.Stat(testEnvironmentPath); os.IsNotExist(err) {
		err := os.Mkdir(testEnvironmentPath, 0755)
		if err != nil {
			return err
		}
	}
	return nil
}

func GetTestEnvironmentConfigPath() (string, error) {
	testEnvironmentPath, err := GetTestEnvironmentPath()
	if err != nil {
		return "", err
	}
	return filepath.Join(testEnvironmentPath, "config.json"), nil
}

func GetTestEnvironmentResultsPath() (string, error) {
	testEnvironmentPath, err := GetTestEnvironmentPath()
	if err != nil {
		return "", err
	}
	return filepath.Join(testEnvironmentPath, "results"), nil
}

func CreateTestEnvironmentResultsDirIfNotExists() error {
	testEnvironmentResultsPath, err := GetTestEnvironmentResultsPath()
	if err != nil {
		return err
	}
	if _, err := os.Stat(testEnvironmentResultsPath); os.IsNotExist(err) {
		err := os.Mkdir(testEnvironmentResultsPath, 0755)
		if err != nil {
			return err
		}
	}
	return nil
}

func ValidateDirectoryPermissions(path string) error {
	testEnvironmentPath, err := GetTestEnvironmentPath()
	if err != nil {
		return err
	}
	testEnvironmentResultsPath, err := GetTestEnvironmentResultsPath()
	if err != nil {
		return err
	}
	if _, err := os.Stat(testEnvironmentPath); err != nil {
		return err
	}
	if _, err := os.Stat(testEnvironmentResultsPath); err != nil {
		return err
	}
	return nil
}