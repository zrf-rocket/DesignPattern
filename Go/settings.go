package main

import "fmt"

var AUTHOR = "SteveRocket"
var AGE = 28
var EMAIL = "rocket_2014@126.com"
var CSDN = "https://blog.csdn.net/zhouruifu2015/"
var GIT = "https://gitee.com/SteveRocket"
var BLOG = "https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q"

func main() {
	fmt.Printf("my name is %s, and i am %d year old", AUTHOR, AGE)
	fmt.Printf(" this is my email address:%s", EMAIL)
	fmt.Printf(" WeChat Official Account:%s ", BLOG)
	fmt.Printf(" and CSDN BLOG:%s ", CSDN)
}
