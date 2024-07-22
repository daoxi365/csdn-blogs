今天我们来认识一门新的编程语言——vbs。（**[点击这里查看百科](https://baike.so.com/doc/4934679-5155117.html)**）
打开记事本，我们先来写一个简单的vbs程序来认识一下它：

```vbnet
Msgbox "Hello,World!",64,"box"
```
[（文字框的百科点这里）](https://baike.so.com/doc/6726208-6940452.html)
`^S`保存，**编码格式为`ANSI`**，保存类型为`所有文件`，命名为`Hello,World.vbs`，保存到桌面。
双击打开它以后会出现一个文字框，上面写着`Hello,World!`字样。

可以嵌套一个循环，就成了恶搞了，请看下面代码（无尽循环，除非用`taskkill /im wscript.exe /f`没有办法关掉，慎用）：

```vbnet
do
Msgbox "You are fool!",64,"warning"
loop
```

这种文字框就是Python的这种效果：
```python
from tkinter import Tk
from tkinter.messagebox import showinfo
window = Tk()
window.withdraw()
showinfo('box','Hello,World!')
window.mainloop()
```

vbs让电脑说话的代码是：

```vbnet
set sapi = CreateObject("SaPi.SpVoice")
sapi.Speak "hello,world!"
```
一定要注意保存的时候要把编码格式改成`ANSI`，否则就报错了！

**下面开始写代码！**

> 本次我们需要`easygui`库，需要自己下载安装，命令`pip3 install easygui`，帮助手册参考这篇优秀文章，[点击这里查看](https://www.cnblogs.com/bldly1989/p/6651855.html)。

还是老规矩，打开开发工具，新建一个空白的Python文档，输入以下内容：

```python
# 导入包
from os import system

def say(text): #创建say方法
	with open('say.vbs','w+',encoding = 'ANSI') as file: #创建文件
		file.write('set sapi = CreateObject("SaPi.SpVoice")\nsapi.Speak "%s"' % (strtext)) #写入代码
	system('call "say.vbs" & del /q /s /f "say.vbs" >nul') # 打开文件，删除文件

#调用
say('你好呀！')
say('我是一个vbs程序，我还能说英语！信不信？')
```
代码完成了，如果大家对这门代码感兴趣，那么请自行百度搜索学习！
