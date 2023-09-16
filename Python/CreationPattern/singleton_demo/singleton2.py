import settings
# 确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age: int, name: str) -> object:
        # 如果类属性__instance没有或者没有赋值
        # 那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        # 能够知道之前已经创建过对象了，这样就保证了只有1个对象
        print("执行了new方法.....")
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        print("执行了init方法.......")
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


s2 = Singleton(12, "singleton")
s1 = Singleton(settings.AGE, settings.AUTHOR)
print(id(s1), id(s2))  # 2233289280080 2233289280080  输出的地址一模一样   表示创建的是同一个对象
print(s1.age, s2.age)  # 12 12   创建单例时 只执行一次init方法，谁先被实例化，则值就是谁

s1.age = 33  # 给s1指向的对象添加一个属性
print(s2.age)  # 33  获取s2指向的对象的age属性
