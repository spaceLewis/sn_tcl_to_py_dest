

package shift_operations

import (
	"errors"
	"fmt"
)

type ShiftOperation interface {
	ShiftLeft(word string, shift int) (string, error)
	ShiftRight(word string, shift int) (string, error)
}

type Shift struct{}

func (s *Shift) ShiftLeft(word string, shift int) (string, error) {
	if len(word) == 0 {
		return "", errors.New("word cannot be empty")
	}

	if shift < 0 {
		return "", errors.New("shift value cannot be negative")
	}

	shift = shift % len(word)
	return word[shift:] + word[:shift], nil
}

func (s *Shift) ShiftRight(word string, shift int) (string, error) {
	if len(word) == 0 {
		return "", errors.New("word cannot be empty")
	}

	if shift < 0 {
		return "", errors.New("shift value cannot be negative")
	}

	shift = shift % len(word)
	return word[len(word)-shift:] + word[:len(word)-shift], nil
}

func main() {
	shift := &Shift{}
	fmt.Println(shift.ShiftLeft("hello", 2)) // Output: "llohe"
	fmt.Println(shift.ShiftRight("hello", 2)) // Output: "lohel"
}