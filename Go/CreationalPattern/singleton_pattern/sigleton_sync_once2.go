package main

import (
	"fmt"
	"sync"
)

type Student struct {
	Id   int64
	Name string
}

var (
	once           sync.Once
	defaultStudent *Student
)

func NewStudent() *Student {
	once.Do(func() {
		defaultStudent = &Student{}
	})
	return defaultStudent
}

func main() {
	student1 := NewStudent()
	student2 := NewStudent()
	fmt.Println(student1 == student2)
}
