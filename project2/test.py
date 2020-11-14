import pygame
import random
from random import randint

from math import sqrt

def positive_or_negative():
    if random.random() < 0.5:
        return 1
    else:
        return -1

class Ball(object):
    """球"""

    def __init__(self, x, y, radius, color):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = randint(1, 9)
        self.sy = int(sqrt(100 - self.sx * self.sx))
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += int(self.sx * (100/self.radius))
        self.y += int(self.sy * (100/self.radius))
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def my_move_right(self, screen):
        self.x += int(self.sx * (100/self.radius))


    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)





def main():
    # 定义用来装所有球的容器
    myball = Ball(100, 100,50,(0,0,225))
    # myball = Ball(100, 100,50,50,50,(0,0,225))
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    myball.draw(screen)
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = (255,0,0)
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, color)
                # ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("go right")
                    # myball.x += myball.sx
                    myball.my_move_right(screen)
                elif event.key == pygame.K_LEFT:
                    print("gp left")
                    myball.x -= myball.sx
                elif event.key == pygame.K_UP:
                    print("go up")
                    myball.y -= myball.sy
                elif event.key == pygame.K_DOWN:
                    print("gp down")
                    myball.y += myball.sy
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        if myball.alive == True:
            myball.draw(screen)
        for i in balls:
            if i.alive == True:
                i.draw(screen)
            else:
                balls.remove(i)

        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)

        for ball in balls:
            myball.eat(ball)
            ball.eat(myball)


        


if __name__ == '__main__':
    main()