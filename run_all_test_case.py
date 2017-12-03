import  unittest


if __name__ == '__main__':
    #默认测试用例加载器，用于需找符合规则的测试用例
    #discover发现
    suite=unittest.defaultTestLoader.discover("./Day5", pattern='*Test.py')
    #执行suite中所有的测试用例
    #unittest.TextTestRunner文本测试用例的运行器
    #首字母大写说明他是一个类，类不能直接调用方法
    #必须要实例化对象才能调用方法
    #python中实例化不需要new关键字，直接在类后面加个（）就可以了
    unittest.TextTestRunner().run(suite)