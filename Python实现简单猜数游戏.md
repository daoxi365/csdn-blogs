我们使用Python来做一个简单猜数游戏。


>本次我们需要random随机数模块。

步骤：
1.打开开发工具，新建一个空白Python文档。
2.输入代码如下：

```python
from random import randint
number = int(input('请输入一个数字，范围在1至100之间：'))
scale = number >= 1 and number <= 100
intNumber = randint(1,100)

while scale:
	if number > intNumber:
		print('猜大了！')
		number = int(input('请输入一个数字，范围在1至100之间：'))
	elif number < intNumber:
		print('猜小了！')
		number = int(input('请输入一个数字，范围在1至100之间：'))
	
	if number == intNumber:
		print('恭喜您，猜对啦！')
		break
```
代码完成了。可以加入try except 语句，检出异常。
