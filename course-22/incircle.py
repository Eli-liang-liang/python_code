class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def getCenter(self):
        return self.center
    def getRadius(self):
        return self.radius
    def setCenter(self, circle_x, circle_y):
        self.center = (circle_x, circle_y)
    def setRadius(self, radius):
        self.radius = radius
    def isInside(circle_x, circle_y, rad, x, y): 
        if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= radius * radius): 
            print("在圆内")
        else: 
            print("在圆外")
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
		
point1 = Point(1,2)
point2 = Point(5,2)

circle1 = Circle(point1,5) # 该圆的圆心坐标为(1,2)，半径为5
circle2 = Circle(point2,1) # 该圆的圆心坐标位(5,2)，半径为1

point3 = Point(1,4)
circle1.isInside(point3) # point3在圆circle1里面，print "在圆内"
circle2.isInside(point3) # point3在圆circle2外，print "在圆外"

circle1.isInside(Point(6,2)) # （6,2) 在圆circle1上面，print "在圆上"