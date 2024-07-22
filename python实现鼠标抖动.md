```python
from random import randint
from pyautogui import position,moveTo,size,FAILSAFE

FAILSAFE = False
sX,sY = size()
while True:
    try:
        x,y = position()
        if x <= sX and y <= sY:
            newX = eval('%d %s %d' % (x,['+','-'][randint(0,1)],randint(1,12)))
            newY = eval('%d %s %d' % (y,['+','-'][randint(0,1)],randint(1,12)))
            moveTo(newX,newY)
        else:
            moveTo(0,0)
    except:
        pass
```
运行后，鼠标开始无规律的抖动，点关闭程序的按钮都有点困难。主要就是随机数的知识。

这里用到了一个`eval`语句，帮助我们合成算式，再将鼠标移动到结果的位置。

您也可以自己设定抖动幅度。
