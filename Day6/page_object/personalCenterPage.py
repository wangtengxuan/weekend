

class PersonalCenterPage:
    #网页是基于浏览器打开所以不能在一个页面中创建浏览器，应该把浏览器的使用权传进来就可以
    def __init__(self,driver):
        self.driver=driver
    title="我的会员中心 - 道e坊商城 - Powered by Haidao"