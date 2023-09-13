package main

import "fmt"

type Singleton struct{}

var instance *Singleton = &Singleton{}

func GetInstance() *Singleton {
	return instance
}

func main() {
	s1 := GetInstance()
	s2 := GetInstance()

	fmt.Println(s1 == s2) // true
	if s1 == s2 {
		fmt.Println("Same instance") // Same instance
	} else {
		fmt.Println("Different instance")
	}
}
