```python
1.通过easygui显示窗口，内容为“你好，世界！”，标题：“程序”。
2.通过tkinter.messagebox.showinfo()显示窗口，内容为“Hello,world!”，标题：“Program”。
```

第1题：

```python
from easygui import msgbox
msgbox('你好，世界！','程序')
```

第2题：

```python
from tkinter.messagebox import showinfo

window = Tk()
window.withdraw()
showinfo('Program','Hello,world!')
window.mainloop()
```

