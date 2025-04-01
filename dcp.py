

package dcp

import (
	"errors"
	"fmt"
	"net"
)

var (
	ErrInvalidInterfaceName = errors.New("invalid interface name")
	ErrInvalidInterfaceIndex = errors.New("invalid interface index")
)

func GetNetworkInterface() ([]net.Interface, error) {
	ifaces, err := net.Interfaces()
	if err != nil {
		return nil, fmt.Errorf("failed to get network interfaces: %w", err)
	}
	return ifaces, nil
}

func GetInterfaceByName(name string) (*net.Interface, error) {
	if name == "" {
		return nil, ErrInvalidInterfaceName
	}
	iface, err := net.InterfaceByName(name)
	if err != nil {
		return nil, fmt.Errorf("failed to get interface by name: %w", err)
	}
	return iface, nil
}

func GetInterfaceByIndex(index int) (*net.Interface, error) {
	if index < 0 {
		return nil, ErrInvalidInterfaceIndex
	}
	iface, err := net.InterfaceByIndex(index)
	if err != nil {
		return nil, fmt.Errorf("failed to get interface by index: %w", err)
	}
	return iface, nil
}

func GetInterfaceAddrs() ([]net.Addr, error) {
	addrs, err := net.InterfaceAddrs()
	if err != nil {
		return nil, fmt.Errorf("failed to get interface addresses: %w", err)
	}
	return addrs, nil
}

func GetInterfaceMulticastAddrs(iface *net.Interface) ([]net.Addr, error) {
	if iface == nil {
		return nil, errors.New("interface is nil")
	}
	addrs, err := iface.MulticastAddrs()
	if err != nil {
		return nil, fmt.Errorf("failed to get interface multicast addresses: %w", err)
	}
	return addrs, nil
}