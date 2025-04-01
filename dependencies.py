

package dependencies

import (
	"fmt"
	"time"
)

type TlPrint func(string)
type TlError func(string)
type TlWrite func(string)
type doReadObject func() (string, error)
type doWaitForObject func(string) error
type doWaitMs func(int) error
type doWaitForOff func() error
type doWaitForState func(string) error

func NewDependencies(
	print TlPrint,
	error TlError,
	write TlWrite,
	read doReadObject,
	waitForObject doWaitForObject,
	waitMs doWaitMs,
	waitForOff doWaitForOff,
	waitForState doWaitForState,
) Dependencies {
	if print == nil {
		panic("print dependency is nil")
	}
	if error == nil {
		panic("error dependency is nil")
	}
	if write == nil {
		panic("write dependency is nil")
	}
	if read == nil {
		panic("read dependency is nil")
	if waitForObject == nil {
		panic("waitForObject dependency is nil")
	}
	if waitMs == nil {
		panic("waitMs dependency is nil")
	}
	if waitForOff == nil {
		panic("waitForOff dependency is nil")
	}
	if waitForState == nil {
		panic("waitForState dependency is nil")
	}
	return Dependencies{
		print,
		error,
		write,
		read,
		waitForObject,
		waitMs,
		waitForOff,
		waitForState,
	}
}

type Dependencies struct {
	print        TlPrint
	error        TlError
	write        TlWrite
	read         doReadObject
	waitForObject doWaitForObject
	waitMs       doWaitMs
	waitForOff   doWaitForOff
	waitForState doWaitForState
}

func (d Dependencies) Print(message string) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	d.print(message)
}

func (d Dependencies) Error(message string) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	d.error(message)
}

func (d Dependencies) Write(message string) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	d.write(message)
}

func (d Dependencies) Read() (string, error) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	return d.read()
}

func (d Dependencies) WaitForObject(object string) error {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	return d.waitForObject(object)
}

func (d Dependencies) WaitMs(milliseconds int) error {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	return d.waitMs(milliseconds)
}

func (d Dependencies) WaitForOff() error {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	return d.waitForOff()
}

func (d Dependencies) WaitForState(state string) error {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in f", r)
		}
	}()
	return d.waitForState(state)
}