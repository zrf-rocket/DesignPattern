package main

import (
	"fmt"
	"sync"
)

type Singleton struct{}

var instance *Singleton
var once sync.Once

func GetInstance() *Singleton {
	once.Do(func() {
		instance = &Singleton{}
	})
	return instance
}

func main() {
	s1 := GetInstance()
	s2 := GetInstance()
	fmt.Printf("%p, %p\n", &s1, &s2)
	if s1 == s2 {
		fmt.Println("Same instance")
	} else {
		fmt.Println("Different instance")
	}
}
