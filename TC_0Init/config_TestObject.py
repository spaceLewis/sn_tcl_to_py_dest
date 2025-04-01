

package config_TestObject

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

const (
	TEST_FILE_START = "Test file started"
	TEST_FILE_STOP  = "Test file stopped"
	DEVICE_INIT     = "Device initialized: %s"
	DEVICE_ERROR    = "Error initializing device: %s"
	CONFIG_FILE     = "config.json"
)

var devices = []string{"Device1", "Device2", "Device3"}

func tc_0init_atsinit() {
	fmt.Println("ATS initialization")
}

func tc_0init_testfile_start() {
	fmt.Println(TEST_FILE_START)
}

func tc_0init_testfile_stop() {
	fmt.Println(TEST_FILE_STOP)
}

func tc_0init_init_all_devices() {
	for _, device := range devices {
		init_act_device(device)
	}
}

func init_act_device(device string) {
	fmt.Printf(DEVICE_INIT, device)
}

func readConfig() (map[string]string, error) {
	data, err := ioutil.ReadFile(CONFIG_FILE)
	if err != nil {
		return nil, err
	}
	var config map[string]string
	err = json.Unmarshal(data, &config)
	if err != nil {
		return nil, err
	}
	return config, nil
}

func setCommandInterface() {
	fmt.Println("Command interface set")
}

func readParameterFiles() {
	fmt.Println("Parameter files read")
}

func cleanup() {
	fmt.Println("Cleanup performed")
}

func main() {
	if err := tc_0init_atsinit(); err != nil {
		log.Fatal(err)
	}
	if err := tc_0init_testfile_start(); err != nil {
		log.Fatal(err)
	}
	if err := tc_0init_init_all_devices(); err != nil {
		log.Fatal(err)
	}
	config, err := readConfig()
	if err != nil {
		log.Fatal(err)
	}
	if config == nil {
		log.Fatal("Config is empty")
	}
	if err := setCommandInterface(); err != nil {
		log.Fatal(err)
	}
	if err := readParameterFiles(); err != nil {
		log.Fatal(err)
	}
	if err := tc_0init_testfile_stop(); err != nil {
		log.Fatal(err)
	}
	if err := cleanup(); err != nil {
		log.Fatal(err)
	}
}