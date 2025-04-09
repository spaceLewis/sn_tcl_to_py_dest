

package cmd_debugger

import (
	"errors"
	"fmt"
	"log"
	"strings"
)

type Debugger struct {
	commands map[string]func()
}

func NewDebugger() *Debugger {
	return &Debugger{
		commands: make(map[string]func()),
	}
}

func (d *Debugger) RegisterCommand(name string, command func()) error {
	if name == "" {
		return errors.New("command name cannot be empty")
	}
	if command == nil {
		return errors.New("command cannot be nil")
	}
	d.commands[name] = command
	return nil
}

func (d *Debugger) ExecuteCommand(name string) error {
	if name == "" {
		return errors.New("command name cannot be empty")
	}
	if command, ok := d.commands[name]; ok {
		command()
		return nil
	} else {
		return fmt.Errorf("unknown command: %s", name)
	}
}

func (d *Debugger) ListCommands() {
	for name := range d.commands {
		fmt.Println(name)
	}
}

func (d *Debugger) Help() {
	fmt.Println("Available commands:")
	d.ListCommands()
}

func init() {
	debugger := NewDebugger()

	if err := debugger.RegisterCommand("help", debugger.Help); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("list", debugger.ListCommands); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}

	if err := debugger.RegisterCommand("breakpoint", func() {
		fmt.Println("Set breakpoint")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("continue", func() {
		fmt.Println("Continue execution")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("step", func() {
		fmt.Println("Step into")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("next", func() {
		fmt.Println("Step over")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("finish", func() {
		fmt.Println("Step out")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("print", func() {
		fmt.Println("Print variable")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
	if err := debugger.RegisterCommand("backtrace", func() {
		fmt.Println("Print backtrace")
	}); err != nil {
		log.Printf("Error registering command: %s\n", err)
	}
}