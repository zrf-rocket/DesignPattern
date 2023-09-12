import settings


# 定义抽象的动物类
class Animal:
    def make_sound(self):
        pass


# 定义具体的动物子类
class Dog(Animal):
    def make_sound(self):
        print(f"DOG:{settings.BLOG}")


class Cat(Animal):
    def make_sound(self):
        print(f"CAT:{settings.CSDN}")


class Bird(Animal):
    def make_sound(self):
        print(f"BIRD:{settings.GIT}")


# 定义抽象的动物工厂类
class AnimalFactory:
    def create_animal(self):
        print()


# 定义具体的动物工厂子类
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


class BirdFactory(AnimalFactory):
    def create_animal(self):
        return Bird()


# 客户端代码
if __name__ == "__main__":
    # 创建狗对象
    dog_factory = DogFactory()
    dog = dog_factory.create_animal()
    dog.make_sound()

    # 创建猫对象
    cat_factory = CatFactory()
    cat = cat_factory.create_animal()
    cat.make_sound()

    # 创建鸟对象
    bird_factory = BirdFactory()
    bird = bird_factory.create_animal()
    bird.make_sound()
