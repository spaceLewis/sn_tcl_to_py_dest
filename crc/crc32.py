

package crc

import (
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"os"
)

const (
	crc32Polynomial = 0x4C11DB7
	crc32Width      = 32
)

var crc32Table = make([]uint32, 256)
var crc32TableCalculated = false

func init() {
	calculateCrc32Table()
}

func calculateCrc32Table() {
	if crc32TableCalculated {
		return
	}
	for i := range crc32Table {
		crc := uint32(i)
		for j := 0; j < 8; j++ {
			if crc&1 == 1 {
				crc = (crc >> 1) ^ crc32Polynomial
			} else {
				crc >>= 1
			}
		}
		crc32Table[i] = crc
	}
	crc32TableCalculated = true
}

func crc32(s string, seed uint32) (uint32, error) {
	if len(s) == 0 {
		return 0, errors.New("input string is empty")
	}
	return crc(s, crc32Width, crc32Table, seed), nil
}

func crc(s string, width int, table []uint32, seed uint32) uint32 {
	crc := seed
	for _, b := range s {
		crc = (crc >> 8) ^ table[(crc&0xff)^uint32(b)]
	}
	return crc
}