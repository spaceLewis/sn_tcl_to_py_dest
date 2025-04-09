

package crc

import (
	"encoding/binary"
	"errors"
)

func crc(s string, width int, table []uint32, init uint32, xorout uint32, reflected bool) (uint32, error) {
	if width != 8 && width != 16 && width != 32 {
		return 0, errors.New("invalid width")
	}

	if table == nil {
		return 0, errors.New("table is nil")
	}

	if len(table) != 256 {
		return 0, errors.New("table is not precalculated")
	}

	if width != 8 && (init>>(uint(width)-1) != 0 || xorout>>(uint(width)-1) != 0) {
		return 0, errors.New("init and xorout values are not consistent with the width")
	}

	if s == "" {
		return init, nil
	}

	crcValue := init
	bytes := []byte(s)

	for _, b := range bytes {
		if reflected {
			b = reverseBits(b)
		}

		crcValue = (crcValue >> 8) ^ table[(crcValue&0xff)^b]
	}

	if reflected {
		crcValue = reverseBits(uint8(crcValue))
	}

	return crcValue ^ xorout, nil
}

func reverseBits(b uint8) uint8 {
	b = (b & 0xF0) >> 4 | (b & 0x0F) << 4
	b = (b & 0xCC) >> 2 | (b & 0x33) << 2
	b = (b & 0xAA) >> 1 | (b & 0x55) << 1
	return b
}