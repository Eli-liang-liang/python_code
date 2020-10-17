import math
class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2) 
		

def main():
    p1 = Point(3, 5)
    p2 = Point() # 默认坐标为(0,0)
    print(p1)
    print(p2)
    p2.move_by(-1, 2) # 向左移动1格，向上移动2个
    print(p1.distance_to(p2)) # 计算p1和p2的距离
    # 自行计算p1 和 p2的距离，并验证正确性


main()