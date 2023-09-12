import settings

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class SingletonClass:
    def __init__(self):
        print(f"Hello {settings.AUTHOR}")

    def do_something(self):
        print(f"view blog {settings.BLOG}")


if __name__ == '__main__':
    singleton_instance = SingletonClass()
    singleton_instance.do_something()

    singleton_instance2 = SingletonClass()

    print(id(singleton_instance), id(singleton_instance2)) # 3012423703568 3012423703568
    print(singleton_instance is singleton_instance2)  # True