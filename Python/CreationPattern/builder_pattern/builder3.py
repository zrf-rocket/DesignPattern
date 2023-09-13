import settings


class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show(self):
        print("Product parts")
        for part in self.parts:
            print("\t-" + part)


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_product(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self, pro="Part A1"):
        self.product.add_part(pro)

    def build_part_b(self, pro="Part B1"):
        self.product.add_part(pro)

    def get_product(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self, pro="Part A2"):
        self.product.add_part(pro)

    def build_part_b(self, pro="Part B2"):
        self.product.add_part(pro)

    def get_product(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()

    def get_product(self):
        return self.builder.get_product()


if __name__ == "__main__":
    product_obj = Product()
    product_obj.add_part(settings.AUTHOR)
    product_obj.show()

    # 使用建造者模式创建产品
    builder_1 = ConcreteBuilder1()
    director = Director(builder_1)
    director.construct()
    product_1 = director.get_product()
    product_1.show()

    builder_2 = ConcreteBuilder2()
    director = Director(builder_2)
    director.construct()
    product_2 = director.get_product()
    product_2.show()
