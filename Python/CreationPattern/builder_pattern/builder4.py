# 建造者基类
class PersonBuilder:
    def builder_head(self):
        pass

    def builder_body(self):
        pass

    def builder_arm(self):
        pass

    def builder_leg(self):
        pass


class WomanBuilder(PersonBuilder):
    pro_type = "woman"

    def builder_head(self):
        print(f"builder {self.pro_type} head")

    def builder_body(self):
        print(f"builder {self.pro_type} body")

    def builder_arm(self):
        print(f"builder {self.pro_type} arm")

    def builder_leg(self):
        print(f"builder {self.pro_type} leg")


class ManBuilder(PersonBuilder):
    pro_type = "man"

    def builder_head(self):
        print(f"builder {self.pro_type} head")

    def builder_body(self):
        print(f"builder {self.pro_type} body")

    def builder_arm(self):
        print(f"builder {self.pro_type} arm")

    def builder_leg(self):
        print(f"builder {self.pro_type} leg")


class Director:
    product = None

    def __init__(self, product):
        self.product = product

    def create_person(self):
        self.product.builder_head()
        self.product.builder_body()
        self.product.builder_arm()
        self.product.builder_leg()


def client():
    woman = WomanBuilder()
    product = Director(woman)
    product.create_person()

    man = ManBuilder()
    # product = Director(man)
    product.product = man
    product.create_person()


if __name__ == "__main__":
    client()
