```python
练习题
使用课中所介绍的同样的方法，在page2.py中，绘制图片./images/start page/bg2.jpg。
```

```python
#导入包
import pygame
from pygame.locals import *
from sys import exit

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

#设定循环
while True:
    canvas.blit(image2,(0,0))
    event()
    pygame.display.update() #更新窗口
```

