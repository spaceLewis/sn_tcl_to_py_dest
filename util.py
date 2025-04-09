

package util

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"
)

type TestSuiteConfig struct {
	Name        string `json:"name"`
	Description string `json:"description"`
}

func GetTestEnvironment() string {
	return os.Getenv("TEST_ENVIRONMENT")
}

func GetTestConfigPath() string {
	return filepath.Join(GetTestEnvironment(), "config")
}

func GetTestConfigFile(name string) string {
	return filepath.Join(GetTestConfigPath(), name)
}

func GetTestOutputPath() string {
	return filepath.Join(GetTestEnvironment(), "output")
}

func GetTestOutputFile(name string) string {
	return filepath.Join(GetTestOutputPath(), name)
}

func GetTestLogPath() string {
	return filepath.Join(GetTestEnvironment(), "logs")
}

func GetTestLogFile(name string) string {
	return filepath.Join(GetTestLogPath(), name)
}

func GetTestTempPath() string {
	return filepath.Join(GetTestEnvironment(), "temp")
}

func GetTestTempFile(name string) string {
	return filepath.Join(GetTestTempPath(), name)
}

func GetTestResourcePath() string {
	return filepath.Join(GetTestEnvironment(), "resources")
}

func GetTestResourceFile(name string) string {
	return filepath.Join(GetTestResourcePath(), name)
}

func GetTestReportPath() string {
	return filepath.Join(GetTestEnvironment(), "reports")
}

func GetTestReportFile(name string) string {
	return filepath.Join(GetTestReportPath(), name)
}

func GetTestScreenshotPath() string {
	return filepath.Join(GetTestEnvironment(), "screenshots")
}

func GetTestScreenshotFile(name string) string {
	return filepath.Join(GetTestScreenshotPath(), name)
}

func GetTestVideoPath() string {
	return filepath.Join(GetTestEnvironment(), "videos")
}

func GetTestVideoFile(name string) string {
	return filepath.Join(GetTestVideoPath(), name)
}

func GetTestDataPath() string {
	return filepath.Join(GetTestEnvironment(), "data")
}

func GetTestDataFile(name string) string {
	return filepath.Join(GetTestDataPath(), name)
}

func GetTestScriptPath() string {
	return filepath.Join(GetTestEnvironment(), "scripts")
}

func GetTestScriptFile(name string) string {
	return filepath.Join(GetTestScriptPath(), name)
}

func GetTestSuitePath() string {
	return filepath.Join(GetTestEnvironment(), "suites")
}

func GetTestSuiteFile(name string) string {
	return filepath.Join(GetTestSuitePath(), name)
}

func GetTestSuiteConfigPath() string {
	return filepath.Join(GetTestSuitePath(), "config")
}

func GetTestSuiteConfigFile(name string) string {
	return filepath.Join(GetTestSuiteConfigPath(), name)
}

func GetTestSuiteOutputPath() string {
	return filepath.Join(GetTestSuitePath(), "output")
}

func GetTestSuiteOutputFile(name string) string {
	return filepath.Join(GetTestSuiteOutputPath(), name)
}

func GetTestSuiteLogPath() string {
	return filepath.Join(GetTestSuitePath(), "logs")
}

func GetTestSuiteLogFile(name string) string {
	return filepath.Join(GetTestSuiteLogPath(), name)
}

func GetTestSuiteTempPath() string {
	return filepath.Join(GetTestSuitePath(), "temp")
}

func GetTestSuiteTempFile(name string) string {
	return filepath.Join(GetTestSuiteTempPath(), name)
}

func GetTestSuiteResourcePath() string {
	return filepath.Join(GetTestSuitePath(), "resources")
}

func GetTestSuiteResourceFile(name string) string {
	return filepath.Join(GetTestSuiteResourcePath(), name)
}

func GetTestSuiteReportPath() string {
	return filepath.Join(GetTestSuitePath(), "reports")
}

func GetTestSuiteReportFile(name string) string {
	return filepath.Join(GetTestSuiteReportPath(), name)
}

func GetTestSuiteScreenshotPath() string {
	return filepath.Join(GetTestSuitePath(), "screenshots")
}

func GetTestSuiteScreenshotFile(name string) string {
	return filepath.Join(GetTestSuiteScreenshotPath(), name)
}

