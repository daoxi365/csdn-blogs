我们来写一个Python输出乘法表的效果。

> 这次也不需要任何库。

步骤：
1.打开开发工具，创建一个新Python文档。
2.输入代码如下：

```python
#双重for循环
for o in range(1,10): #嵌套第一个循环
	for t in range(1,o+1): #嵌套第二个循环
		print('{0}×{1}={2}'.format(o,t,o * t),end = '')
		#输出信息
		#可以用格式化字符串，也可以用强转：%s .format +str()
	print() #换行
```
代码完成了。

