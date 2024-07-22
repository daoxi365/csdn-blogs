> 本次我们需要使用`pyinstaller`工具，请使用`pip3 install pyinstaller`来安装。
> 还需要`easygui`模块，使用同样方法安装。

我们安装成功后，制作一个简单的小游戏：

```python
from random import randint
from easygui import msgbox,integerbox

secret = randint(1,100)
title = '猜数字'
tries = 0
msgbox('现在开始猜数字，数字的范围是1-100！',title)
temp = integerbox("请输入一个数字：",title)
guess = int(temp)

if guess == secret:   
    msgbox("恭喜你一次就猜对了！",title)   
else:
    if guess < secret:  
        msgbox("猜小了！",title)  
    else:
        msgbox("猜大了！",title) 

while guess != secret and tries < 15:
	temp = integerbox("猜错了，重新猜猜吧：",title)
	guess = int(temp)
	tries += 1
	if guess == secret:
		msgbox("恭喜您，猜对啦！",title)
	else:
		if guess < secret:
			msgbox("猜小了！",title)
		else:
			msgbox('猜大了！',title)
	while tries >=5:
		msgbox("没有机会了！",title)
		break
msgbox("哈哈，正确数字是" + str(secret) + '！',title)
```
这是一个猜数游戏。我们把它放在一个文件夹下，命名为`guess.py`。可以先看一下实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212336854.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212418386.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212432142.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
……
效果就先不说了。打开命令提示符，切换到当前目录：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212616990.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
输入以下代码：

```
pyinstaller guess.py -F -w
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212732483.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
然后点回车键，发生了以下的事情：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212843585.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212848116.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
当看到语句`Building EXE from EXE-00.toc completed successfully.`时，那么我们就成功了！看一下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214212948661.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
我们的文件夹里多了很多文件，可执行文件在`dist`文件夹里：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201214213037119.png)
效果和运行程序一模一样！