func GetTestSuiteVideoPath() string {
	return filepath.Join(GetTestSuitePath(), "videos")
}

func GetTestSuiteVideoFile(name string) string {
	return filepath.Join(GetTestSuiteVideoPath(), name)
}

func GetTestSuiteDataPath() string {
	return filepath.Join(GetTestSuitePath(), "data")
}

func GetTestSuiteDataFile(name string) string {
	return filepath.Join(GetTestSuiteDataPath(), name)
}

func GetTestSuiteScriptPath() string {
	return filepath.Join(GetTestSuitePath(), "scripts")
}

func GetTestSuiteScriptFile(name string) string {
	return filepath.Join(GetTestSuiteScriptPath(), name)
}

func GetTestSuiteConfig() (TestSuiteConfig, error) {
	var config TestSuiteConfig
	data, err := os.ReadFile(GetTestSuiteConfigFile("config.json"))
	if err != nil {
		return config, err
	}
	err = json.Unmarshal(data, &config)
	if err != nil {
		return config, err
	}
	return config, nil
}

func GetTestSuiteOutput() (string, error) {
	data, err := os.ReadFile(GetTestSuiteOutputFile("output.json"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteLog() (string, error) {
	data, err := os.ReadFile(GetTestSuiteLogFile("log.txt"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteTemp() (string, error) {
	data, err := os.ReadFile(GetTestSuiteTempFile("temp.txt"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteResource() (string, error) {
	data, err := os.ReadFile(GetTestSuiteResourceFile("resource.txt"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteReport() (string, error) {
	data, err := os.ReadFile(GetTestSuiteReportFile("report.txt"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteScreenshot() (string, error) {
	data, err := os.ReadFile(GetTestSuiteScreenshotFile("screenshot.png"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteVideo() (string, error) {
	data, err := os.ReadFile(GetTestSuiteVideoFile("video.mp4"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteData() (string, error) {
	data, err := os.ReadFile(GetTestSuiteDataFile("data.txt"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func GetTestSuiteScript() (string, error) {
	data, err := os.ReadFile(GetTestSuiteScriptFile("script.sh"))
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func ReadFile(path string) (string, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func WriteFile(path string, content string) error {
	return os.WriteFile(path, []byte(content), 0644)
}

func AppendFile(path string, content string) error {
	f, err := os.OpenFile(path, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = f.WriteString(content)
	if err != nil {
		return err
	}
	return nil
}

func DeleteFile(path string) error {
	return os.Remove(path)
}

func FileExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}

func DirExists(path string) bool {
	fi, err := os.Stat(path)
	if err != nil {
		return false
	}
	return fi.IsDir()
}

func CreateDir(path string) error {
	return os.MkdirAll(path, 0755)
}

func DeleteDir(path string) error {
	return os.RemoveAll(path)
}

func CopyFile(src string, dst string) error {
	srcFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer srcFile.Close()

	dstFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer dstFile.Close()

	_, err = io.Copy(dstFile, srcFile)
	if err != nil {
		return err
	}
	return nil
}

func CopyDir(src string, dst string) error {
	srcInfo, err := os.Stat(src)
	if err != nil {
		return err
	}

	if !srcInfo.IsDir() {
		return fmt.Errorf("source is not a directory")
	}

	dstInfo, err := os.Stat(dst)
	if err != nil {
		if os.IsNotExist(err) {
			err = os.MkdirAll(dst, 0755)
			if err != nil {
				return err
			}
		} else {
			return err
		}
	}

	if dstInfo.IsDir() {
		err = filepath.Walk(src, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			srcPath := path
			relPath, err := filepath.Rel(src, srcPath)
			if err != nil {
				return err
			}

			dstPath := filepath.Join(dst, relPath)

			if info.IsDir() {
				err = os.MkdirAll(dstPath, 0755)
				if err != nil {
					return err
				}
			} else {
				err = CopyFile(srcPath, dstPath)
				if err != nil {
					return err
				}
			}

			return nil
		})
		if err != nil {
			return err
		}
	}
	return nil
}

func MoveFile(src string, dst string) error {
	return os.Rename(src, dst)
}

func MoveDir(src string, dst string) error {
	return os.Rename(src, dst)
}

func GetFileInfo(path string) (os.FileInfo, error) {
	return os.Stat(path)
}

func GetFileSize(path string) (int64, error) {
	info, err := GetFileInfo(path)
	if err != nil {
		return 0, err
	}
	return info.Size(), nil
}

func GetFileMode(path string) (os.FileMode, error) {
	info, err := GetFileInfo(path)
	if err != nil {
		return 0, err
	}
	return info.Mode(), nil
}

func GetFileModTime(path string) (time.Time, error) {
	info, err := GetFileInfo(path)
	if err != nil {
		return time.Time{}, err
	}
	return info.ModTime(), nil
}

func GetFileOwner(path string) (string, error) {
	info, err := GetFileInfo(path)
	if err != nil {
		return "", err
	}
	return info.Sys().(*syscall.Stat_t).Uid, nil
}

func GetFileGroup(path string) (string, error) {
	info, err := GetFileInfo(path)
	if err != nil {
		return "", err
	}
	return info.Sys().(*syscall.Stat_t).Gid, nil
}

func GetDirInfo(path string) (os.FileInfo, error) {
	return os.Stat(path)
}

func GetDirSize(path string) (int64, error) {
	info, err := GetDirInfo(path)
	if err != nil {
		return 0, err
	}
	return info.Size(), nil
}

func GetDirMode(path string) (os.FileMode, error) {
	info, err := GetDirInfo(path)
	if err != nil {
		return 0, err
	}
	return info.Mode(), nil
}

func GetDirModTime(path string) (time.Time, error) {
	info, err := GetDirInfo(path)
	if err != nil {
		return time.Time{}, err
	}
	return info.ModTime(), nil
}

func GetDirOwner(path string) (string, error) {
	info, err := GetDirInfo(path)
	if err != nil {
		return "", err
	}
	return info.Sys().(*syscall.Stat_t).Uid, nil
}

func GetDirGroup(path string) (string, error) {
	info, err := GetDirInfo(path)
	if err != nil {
		return "", err
	}
	return info.Sys().(*syscall.Stat_t).Gid, nil
}

func GetDirFiles(path string) ([]string, error) {
	files, err := filepath.Glob(filepath.Join(path, "*"))
	if err != nil {
		return nil, err
	}
	return files, nil
}

func GetDirDirs(path string) ([]string, error) {
	dirs, err := filepath.Glob(filepath.Join(path, "*/"))
	if err != nil {
		return nil, err
	}
	return dirs, nil
}

func GetDirSubdirs(path string) ([]string, error) {
	dirs, err := filepath.Glob(filepath.Join(path, "*/"))
	if err != nil {
		return nil, err
	}
	return dirs, nil
}

func GetDirSubfiles(path string) ([]string, error) {
	files, err := filepath.Glob(filepath.Join(path, "*"))
	if err != nil {
		return nil, err
	}
	return files, nil
}

func GetDirSubdirsRecursive(path string) ([]string, error) {
	dirs := []string{}
	err := filepath.Walk(path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() {
			dirs = append(dirs, path)
		}

		return nil
	})
	if err != nil {
		return nil, err
	}
	return dirs, nil
}

func GetDirSubfilesRecursive(path string) ([]string, error) {
	files := []string{}
	err := filepath.Walk(path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			files = append(files, path)
		}

		return nil
	})
	if err != nil {
		return nil, err
	}
	return files, nil
}

func GetDirSubdirsRecursiveDepth(path string, depth int) ([]string, error) {
	dirs := []string{}
	err := filepath.Walk(path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() {
			relPath, err := filepath.Rel(path, info.Name())
			if err != nil {
				return err
			}

			parts := strings.Split(relPath, string(os.PathSeparator))
			if len(parts) <= depth {
				dirs = append(dirs, path)
			}
		}

		return nil
	})
	if err != nil {
		return nil, err
	}
	return dirs, nil
}

func GetDirSubfilesRecursiveDepth(path string, depth int) ([]string, error) {
	files := []string{}
	err := filepath.Walk(path, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.IsDir() {
			relPath, err := filepath.Rel(path, info.Name())
			if err != nil {
				return err
			}

			parts := strings.Split(relPath, string(os.PathSeparator))
			if len(parts) <= depth {
				files = append(files, path)
			}
		}

		return nil
	})
	if err != nil {
		return nil, err
	}
	return files, nil
}

func init() {
	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)
}