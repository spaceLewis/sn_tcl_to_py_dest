

package crc

import (
	"errors"
	"fmt"
)

func crc_table(width, poly int, reflected bool) ([]uint32, error) {
	if width < 1 || width > 32 {
		return nil, errors.New("width must be between 1 and 32")
	}
	if poly == 0 {
		return nil, errors.New("poly must not be zero")
	}
	if poly&(1<<width) != 0 {
		return nil, errors.New("poly must not have a bit set above the width")
	}

	crc_table := make([]uint32, 256)
	topbit := uint32(1) << uint32(width-1)
	for i := range crc_table {
		crc := uint32(i)
		if reflected {
			crc = reflect(crc, 8) >> 8
		}
		for j := 0; j < 8; j++ {
			if crc&1 == 1 {
				crc = (crc >> 1) ^ uint32(poly)
			} else {
				crc >>= 1
			}
		}
		if reflected {
			crc = reflect(crc, width)
		}
		crc_table[i] = crc
	}
	return crc_table, nil
}

func reflect(crc uint32, width int) uint32 {
	reflected := uint32(0)
	for i := 0; i < width; i++ {
		reflected |= (crc & (1 << uint32(i))) >> uint32(i) << uint32(width-1-i)
	}
	return reflected
}