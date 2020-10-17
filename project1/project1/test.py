import sys
import pygame
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 设置窗口分辨率的大小
    screen = pygame.display.set_mode((1200, 800))
    # 设置窗口的标题
    pygame.display.set_caption("Alien Invasion")

    bg_color = (255, 0, 0)


    # 加载ship图片
    ship_image = pygame.image.load('images/ship.bmp')
    # 获取表示ship位置的坐标对
    ship_rect = ship_image.get_rect()
    # 获取屏幕信息
    screen_rect = screen.get_rect()
    # 设置ship中间的x处于屏幕中间
    ship_rect.centerx = screen_rect.centerx
    # 设置ship底部处于屏幕底部
    ship_rect.bottom = screen_rect.bottom

    ship_go_up = False
    ship_go_down = False
    ship_go_left = False
    ship_go_right = False
    speed = 10 
    # 开始游戏的主循环
    while True:
    	# 监视键盘和鼠标事件
        for event in pygame.event.get():
            # if ship_rect.bottom > 800 or ship_rect.bottom < 0 or ship_rect.centerx > 1200 or ship_rect.centerx < 0:
            #     continue
            # else:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("detect key!!")
                if event.key == pygame.K_s:
                    speed += 20
                    print("more speed")
                elif event.key == pygame.K_d:
                    speed -= 20
                    if (speed < 0):
                        speed = 1
                    print("less speed")
                if event.key == pygame.K_DOWN:
                    print("go down!!")
                    ship_go_down = True
                if event.key == pygame.K_RIGHT:
                    print("go right!!")
                    ship_go_right = True
                if event.key == pygame.K_UP:
                    print("go up!!")
                    ship_go_up = True
                if event.key == pygame.K_LEFT:
                    print("go left!!")
                    ship_go_left = True
            elif event.type == pygame.KEYUP:
                    ship_go_up = False
                    ship_go_down = False
                    ship_go_left = False
                    ship_go_right = False
        if ship_go_up == True:
            ship_rect.bottom -= speed
            if ship_rect.bottom < 10:
                ship_rect.bottom = 10
        if ship_go_down == True:
            ship_rect.bottom += speed
            if ship_rect.bottom > 800:
                ship_rect.bottom = 800
        if ship_go_left == True:
            ship_rect.centerx -= speed
            if ship_rect.centerx < 0:
                ship_rect.centerx = 0
        if ship_go_right == True:
            ship_rect.centerx += speed
            if ship_rect.centerx > 1200:
                ship_rect.centerx = 1200
                    
        # 每次循环都会重新绘制屏幕
        # 绘制背景颜色
        screen.fill(bg_color)
        # 绘制ship
        screen.blit(ship_image, ship_rect)
        # 让最近绘制的屏幕可见
        pygame.display.flip()
# 调用函数
run_game()