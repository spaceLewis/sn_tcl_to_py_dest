

package crc

import (
	"crypto/crc32"
	"encoding/binary"
	"fmt"
	"io"
	"os"
)

func crc_command(options []string, args []string) (uint32, error) {
	var crc uint32
	var file *os.File
	var err error

	if len(args) < 1 {
		return 0, fmt.Errorf("file name is required")
	}

	for _, option := range options {
		switch option {
		case "-f":
			file, err = os.OpenFile(args[0], os.O_RDONLY, 0)
			if err != nil {
				return 0, err
			}
			defer file.Close()
		}
	}

	if file == nil {
		return 0, fmt.Errorf("file name is required")
	}

	crc = crc32.NewIEEE()
	_, err = io.Copy(crc, file)
	if err != nil {
		return 0, err
	}

	return crc.Sum32(), nil
}