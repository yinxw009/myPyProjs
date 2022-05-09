class Person:                                  #1 添加类的注释

    """
    类的描述、类的作用；类的构造函数等等；类属性的描述。
    此格式(三引号对)的注释可生成项目文档
    Attributes:属性的类型、含义等
    """
    count = 1 #'#'开头的注释用于开发人员自己阅读，不生成项目文档
    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance 参数的含义，参数的类型，是否有默认值
        :step distance
        :return: 返回的结果的含义(时间)，返回数据的类型
        """
        print('人在跑')
        return distance / step

# help(Person)

__all__ = ['varIntModPub', '_varIntModPro', '__varIntModPri']
varIntModPub  = 333
_varIntModPro  = 666
__varIntModPri = 999


class Car:
    def __init__(self):
        self.color = '黑色'
    def toot(self):
        print("%s的车在鸣笛...",(self.color))

bmw = Car()
bmw.toot()