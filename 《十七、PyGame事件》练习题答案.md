```python
练习题
使用同样的方法，将 page2.py 中也添加上点击按钮进入到 game.py 文件。
注：按钮区域坐标不变。
```

```python
#导入包
import pygame
from pygame.locals import *
from sys import exit
from os import system,remove
from os.path import exists

#创建一个窗口
pygame.init() #初始化窗口
canvas = pygame.display.set_mode((1000,600)) #新建一个长1000像素，宽600像素的窗口
canvas.fill((255,255,255)) #填充白色，中间是RGB值
pygame.display.set_caption('抗击病毒') #窗口标题

#导入图片
image2 = pygame.image.load('./images/start page/bg2.jpg')

#处理事件函数
def event():
    for event in pygame.event.get(): #遍历窗口的事件
        if event.type == QUIT: #如果是退出事件
            pygame.quit() #关闭窗口
            exit() #退出程序
        if event.type == MOUSEBUTTONDOWN: #如果是鼠标按下事件
            if event.button == 1: #如果是左键
                pos = event.pos #获取鼠标的位置
                mouseX = pos[0] # X坐标
                mouseY = pos[1] # Y坐标
                if 650 <= mouseX <= 990 and 510 <= mouseY <= 585: #如果点击区域是按钮
                    pygame.quit() #关闭当前PyGame窗口
                    with open('START.txt','w+') as f: #生成一个空白文件 START.txt
                        f.write('') #内容为空
                    system('python "game.py"') #打开 page2.py 文件

#设定循环
while True:
    canvas.blit(image2,(0,0))
    event()
    pygame.display.update() #更新窗口
```

