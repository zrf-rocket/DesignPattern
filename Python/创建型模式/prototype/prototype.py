# @author:SteveRocket 
# @Date:2023/9/11
# @File:prototype
# @Email:rocket_2014@126.com
# @CSDN:https://blog.csdn.net/zhouruifu2015/
# @WeChat:https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
import settings
import copy


class Prototype:
    def __init__(self):
        print(f"view {settings.BLOG}")

    def clone(self):
        pass


class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


# 创建原型对象
prototype = ConcretePrototype(settings.AUTHOR)

# 克隆原型对象
clone01 = prototype.clone()
print(clone01.name)  # SteveRocket

clone02 = prototype.clone()
print(clone02.name)  # SteveRocket
print(id(clone01), id(clone02))  # 2520871297184 2520871614256
