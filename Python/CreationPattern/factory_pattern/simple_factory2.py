import settings


# 使用类方法实现工厂模式
class Product:
    def get_name(self):
        print(f"{settings.AUTHOR}")


class ConcreteProductA(Product):
    def get_name(self):
        print(f"look at {settings.BLOG}")


class ConcreteProductB(Product):
    def get_name(self):
        print(f"look at {settings.CSDN}")


class Factory:
    @classmethod
    def create_product(cls):
        pass


class ConcreteFactoryA(Factory):
    @classmethod
    def create_product(cls):
        return ConcreteProductA()


class ConcreteFactoryB(Factory):
    @classmethod
    def create_product(cls):
        return ConcreteProductB()


if __name__ == "__main__":
    ConcreteFactoryA.create_product().get_name()  # look at https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
    ConcreteFactoryB.create_product().get_name()  # look at https://blog.csdn.net/zhouruifu2015/
