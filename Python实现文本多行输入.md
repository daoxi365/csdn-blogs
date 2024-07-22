> 我们都知道，Python内置方法input只能输入一行内容，我们今天实现嵌套while循环来实现输入多行文本功能。
我们本次不需要任何库。

步骤：
1.打开开发工具，创建一个新Python文档。
2.输入代码如下：

```python
#创建空列表储存多行输入信息
textList = []
#创建关键字变量
keywords = '__end__'
#打印文字信息
print('文字多行输入，输入“{0}”即可停止。\n请在下方输入内容。\n'.format(keywords))
#嵌套循环
while True:
	#声明变量来储存输入信息
	text = input()
	#判断输入信息是否为结束输入的关键字
	if text == keywords:
		#跳出循环
		break
	else: #如果不是就添加到列表
		textList.append(text)

#打印输入的内容
for i in textList:
	print(i)
```
代码完成了。实现效果：
![图片](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200728140137286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![图片](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200728140213427.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

