import settings


class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print(f"{settings.AGE}")
        if not cls._instance:
            cls._instance = super(SingletonClass, cls)
        return cls._instance


# class Person1(SingletonClass):
#     def __init__(self, author):
#         self.author = author
#         super(Person1, self).__init__()
#
#
# class Person2(SingletonClass):
#     def __init__(self, author):
#         self.author = author
#         super(Person2, self).__init__()
#
# if __name__ == '__main__':
#     singleton_instance = Person1(settings.AUTHOR)
#     singleton_instance2 = Person1(settings.AUTHOR)
#
#     print(id(singleton_instance2), id(singleton_instance))
#     print(singleton_instance2 is singleton_instance)
#     print(singleton_instance2 == singleton_instance)


class SingletonObject:
    def __new__(cls, *args, **kwargs):
        # 并将一个类的实例绑定到类变量_instance上
        # 判断当前实例是否存在，如果前面已经有人实例过，则直接返回实例
        if not hasattr(cls, "_instance"):
            # 如果内存没有该实例 往下执行
            # 需要注明该父类的内存空间内最多允许相同名字子类的实例对象存在1个（不可多个）

            origin_object = super(SingletonObject, cls)  # 父类
            # origin_object让cls继承指定的父类Singleton
            cls._instance = origin_object.__new__(cls)
            # cls._instance 创建了该实例

        # 如果cls._instance不为None, 直接返回cls._instance
        return cls._instance


class Person1(SingletonObject):
    def __init__(self, name):
        self.name = name


class Person2(SingletonObject):
    def __init__(self, alias):
        self.alias = alias


if __name__ == "__main__":
    person1 = Person1(settings.AUTHOR)
    print(person1.name)  # SteveRocket
    person3 = Person1(settings.AUTHOR)
    print(person3.name)  # SteveRocket
    print(id(person1), id(person3))  # 2989265330704 2989265330704

    person3.name = "Python3.11"
    print(person1.name)  # Python3.11
    print(person3.name)  # Python3.11
    print(id(person1), id(person3))  # 2989265330704 2989265330704

    person2 = Person2("Cramer")
    print(id(person2))  # 2989264763984
    print(person2.alias)  # Cramer
    print(person1.name)  # Python3.11
