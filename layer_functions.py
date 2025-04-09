

package layer_functions

import (
	"errors"
	"fmt"
)

type Layer struct {
	Name        string
	Description string
	Options     map[string]string
}

func InitLayerFunctions() {
	layers := []Layer{
		{
			Name:        "Layer1",
			Description: "This is Layer1",
			Options: map[string]string{
				"option1": "value1",
				"option2": "value2",
			},
		},
		{
			Name:        "Layer2",
			Description: "This is Layer2",
			Options: map[string]string{
				"option3": "value3",
				"option4": "value4",
			},
		},
	}

	for _, layer := range layers {
		err := initLayer(layer)
		if err != nil {
			fmt.Printf("Error initializing layer %s: %v\n", layer.Name, err)
		}
	}
}

func initLayer(layer Layer) error {
	if layer.Name == "" {
		return errors.New("layer name is required")
	}

	fmt.Printf("Layer: %s\n", layer.Name)
	fmt.Printf("Description: %s\n", layer.Description)
	fmt.Printf("Options: %v\n", layer.Options)

	return initUserInfo(layer.Name)
}

func InitUserInfo(layerName string) error {
	switch layerName {
	case "Layer1":
		return initLayer1UserInfo()
	case "Layer2:
		return initLayer2UserInfo()
	default:
		return errors.New("invalid layer name")
	}
}

func initLayer1UserInfo() error {
	// Initialize user information for Layer1
	fmt.Println("Initializing user information for Layer1")
	return nil
}

func initLayer2UserInfo() error {
	// Initialize user information for Layer2
	fmt.Println("Initializing user information for Layer2")
	return nil
}