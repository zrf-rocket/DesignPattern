import settings
import copy


class Object1:
    def __init__(self):
        self.age = settings.AGE
        self.author = settings.AUTHOR


class Object2(Object1):
    def __init__(self):
        Object1.__init__(self)
        self.blog = settings.BLOG

    def __str__(self):
        return "{}, {}, {}".format(self.age, self.author, self.blog)


if __name__ == "__main__":
    obj1 = Object2()
    obj2 = copy.deepcopy(obj1)
    obj3 = Object2()

    print(id(obj1), id(obj2), id(obj3))  # 2187342458320 2187342452880 2186779985616
    print(
        [str(i) for i in (obj1, obj2)]
    )  # ['28, SteveRocket, https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q', '28, SteveRocket, https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q']
    for i in (obj1, obj2, obj3):
        print(i)  # 28, SteveRocket, https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
    print(
        [i for i in (obj1, obj2)]
    )  # [<__main__.Object2 object at 0x000001FD47C52DD0>, <__main__.Object2 object at 0x000001FD47C51890>]
