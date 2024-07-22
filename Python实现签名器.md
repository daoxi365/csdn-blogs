在开始之前，请大家准备一些东西：
1.pygame、easygui（请大家自行下载安装`pip3 install pygame`，`pip3 install easygui`）
2.签名器预备文件（[请大家点击这里下载](https://pandaoxi2020.lanzous.com/itbLQfuneeb)）

请大家将文件下载完成后打开，解压，密码是`signer3.0`，解压完成后，打开文件夹`签名器3.0 Python\签名器3.0 Python\签名器3.0 Python\预留代码\签名器3.0 Python`。

打开开发工具，导入该项目，先看一看项目的实现效果（完整代码）：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820135431115.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2020082013545459.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820135543104.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
打开预留代码的`index.py`可以发现是一个空的文字框。
可以看到，代码注释是有的，甚至坐标都给出来了：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820135823953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
在这里考考大家，能不能按照注释内容写出来完整的代码？

**预留代码**

```python
#coding:utf-8
#导入需要用的库
import easygui,pygame
from pygame import *
#初始化pygame库
pygame.init()
#创建一个1900,740的窗口，命名为canvas
canvas = pygame.display.set_mode((1900, 740))
canvas.fill((255,255,255))
#命名窗口标题
pygame.display.set_caption("签名器3.0Python版")
#背景一图片路径："文    件/图    片/img1.jpg"
#坐标图片路径："文    件/图    片/coordinate.jpg"
#字体一图片路径："文    件/字    体/个性签.TTF"  大小50像素
#字体二图片路径："文    件/字    体/古韵签.ttf" 大小50像素
#字体三图片路径："文    件/字    体/可爱签.TTF"  大小50像素
#字体四图片路径："文    件/字    体/潇洒签.TTF"  大小50像素
#感谢字体图片路径："文    件/字    体/Thank.TTF"大小50像素








#处理关闭页面的函数
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 

#使用enterbox接受用户输入的内容，将内容存到变量里！

while True:
    #背景图片坐标：0,0
    #字体一坐标：1067,559 颜色：黑色
    #字体二坐标：405,550 颜色：黑色
    #字体三坐标：1058,275 颜色：黑色
    #字体四坐标：418,285 颜色：黑色
    #感谢字体坐标：800,444 颜色：黑色















    #调用关闭页面的函数
    handleEvent()
    #更新屏幕的内容
    pygame.display.update()
```
**完整代码**
如果大家实在不会写可以参考一下我写出来的：

```python
#coding:utf-8
import easygui,pygame
from pygame import *
pygame.init()
canvas = pygame.display.set_mode((1900, 740))
canvas.fill((255,255,255))
pygame.display.set_caption("签名器3.0Python版")
bg1=pygame.image.load("文    件/图    片/img1.jpg")
bg2=pygame.image.load("文    件/图    片/coordinate.jpg")
font1=pygame.font.Font("文    件/字    体/个性签.TTF",50)
font2=pygame.font.Font("文    件/字    体/古韵签.ttf",50)
font3=pygame.font.Font("文    件/字    体/可爱签.TTF",50)
font4=pygame.font.Font("文    件/字    体/潇洒签.TTF",50)
t=pygame.font.Font("文    件/字    体/Thank.TTF",50)
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
i=easygui.enterbox("请输入您的名字：","签名器3.0Python版")
while True:
    canvas.blit(bg1,(0,0))
    p1=font1.render(i,True,(0,0,0))
    canvas.blit(p1,(1067,559))
    p2=font2.render(i,True,(0,0,0))
    canvas.blit(p2,(405,550))
    p3=font3.render(i,True,(0,0,0))
    canvas.blit(p3,(1058,275))
    p4=font4.render(i,True,(0,0,0))
    canvas.blit(p4,(418,285))
    thank=t.render("感谢使用！",True,(0,0,0))
    canvas.blit(thank,(800,444))
    handleEvent()
    pygame.display.update()
```
您做出来了吗？
