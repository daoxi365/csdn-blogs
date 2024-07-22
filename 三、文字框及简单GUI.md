我们首先来安装`easygui模块`，打开命令提示符，输入代码：`pip3 install easygui`。
下载完成后，请往下看！
<hr>

**使用内置的文字框：**

（格式：`函数名(title='设置的标题',message='显示的信息')`）

```python
#导入需要用的模块
from tkinter.messagebox import showinfo,showwarning,showerror

'''
#导入格式：
# from 模块名 import 内容
# import 模块名
#-------------------
#推荐用第一种，因为这样节省系统资源，也方便写代码，导入多个内容时用英文逗号间隔
#第二种可以这样写：
# import 模块名 as 名称
#就是给模块起一个名字，使用时不用写完整的模块名，直接使用设定的名称即可
'''

#设置变量
title = '文字框'
msg = ['警告！病毒程序开始运行！','通知！程序正常运行！','错误！安全软件拦截！']

#我们想用警示框显示列表中第一个元素
showwarning(title,msg[0])
#我们想用通知框显示列表中第二个元素
showinfo(title,msg[1])
#我们想用错误框显示列表中第三个元素
showerror(title,msg[2])
```
这些窗口弹出时都含有声音，但是也有一个小框：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201220110553836.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
我们需要把它干掉，所以代码就变成了：

```python
from tkinter.messagebox import showinfo,showwarning,showerror
from tkinter import Tk

#设置变量
title = '文字框'
msg = ['警告！病毒程序开始运行！','通知！程序正常运行！','错误！安全软件拦截！']
window = Tk()

#不显示窗口
window.withdraw()
#我们想用警示框显示列表中第一个元素
showwarning(title,msg[0])
#我们想用通知框显示列表中第二个元素
showinfo(title,msg[1])
#我们想用错误框显示列表中第三个元素
showerror(title,msg[2])

#循环刷新
window.mainloop()
```
这样就行了。
<hr>

在这里给大家分享一个更简单的方法—— `msgbox`。
（注意，这里的格式发生变化：`msgbox('显示的内容','标题')`）

```python
#导入easygui
from easygui import msgbox

#创建变量
title = '文字框'
msg = ['警告！病毒程序开始运行！','通知！程序正常运行！','错误！安全软件拦截！']

#显示窗口
msgbox(msg[0],title)
msgbox(msg[1],title)
msgbox(msg[2],title)
```
后期我们在学习GUI模块时多给大家讲解。
<hr>
作业：

```python
1.通过easygui显示窗口，内容为“你好，世界！”，标题：“程序”。
2.通过tkinter.messagebox.showinfo()显示窗口，内容为“Hello,world!”，标题：“Program”
```

