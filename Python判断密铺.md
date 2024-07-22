埃舍尔密铺是小学必须掌握的一项内容，根据我的整理，求内角和的公式是：`多边形内角和=180°×(n-2)`，密铺是`取余2n÷(n-2)=0`。我们打开编辑器，输入以下代码：

```python
while True:
	try:
		sides = int(input('请输入您要查询的多边形边数：'))
		figure_sum = 180 * (sides - 2)
		canTessellation = (2 * sides / (sides - 2)) % 1 == 0
		if canTessellation == True and sides >= 3:
			types = '可以密铺'
		else:
			types = '不能密铺'
		print('%d边形的内角和是%d°\n这种图形%s！\n' % (sides,figure_sum,types))
	except Exception as e:
		print('\n遇到错误：',e,'\n')
```
这样，我们的代码就完成了。
