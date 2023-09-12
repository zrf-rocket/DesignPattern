import settings
# 使用元类来实现单例模式

class SingletonMeta(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(SingletonMeta, self).__call__()
        return self._instance[self]


class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        print(f"author {settings.AUTHOR}")

    def do_something(self):
        print(f"view blog {settings.BLOG}")


if __name__ == '__main__':
    singleton_instance = SingletonClass()
    singleton_instance.do_something()

    singleton_instance2 = SingletonClass()
    singleton_instance2.do_something()

    print(id(singleton_instance2), id(singleton_instance))  # 2666431948688 2666431948688
    print(singleton_instance2 is singleton_instance) # True
    print(singleton_instance2 == singleton_instance) # True