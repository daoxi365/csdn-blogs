我们的新课即将开始，请大家先下载[课程文件](https://pandaoxi2020.lanzous.com/b01c2eofe)，下载密码是`study`。可以打开完整版看一下效果。

[video(video-guoWJ0no-1611804357132)(type-tencent)(url-https://v.qq.com/txp/iframe/player.html?vid=k32242adf8y)(image-http://puui.qpic.cn/vpic/0/k32242adf8y.png/0)(title-《十六、PyGame显示图片》)]

<hr>

# `PyGame`窗口
我们后期做游戏都需要这个库，它专门用来开发游戏，里面有很多内容。
## 如何创建一个窗口呢？
我们打开待完成文件夹中的`page1.py`，书写代码如下：

```python
#导入包
import pygame
from pygame.locals import *

#创建一个窗口
pygame.init() #初始化窗口
canvas = pygame.display.set_mode((1000,600)) #新建一个长1000像素，宽600像素的窗口
canvas.fill((255,255,255)) #填充白色，中间是RGB值
pygame.display.set_caption('抗击病毒') #窗口标题

#设定循环
while True:
    pygame.display.update() #更新窗口
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210128112642784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
我们发现无法关闭窗口。这是因为我们并没有给定程序，如果点击右上角的`×`，该如何处置，所以我们的代码变更为：

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

#处理事件函数
def event():
    for event in pygame.event.get(): #遍历窗口的事件
        if event.type == QUIT: #如果是退出事件
            pygame.quit() #关闭窗口
            exit() #退出程序

#设定循环
while True:
    event()
    pygame.display.update() #更新窗口
```
这样就可以退出了。
## 如何添加图片？
我们的窗口现在是空白的，我们要添加一张图片，该如何添加呢？
这时候，需要我们使用`窗口对象.blit(图片对象,(X坐标,Y坐标))`来解决了。程序里的坐标是指**直角坐标系**，我们通过一个平面上的横和纵两个方面，来确定一个东西的位置。这个坐标以它的**左上角**为参照，即窗口左上角坐标为`(0,0)`。

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
image1 = pygame.image.load('./images/start page/bg1.jpg')

#处理事件函数
def event():
    for event in pygame.event.get(): #遍历窗口的事件
        if event.type == QUIT: #如果是退出事件
            pygame.quit() #关闭窗口
            exit() #退出程序

#设定循环
while True:
    canvas.blit(image1,(0,0)) #绘制图片
    event()
    pygame.display.update() #更新窗口
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210128113534671.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
我们后期会学到更多的事件，今天就先说这么多，来看下练习题吧！
<hr>

```python
练习题
使用课中所介绍的同样的方法，在page2.py中，绘制图片./images/start page/bg2.jpg。
```

