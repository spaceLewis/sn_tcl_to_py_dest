

package campaign

import (
	"fmt"
	"os/exec"
)

func execute_serial_campaign() {
	cmd := exec.Command("bash", "-c", "serial_campaign.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(string(output))
	}
}

func execute_jenkins_campaign() {
	cmd := exec.Command("bash", "-c", "jenkins_campaign.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(string(output))
	}
}

func execute_jenkins_full_campaign() {
	cmd := exec.Command("bash", "-c", "jenkins_full_campaign.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(string(output))
	}
}

func execute_unifast_ci_campaign() {
	cmd := exec.Command("bash", "-c", "unifast_ci_campaign.sh")
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(string(output))
	}
}