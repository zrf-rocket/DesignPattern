# @author:SteveRocket 
# @Date:2023/9/11
# @File:prototype02
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
import copy
import settings


class Prototype:
    def __init__(self):
        print(f"view {settings.BLOG}")
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Person:
    def __str__(self):
        return f"{settings.AUTHOR}"


person = Person()
prototype = Prototype()
prototype.register_object('person', person)
b = prototype.clone('person', a=11, b=22, c=33, blog=settings.BLOG)
print(person)
print(b.__dict__)
print(b.a, b.b, b.c, b.blog)
