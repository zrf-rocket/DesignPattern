import settings


class Factory:
    def look(self):
        raise NotImplementedError


class LookCSDN(Factory):
    def look(self):
        print(f"look at {settings.CSDN}")


class LookWeChat(Factory):
    def look(self):
        print(f"look at {settings.BLOG}")


class LookFactory:
    """
    工厂模式：暴露给用户去调用的，用户可通过该类进行选择Look的子类进行实例化
    """

    @staticmethod
    def look_at(addr):
        if addr == "csdn":
            return LookCSDN()
        elif addr == "wechat":
            return LookWeChat()


if __name__ == "__main__":
    # 先实例化工厂类 然后 实例化子类 最后调用工厂方法
    LookFactory.look_at("csdn").look()  # look at https://blog.csdn.net/zhouruifu2015/
    LookFactory.look_at(
        "wechat"
    ).look()  # look at https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
