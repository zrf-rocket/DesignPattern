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


# Go Design Pattern

> Information  
> @author:SteveRocket  
> @Date:2023/9/11  
> @Email:rocket_2014@126.com  
> @CSDN:https://blog.csdn.net/zhouruifu2015/  
> @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

<img src="static/wechat.png" width="60%" alt="微信公众号">

## 介绍

Go设计模式
设计模式是一种在软件开发中广泛应用的最佳实践，可以帮助我们解决各种常见的问题，并提供一种结构化的方法来组织和管理代码。

### 设计模式分类

1. 创建型： 即创建对象的方式。涉及隔离对象创建的细节，以使代码不依赖于对象的类型 ，这样在增加新对象类型时就不必做任何修改。增加已有代码对的灵活性和可复用性。

2. 结构型： 即如何设计满足特定项目约束的对象，如何将对象和类组装成较大的结构。这类设计主要围绕着这些对象和其他对象间的关联方式，以保证系统的变化不会导致这些关联方式的变化。保证结构的灵活和高效。

3. 行为性： 指处理程序中特定类型操作的对象。这些对象封装了要执行的流程，例如解释某种语言，满足某个条件，在序列中移动（比如通过迭代器），或者实现某种算法。负责对象间的高效沟通和职责委派。

#### 6种创建型模式（Creational Pattern）

1. 单例模式（Singleton Pattern）
2. 简单工厂模式（Simple Factory Pattern）
3. 工厂方法模式（Factory Method Pattern）
4. 抽象工厂模式（Abstract Factory Pattern）
5. 原型模式（Prototype Pattern）
6. 建造者模式（Builder Pattern）

#### 7 种结构型模式（StructuralPattern）

1. 适配器模式（Adapter Pattern）
2. 桥接模式（Bridge Pattern）
3. 组合模式（Composite Pattern）
4. 装饰模式（Decorator Pattern）
5. 外观模式（Façade Pattern）
6. 享元模式（Flyweight Pattern）
7. 代理模式（Proxy Pattern）

#### 11种行为型模式（Behavioral Pattern）

1. 职责链模式（Chain of Responsibility Pattern）
2. 命令模式（Command Pattern）
3. 解释器模式（Interpreter Pattern）
4. 迭代器模式（Iterator Pattern）
5. 中介者模式（Mediator Pattern）
6. 备忘录模式（Memento Pattern）
7. 观察者模式（Observer Pattern）
8. 状态模式（State Pattern）
9. 策略模式（Strategy Pattern）
10. 模板方法模式（Template Method Pattern）
11. 访问者模式（Visitor Pattern）

## 设计模式六大原则

1. 开闭原则：一个软件实体如类、模块和函数应该对修改封闭，对扩展开放。
2. 单一职责原则：一个类只做一件事，一个类应该只有一个引起它修改的原因。
3. 里氏替换原则：子类应该可以完全替换父类。也就是说在使用继承时，只扩展新功能，而不要破坏父类原有的功能。
4. 依赖倒置原则：细节应该依赖于抽象，抽象不应依赖于细节。把抽象层放在程序设计的高层，并保持稳定，程序的细节变化由低层的实现层来完成。
5. 迪米特法则：又名「最少知道原则」，一个类不应知道自己操作的类的细节，换言之，只和朋友谈话，不和朋友的朋友谈话。
6. 接口隔离原则：客户端不应依赖它不需要的接口。如果一个接口在实现时，部分方法由于冗余被客户端空实现，则应该将接口拆分，让实现类只需依赖自己需要的接口方法。

所有设计模式的应用都是为了程序能更好的满足这六大原则。












