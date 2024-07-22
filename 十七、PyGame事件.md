> 我们昨天在窗口上绘制了一张图片，今天我们来完善一下**游戏的引入**功能。

我们发现，昨天我们绘制的一张图片右下角有一个按钮，当玩家点击按钮时，我们切换到另一个文件。可是我们昨天发现点击按钮是没有效果的，今天我们就来完善这个功能。

<hr>

# 事件都有哪些？
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210129111035214.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
（表格来自：[《PyGame事件》](https://blog.csdn.net/Hubz131/article/details/86718684)）


<hr>

# 我们在哪写代码？

今天我们要在`event`函数内写一些代码，在开头写一些代码。

<hr>

# 开始写吧！

## 在`event`函数内，添加一个判断事件的语句
我们找到`event`函数，没有改以前是这样：
```python
#处理事件函数
def event():
    for event in pygame.event.get(): #遍历窗口的事件
        if event.type == QUIT: #如果是退出事件
            pygame.quit() #关闭窗口
            exit() #退出程序
```
现在，我们要在循环内加一个判断，如果发生了鼠标按下事件……

```python
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
                    with open('start.txt','w+') as f: #生成一个空白文件 start.txt
                        f.write('') #内容为空
                    system('python "page2.py"') #打开 page2.py 文件
```
可能大家对`650 <= mouseX <= 990 and 510 <= mouseY <= 585`这个表达式有一些不明白，请看图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210129112634504.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

嘿嘿，好理解不？

## 在开头判断是否有这个文件
这一次我们要打开`page2.py`，在昨天练习题的基础上，在`导入图片`注释的上方，写入代码：
```python
if not exists('start.txt'): #如果不存在这个文件
    pygame.quit() #关闭窗口
    system('python "抗击病毒.py"') #回到主程序文件
else: #如果存在（即通过 page1.py 文件调用命令打开）
    remove('start.txt') #删除文件
```
先别着急运行，在文件开头`导入包`时，上面写这两行代码：

```python
from os import system,remove
from os.path import exists
```
在`page1.py`中，也添加上，再运行`page1.py`，点击下面的按钮，就可以打开`page2.py`了。如果我们直接打开`page2.py`，那么就会回到主程序文件，即`抗击病毒.py`。

<hr>

```python
练习题
使用同样的方法，将 page2.py 中也添加上点击按钮进入到 game.py 文件。
注：按钮区域坐标不变。
```

