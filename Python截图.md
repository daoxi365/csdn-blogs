> 我们用到了第三方模块`pyautogui`，请提前安装。

直接看代码：

```python
from pyautogui import screenshot
from tkinter import Tk
from time import strftime

window = Tk()
window.withdraw()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

image = screenshot(region = (0,0,width,height)) #前两个是起始x和y，后两个是终止x和y，这里表示截全屏的图
image.save('./screenshot.png')

window.mainloop()
```

（截取效果）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210219115901113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

