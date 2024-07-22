我们今天来写一个简单计算器。

> 这个代码不需要任何库，且只需要很少代码。

步骤：
1.打开开发工具，创建一个新的Python文档。
2.输入代码如下：

```python
while True:
	try:
		calc = eval(input('请在此处键入一个算式：'))
		print('计算结果：{0}'.format(calc))
	except ValueError:
		print('Error! Please try again!')
	except SyntaxError:
		print('Error! Please try again!')
	except TypeError:
		print('Error! Please try again!')
```
代码完成了。
可以多添加几个`except`，使代码不容易出错、报错。
最简单的代码：

```python
calc = eval(input('请在此处键入一个算式：'))
print(calc)
```

