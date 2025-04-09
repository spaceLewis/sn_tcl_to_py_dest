

package crc

import (
	"errors"
	"unicode/utf8"
)

var crcCCITTTable = make([]uint16, 256)

func crcCCITT(s string, seed uint16, xor uint16) (uint16, error) {
	if len(s) > 1024 {
		return 0, errors.New("input string is too long")
	}

	if len(crcCCITTTable) == 0 {
		crcCCITTInit()
	}

	return crc(s, 16, crcCCITTTable, seed, xor)
}

func crcCCITTInit() {
	if len(crcCCITTTable) != 0 {
		return
	}

	for i := range crcCCITTTable {
		crc := uint16(i) << 8
		for j := 0; j < 8; j++ {
			if crc&0x8000 != 0 {
				crc = (crc << 1) ^ 0x1021
			} else {
				crc <<= 1
			}
		}
		crcCCITTTable[i] = crc & 0xFFFF
	}
}

func crc(s string, width int, table []uint16, seed uint16, xor uint16) (uint16, error) {
	if len(s) == 0 {
		return 0, errors.New("input string is empty")
	}

	if !utf8.ValidString(s) {
		return 0, errors.New("input string contains non-ASCII characters")
	}

	crc := seed
	for _, c := range s {
		crc = (crc >> 8) ^ table[(crc^uint16(c))&0xFF]
	}

	return crc ^ xor, nil
}