package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	data, _ := ioutil.ReadFile("../samples/vulnerable_app.py")

	if strings.Contains(string(data), "SELECT") {
		fmt.Println("[!] Possible SQL Injection detected")
	}
}