# @author:SteveRocket
# @Date:2023/9/12
# @File:pool
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
import settings


class ObjectPool:
    def __init__(self, max_objects):
        self.max_objects = max_objects
        self.objects = []

    def create_object(self):
        if len(self.objects) < self.max_objects:
            obj = Object()
            self.objects.append(obj)
            return obj
        else:
            return None

    def get_object(self):
        if len(self.objects) > 0:
            return self.objects.pop()
        else:
            return None

    def release_object(self, obj):
        self.objects.append(obj)


class Object:
    def __init__(self):
        print(f"new object {self}")

    def do_something(self):
        print(f"view blog {settings.BLOG}")


if __name__ == "__main__":
    # 使用对象池
    pool = ObjectPool(5)

    # 创建对象
    pool.create_object()
    print(len(pool.objects))  # 1
    pool.create_object()
    pool.create_object()
    print(len(pool.objects))  # 3

    # 获取对象
    obj1 = pool.get_object()
    obj2 = pool.get_object()
    print(len(pool.objects))  # 1
    # 使用对象
    if obj1:
        obj1.do_something()  # view blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q

    if obj2:
        obj2.do_something()  # view blog https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
    print(len(pool.objects))  # 1

    # 释放对象 返回对象池中
    if obj1:
        pool.release_object(obj1)

    if obj2:
        pool.release_object(obj2)

    print(len(pool.objects))  # 3
