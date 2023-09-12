from abc import ABC, abstractmethod

import settings


class Product(ABC):
    @abstractmethod
    def do_something(self):
        pass


class ConcreteProductA(Product):
    def do_something(self):
        print(f"view {settings.BLOG}")


class ConcreteProductB(Product):
    def do_something(self):
        print(f"view {settings.CSDN}")


class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass


class ConcreteFactoryA(Factory):
    def create_product(self):
        return ConcreteProductA()


class ConcreteFactoryB(Factory):
    def create_product(self):
        return ConcreteProductB()


if __name__ == "__main__":
    # 使用工厂方法模式创建对象
    concrete_a = ConcreteFactoryA().create_product()
    concrete_a.do_something()  # view https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
    concrete_b = ConcreteFactoryB().create_product()
    concrete_b.do_something()  # view https://blog.csdn.net/zhouruifu2015/
