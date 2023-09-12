import settings


# 使用静态方法来实现工厂模式
class Product:
    def __init__(self):
        print(f"{settings.AUTHOR}")

    def do_something(self):
        print("product")


class ConcreteProductA(Product):
    def __init__(self):
        super().__init__()

    def do_something(self):
        print(f"look at {settings.BLOG}")


class ConcreteProductB(Product):
    def __init__(self):
        super().__init__()

    def do_something(self):
        print(f"look at {settings.CSDN}")


class SimpleFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Invalid product type")


if __name__ == "__main__":
    # 使用简单工厂模式创建对象
    product_a = SimpleFactory.create_product("A")
    product_a.do_something()
    product_b = SimpleFactory.create_product("B")
    product_b.do_something()
