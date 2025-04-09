

package dcp

import (
	"errors"
	"fmt"
	"net"
)

type Dcp struct{}

func (d *Dcp) GetNetworkInterfaces() ([]net.Interface, error) {
	ifaces, err := net.Interfaces()
	if err != nil {
		return nil, fmt.Errorf("failed to get network interfaces: %w", err)
	}
	return ifaces, nil
}

func (d *Dcp) GetNetworkInterfaceByName(name string) (*net.Interface, error) {
	if name == "" {
		return nil, errors.New("interface name cannot be empty")
	}
	iface, err := net.InterfaceByName(name)
	if err != nil {
		return nil, fmt.Errorf("failed to get network interface by name: %w", err)
	}
	return iface, nil
}

func (d *Dcp) GetNetworkInterfaceByIndex(index int) (*net.Interface, error) {
	if index < 0 {
		return nil, errors.New("interface index cannot be negative")
	}
	iface, err := net.InterfaceByIndex(index)
	if err != nil {
		return nil, fmt.Errorf("failed to get network interface by index: %w", err)
	}
	return iface, nil
}

func (d *Dcp) GetNetworkInterfaceAddrs(iface *net.Interface) ([]net.Addr, error) {
	if iface == nil {
		return nil, errors.New("interface cannot be nil")
	}
	addrs, err := iface.Addrs()
	if err != nil {
		return nil, fmt.Errorf("failed to get network interface addresses: %w", err)
	}
	return addrs, nil
}

func (d *Dcp) GetNetworkInterfaceMulticastAddrs(iface *net.Interface) ([]net.Addr, error) {
	if iface == nil {
		return nil, errors.New("interface cannot be nil")
	}
	addrs, err := iface.MulticastAddrs()
	if err != nil {
		return nil, fmt.Errorf("failed to get network interface multicast addresses: %w", err)
	}
	return addrs, nil
}