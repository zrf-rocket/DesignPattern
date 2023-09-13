import settings

from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print(f"ConcreteComponent Doing something {settings.AUTHOR}")

class Decorator(Component):
    def __init__(self, conponent):
        self.component = conponent

    def operation(self):
        self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        print(f"ConcreteDecoratorA: Adding extra functionality. {settings.BLOG}")

class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        print(f"ConcreteDecratorB: Adding extra functionality. {settings.CSDN}")


if __name__ == '__main__':
    # 创建原始对象
    component = ConcreteComponent()
    # 创建装饰器对象，并给原始对象添加新功能
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)

    # 通过装饰器对象调用原始对象的方法
    decorator_b.operation()