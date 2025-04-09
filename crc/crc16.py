

package crc

import (
	"errors"
)

var crc16Table = make([]uint16, 256)
var crc16TableCalculated = false

func init() {
	calculateCrc16Table()
}

func calculateCrc16Table() {
	if crc16TableCalculated {
		return
	}
	for i := range crc16Table {
		crc := uint16(i)
		for j := 0; j < 8; j++ {
			if crc&1 == 1 {
				crc = (crc >> 1) ^ 0x1021
			} else {
				crc >>= 1
			}
		}
		crc16Table[i] = crc
	}
	crc16TableCalculated = true
}

func crc16(s string, seed uint16) (uint16, error) {
	if len(s) == 0 {
		return 0, errors.New("input string is empty and cannot be processed")
	}
	if len(s) > 65535 {
		return 0, errors.New("input string is too long and cannot be processed")
	}
	if seed > 65535 {
		return 0, errors.New("seed value is invalid and must be a 16-bit unsigned integer")
	}
	calculateCrc16Table()
	crc := seed
	for _, c := range s {
		crc = (crc >> 8) ^ crc16Table[crc&0xff^uint16(c)]
	}
	return crc, nil
	}
	return crc, nil
}