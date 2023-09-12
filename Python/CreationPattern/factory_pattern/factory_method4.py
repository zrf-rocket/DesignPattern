import settings


class Factory:
    """工厂类"""

    def get_article(self):
        return self.article_addr


class GIT(Factory):
    def __init__(self):
        self.article_addr = settings.GIT

    def article(self):
        print("Gitee")


class WECHAT(Factory):
    def __init__(self):
        self.article_addr = settings.BLOG

    def article(self):
        print("WeChat")


class ArticleInterfaceFactory:
    """
    接口基类
    """

    def create(self):
        """把要创建的工厂对象装配进来"""
        raise NotImplementedError


class ArticleGit(ArticleInterfaceFactory):
    def create(self):
        return GIT()


class ArticleWeChat(ArticleInterfaceFactory):
    def create(self):
        return WECHAT()


if __name__ == "__main__":
    git_interface = ArticleGit()
    git_obj = git_interface.create()
    git_obj.article()  # Gitee
    print(git_obj.get_article())  # https://gitee.com/SteveRocket

    wechat_interface = ArticleWeChat()
    wechat_obj = wechat_interface.create()
    wechat_obj.article()  # WeChat
    print(wechat_obj.get_article())  # https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q
