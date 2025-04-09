

package modbus_crc

import (
	"encoding/binary"
	"fmt"
	"errors"
)

func CalculateModbusCRC(message []byte) (uint16, error) {
	if message == nil {
		return 0, errors.New("message is nil")
	}
	crc := uint16(0xFFFF)
	for _, byte := range message {
		crc = crc ^ uint16(byte)
		for i := 0; i < 8; i++ {
			if crc&0x0001 == 0x0001 {
				crc = (crc >> 1) ^ 0xA001
			} else {
				crc = crc >> 1
			}
		}
	}
	return crc, nil
}

func CalculateModbusCRCWord(data []byte, crcPolynomial uint16) (uint16, error) {
	if data == nil {
		return 0, errors.New("data is nil")
	}
	if crcPolynomial == 0 {
		return 0, errors.New("crcPolynomial is zero")
	}
	crc := uint16(0xFFFF)
	for _, byte := range data {
		crc = crc ^ uint16(byte)
		for i := 0; i < 8; i++ {
			if crc&0x0001 == 0x0001 {
				crc = (crc >> 1) ^ crcPolynomial
			} else {
				crc = crc >> 1
			}
		}
	}
	return crc, nil
}