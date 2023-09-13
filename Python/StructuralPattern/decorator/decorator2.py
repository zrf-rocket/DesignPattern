import settings
class Person:
    def func1(self):
        print(f"Look at:{settings.BLOG}")

    def func2(self):
        print(f"Look at:{settings.CSDN}")

class PersonDecorator:
    def __init__(self, decorator):
        self._decorator = decorator

    def func1(self):
        print(f"My name is {settings.AUTHOR}")
        self._decorator.func1()

    def __getattr__(self, item):
        return getattr(self._decorator, item)

if __name__ == '__main__':
    person = Person()
    steverocket = PersonDecorator(person)
    steverocket.func1()
    steverocket.func2()