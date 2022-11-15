# flake8: noqa
import pygame
import os


"""创建界面"""
WIDTH,HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("abias's world")


"""颜色设置"""
WHITE = (255,255,255)

"""帧数设置"""
FPS = 60 #每秒帧率

"""加入角色"""
#1，阿庇亚斯虫001
BUG = pygame.transform.scale()
ABIAS_BUG_IMAGE = pygame.image.load(
    os.path.join('testing','pygame001','sbug.jpg'))

SHIT_IMAGE = pygame.image.load(
    os.path.join('testing','pygame001','sshit.jpg'))

"""背景色设置函数"""
def draw_window(color):
        WIN.fill(color)
        WIN.blit(ABIAS_BUG_IMAGE,(700,200))#放置虫子位置
        WIN.blit(SHIT_IMAGE,(200,200))
        pygame.display.update()


"""事件循环"""
def main():
    tic = pygame.time.Clock()
    run = True
    while run:
        tic.tick(FPS) #循环速度
        """遍历事件列表"""
        for event in pygame.event.get():
            """关闭功能"""
            if event.type == pygame.QUIT:
                run = False
        draw_window(WHITE)


    pygame.quit()

"""确保只运行主函数，文件名/主程序入口"""
if __name__ == "__main__":
    main()