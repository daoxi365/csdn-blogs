啊，为此我特意准备了两个程序，一个是用来测试的，一个是主程序。来看看吧

直接放连点器代码：

```python
# 改进版
import pyautogui as pag
from time import sleep,time

pag.PAUSE = 0
def mouse():
    b = input('请问您需要点击多少下？')
    b = int(b)
    c = input('点击时需要左键还是右键？\n左键请输入0，右键输入1：')
    c = int(c)
    print('请注意：您需要在8秒内将鼠标移动到您需要连点的地方，然后不要动，等待开始快速连点。')
    sleep(8)
    print('开始点击！')
    x,y = pag.position()
    d = 'left'
    if c:
        d = 'right'
    e = time()
    for i in range(0,b):
        pag.click(x,y,button = d)
    f = time() - e
    input('完成。用时%f秒。' % f)

def key():
    print('请在以下支持的按键中挑选您需要的键。')
    for i in pag.KEYBOARD_KEYS:
        print(r'%s' % i,end=' ')
    b = input('\n请输入您需要快速输入的字符：')
    if b in pag.KEYBOARD_KEYS:
        c = input('请输入您需要多少次输入：')
        c = int(c)
        print('请注意，您需要在8秒内切换到需要输入的窗口。')
        sleep(8)
        print('开始工作！')
        e = time()
        for i in range(0,c):
            pag.press(b)
        f = time() - e
        input('完成。用时%f秒。' % f)
    else:
        input('您输入的字符不属于支持字符，请修改。')    
    
try:
    a = input('输入您需要的服务（数字）：\n1:快速连点\n2:快速输入\n>>> ')
    a = int(a)
    if a == 1:
        mouse()
    elif a == 2:
        key()
    else:
        input('不好意思，没有找到您需要的服务。\n')
except Exception as e:
    print('错误；\n',e)
```
测试程序：

```python
import pygame
from pygame.locals import *
from pygame.color import THECOLORS

pygame.init()
canvas = pygame.display.set_mode((600,600))
canvas.fill((255,255,255))
pygame.display.set_caption('TEST')

# 鼠标点击次数
mouBut = 0
# 空格键按下次数
keyDow = 0

def handle():
    global mouBut,keyDow
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # 当按下鼠标
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            # 且在黑色矩形内
            if 200 <= x <= 400 and 200 <= y <= 400:
                mouBut += 1
        # 当按下键盘
        if event.type == KEYDOWN:
            # 且为空格键
            if event.key == K_SPACE:
                keyDow += 1

while True:
    # 每次重绘背景
    canvas.fill((255,255,255))
    # 鼠标测试，绘制矩形
    pygame.draw.rect(canvas,(0,0,0),(200,200,200,200),0)
    # 绘制文字
    font1 = pygame.font.SysFont('Consolas',30)
    font2 = font3 = font4 = font5 = font6 = font1
    canvas.blit(font1.render('MouseButtonDown:%d' % mouBut,True,(0,0,0)),(10,10))
    canvas.blit(font2.render('KeyDown:%d' % keyDow,True,(0,0,0)),(10,50))
    canvas.blit(font3.render('CLICK ME!',True,(255,255,255)),(225,275))
    canvas.blit(font4.render('Click the black rectangle or press',True,(255,0,0)),(10,100))
    canvas.blit(font5.render('the spacebar!',True,(255,0,0)),(10,150))    
    canvas.blit(font6.render('By PanDaoxi',True,(0,0,255)),(200,500))
    handle()
    pygame.display.update()
```

由于发懒，没仔细做主程序GUI。运行测试程序然后再打开主程序，一旦打开程序的时候手残，就会凉凉。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8256eb816451409dbe5839f31d81c9f4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
在连点模式下，
我给程序设定了8秒的等待时间，这8秒内，你需要**打开测试程序，并把鼠标放在需要点的地方。**

程序会询问你一些参数，![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3498137681e5492f9d0cbdc9991cfef9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
直接回答即可。如图，按下回车键后，就开始等待那8秒，然后连点了。在此之前，我们看一下测试程序：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8db4691bdb294b579b53ae8f85561dfb.png)
点击后，
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a05a88155a49446eacef018027afe1ed.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
程序点击很快，一下子点完。我用改进版试一下1000次。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b2c83a5ff73f476899def3108aaadd04.png)


再试试快速输入，也是很快，用命令提示符试就行，这个测试程序是针对物理键盘的。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ee10ac45e6de41d18331f77c775184f6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/188cedb564aa4f91bfc2c55849fc6c66.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
突然一下，多了10个。因为数太小，所以被忽略不计，试试1000.![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/df948b6df625400d9298d7ba82cb0d3a.png)

