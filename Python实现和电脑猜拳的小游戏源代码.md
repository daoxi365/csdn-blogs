和小伙伴玩时，我们经常会用到猜拳来决定谁来表演节目。我们今天来写一个和电脑玩猜拳的程序，话不多说，直接看代码：

```python
import random
num = 1
yin_num = 0
shu_num = 0
while num <= 100:
    if shu_num == 2 or yin_num == 2:
        break
    user = int(input('请出拳 0（石头） 1（剪刀） 2（布）：'))
    if user > 2:
        print('不能出大于2的值')
    else:
        data = ['石头', '剪刀', '布']
        com = random.randint(0, 2)
        print("您出的是{}，电脑出的是{}".format(data[user], data[com]))
        if user == com:
            print('平局')
            continue
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0):
            print('恭喜您，您获胜了！')
            yin_num += 1
        else:
            print('不好意思，您输了。下次走远！')
            shu_num += 1
    num += 1

```
代码完成了！
