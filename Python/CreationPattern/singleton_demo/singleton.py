import settings

class SingletonClass:
    def __init__(self):
        print(f"author:{settings.AUTHOR}")

    def do_something(self):
        print(f"view {settings.BLOG}")


singleton_instance = SingletonClass()