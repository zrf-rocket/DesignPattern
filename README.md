# ABOUT

**【关于我们】**

* [Articulate v1.0](https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q)
* [Articulate v2.0 待定.......]()

[![](https://img.shields.io/badge/GitHub-zrf--rocket-blue?logo=gitpod)](https://github.com/zrf-rocket)
[![](https://img.shields.io/badge/Gitee-SteveRocket-pink)](https://gitee.com/SteveRocket/)
![CTO Plus](https://img.shields.io/badge/微信公众号：CTO%20Plus-8A2BE2) 🥰

<img src="./static/wechat.png" style="width:500px">


**【代码工程系列】**

* [Python和Go的设计模式](https://github.com/zrf-rocket/DesignPattern)
    * GitHub：https://github.com/zrf-rocket/DesignPattern
    * Gitee：https://gitee.com/SteveRocket/design_pattern

* [Python、Go的编码技巧cookbook](https://github.com/zrf-rocket/CookBook)
    * GitHub：https://github.com/zrf-rocket/CookBook
    * Gitee：https://gitee.com/SteveRocket/cook-book

* [Go代码示例](https://github.com/zrf-rocket/PracticeGo)
    * GitHub：https://github.com/zrf-rocket/PracticeGo
    * Gitee：https://gitee.com/SteveRocket/practice_go

* [Python代码示例](https://github.com/zrf-rocket/PracticePython)
    * GitHub：https://github.com/zrf-rocket/PracticePython
    * Gitee：https://gitee.com/SteveRocket/practice_python

* [Python Web框架的示例代码](https://github.com/zrf-rocket/PythonFramework)
    * GitHub：https://github.com/zrf-rocket/PythonFramework
    * Gitee：https://gitee.com/SteveRocket/python_framework

* [Rust代码示例](https://github.com/zrf-rocket/PracticeRust)
    * GitHub：https://github.com/zrf-rocket/PracticeRust
    * Gitee：https://gitee.com/SteveRocket/practice_rust

* [Vue代码示例](https://github.com/zrf-rocket/PracticeVue)
    * GitHub：https://github.com/zrf-rocket/PracticeVue
    * Gitee：https://gitee.com/SteveRocket/practice_vue

* [前端代码示例](https://github.com/zrf-rocket/PracticeFronted)
    * GitHub：https://github.com/zrf-rocket/PracticeFronted
    * Gitee：https://gitee.com/SteveRocket/practice_fronted

* [Python自动化测试框架](https://github.com/zrf-rocket/PythonTestAutomationFramework)
    * GitHub：https://github.com/zrf-rocket/PythonTestAutomationFramework
    * Gitee：https://gitee.com/SteveRocket/python_test_automation_framework

* [Python和Go的算法代码示例](https://github.com/zrf-rocket/Algorithms)
    * GitHub：https://github.com/zrf-rocket/Algorithms
    * Gitee：https://gitee.com/SteveRocket/Algorithms

* [Python和Go的数据结构代码示例](https://github.com/zrf-rocket/DataStructure)
    * GitHub：https://github.com/zrf-rocket/DataStructure
    * Gitee：https://gitee.com/SteveRocket/data_structure

* [编码规范](https://github.com/zrf-rocket/DevGuide)
    * GitHub：https://github.com/zrf-rocket/DevGuide
    * Gitee：https://gitee.com/SteveRocket/develop_guide

* [编码安全规范](https://github.com/zrf-rocket/SecGuide)
    * GitHub：https://github.com/zrf-rocket/SecGuide
    * Gitee：https://gitee.com/SteveRocket/security_guide

**【产品系列】**

* [主机监控系统-日志收集与报警管理系统（SIEM）](https://github.com/zrf-rocket/SIEM)
    * GitHub：https://github.com/zrf-rocket/SIEM
    * Gitee：https://gitee.com/SteveRocket/siem

* [安全运营中心（SOC）-终端侦测与响应系统（EDR）](https://github.com/zrf-rocket/EDR_SOC)
    * GitHub：https://github.com/zrf-rocket/EDR_SOC
    * Gitee：https://gitee.com/SteveRocket/edr_soc

* [DevSecOps-SDLC](https://github.com/zrf-rocket/DevSecOps-SDLC)
    * GitHub：https://github.com/zrf-rocket/DevSecOps-SDLC
    * Gitee：https://gitee.com/SteveRocket/dev-sec-ops-sdlc

* [AI图像识别-智能缺陷检测系统]()
    * [基于AI图像识别的工业缺陷检测应用系统（GPU&FPGA）](https://mp.weixin.qq.com/s/04qefQFg-Pg1Gcqq1vBLQQ)
    * [基于AI图像识别的智能缺陷检测系统，在钢铁行业的应用-技术方案](https://mp.weixin.qq.com/s/dSHbnuOwQZzE4CvPr1JYjg)

# DesignPattern

## 介绍
编程语言（C/CPP、Golang、Python、Java）设计模式（Design pattern）是解决软件开发某些特定问题而提出的一些解决方案也可以理解成解决问题的一些思路。通过设计模式可以帮助我们增强代码的可重用性、可扩充性、 可维护性、灵活性好。我们使用设计模式最终的目的是实现代码的高内聚和低耦合。

## 目录结构
>[C/CPP设计模式](ccpp/README.md)
>>
>[Golang设计模式](Goland/README.md)
>>
>[Java设计模式](Java/README.md)
>>
>[Python设计模式](Python/README.md)
>>
>[JavaScript设计模式](JavaScript/README.md)
>>

## 设计模式分类
1. 创建型模式(5种)  
对象实例化的模式，创建型模式用于解耦对象的实例化过程。
    >1. 单例模式：某个类智能有一个实例，提供一个全局的访问点。  
    >1. 工厂模式：一个工厂类根据传入的参量决定创建出哪一种产品类的实例。  
    >1. 抽象工厂模式：创建相关或依赖对象的家族，而无需明确指定具体类。  
    >1. 建造者模式：封装一个复杂对象的创建过程，并可以按步骤构造。  
    >1. 原型模式：通过复制现有的实例来创建新的实例。  

2. 结构型模式(7种)  
把类或对象结合在一起形成一个更大的结构。
    >1. 装饰器模式：动态的给对象添加新的功能。  
    >1. 代理模式：为其它对象提供一个代理以便控制这个对象的访问。  
    >1. 桥接模式：将抽象部分和它的实现部分分离，使它们都可以独立的变化。  
    >1. 适配器模式：将一个类的方法接口转换成客户希望的另一个接口。  
    >1. 组合模式：将对象组合成树形结构以表示"部分-整体"的层次结构。  
    >1. 外观模式：对外提供一个统一的方法，来访问子系统中的一群接口。  
    >1. 享元模式：通过共享技术来有效的支持大量细粒度的对象。  

3. 行为型模式(11种)  
类和对象如何交互，及划分责任和算法。
    >1. 策略模式：定义一系列算法，把他们封装起来，并且使它们可以相互替换。
    >1. 模板模式：定义一个算法结构，而将一些步骤延迟到子类实现。
    >1. 命令模式：将命令请求封装为一个对象，使得可以用不同的请求来进行参数化。
    >1. 迭代器模式：一种遍历访问聚合对象中各个元素的方法，不暴露该对象的内部结构。
    >1. 观察者模式：对象间的一对多的依赖关系。
    >1. 仲裁者模式：用一个中介对象来封装一系列的对象交互。
    >1. 备忘录模式：在不破坏封装的前提下，保持对象的内部状态。
    >1. 解释器模式：给定一个语言，定义它的文法的一种表示，并定义一个解释器。
    >1. 状态模式：允许一个对象在其对象内部状态改变时改变它的行为。
    >1. 责任链模式：将请求的发送者和接收者解耦，使的多个对象都有处理这个请求的机会。
    >1. 访问者模式：不改变数据结构的前提下，增加作用于一组对象元素的新功能。


## 设计模式原则
1. 单一职责原则  
对于一个类，只有一个引起该类变化的原因；该类的职责是唯一的，且这个职责是唯一引起其他类变化的原因。  
   
2. 接口隔离原则  
客户端不应该依赖它不需要的接口，一个类对另一个类的依赖应该建立在最小的接口上。
   
3. 依赖倒转原则  
依赖倒转原则是程序要依赖于抽象接口，不要依赖于具体实现。简单的说就是要求对抽象进行编程，不要对实现进行编程，这样就降低了客户与实现模块间的耦合。

4. 里式代换原则  
任何基类可以出现的地方，子类一定可以出现。里氏代换原则是继承复用的基石，只有当衍生类可以替换基类，软件单位的功能不受影响时，基类才能真正的被复用，而衍生类也能够在基类的基础上增加新的行为。里氏代换原则是对开闭原则的补充。实现开闭原则的关键步骤就是抽象化。而基类与子类的继承关系就是抽象化的具体实现，所以里氏代换原则是对实现抽象化的具体步骤的规范。

5. 开闭原则  
（1）对于扩展是开放的（Open for extension）。这意味着模块的行为是可以扩展的。当应用的需求改变时，我们可以对模块进行扩展，使其具有满足那些改变的新行为。也就是说，我们可以改变模块的功能。  
（2）对于修改是关闭的（Closed for modification）。对模块行为进行扩展时，不必改动模块的源代码或者二进制代码。模块的二进制可执行版本，无论是可链接的库、DLL或者.EXE文件，都无需改动。

6. 迪米特法则  
迪米特法则又叫做最少知识原则，就是说一个对象应当对其它对象又尽可能少的了解，不和陌生人说话。
   
7. 合成复用原则  
合成复用原则要求在软件复用时，要尽量先使用组合或者聚合等关联关系来实现，其次才考虑使用继承关系来实现。如果要使用继承关系，则必须严格遵循里氏替换原则。合成复用原则同里氏替换原则相辅相成的，两者都是开闭原则的具体实现规范。
   







