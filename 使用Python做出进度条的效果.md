今天我们来使用Python做出**进度条**的效果。

实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200710154614923.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200710154636416.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
> 注意，这里不需要任何第三方库文件，只需要一台电脑，Windows系统，和Python3。

代码很简单，只需要**双重for循环**、**range()**。

步骤：
1.我们首先需要学会打出特殊符号：▉（完整方块，在这里直接复制即可）。
2.接着我们打开开发工具，创建一个新的、空白的Python文档。
3.输入代码如下：

```python
from time import sleep #导入sleep延时
from os import system #导入 os.system()
products = ['产品1','产品2','产品3'] #创建products列表，里面放入模拟下载的文件

#创建下载完成后函数
def isDownloadOkay(product):
	#生成VBS文本框
    with open('box.vbs','w+',encoding = 'ANSI') as file:
        #下面是一句VBS代码
        file.write('Msgbox "下载完成！"+chr(13)+"您下载的文件是：{0}",64,"通知"'.format(product))
        #下面是一句批处理命令，打开程序后延时2秒删除掉它，因为它是临时文件
    system('call "box.vbs" & ping 127.0.1 /n 2 >nul & del /q /s /f "box.vbs" >nul')

if len(products) != 0: #判断列表长度是否不等于0
	for product in products: #嵌套第一层循环
		print('正在从 Internet 上下载：{0}。\n下载进度：\n'.format(product))
		#输出信息
		for download in range(1,101): #嵌套第二层循环
			print('{0}（{1}%）'.format(download * '▉',float(download)))
			#输出进度条
			sleep(0.2)
			#延时 0.2 秒
			if download == 100:
				print('\n{0}的下载任务已经完成！\n'.format(product))
				isDownloadOkay(product = product)
else: #如果列表长度等于0
	print('您当前的产品列表长度为0，无法下载。')
	#输出信息
```
代码写完了。
有很多朋友应该会问：为啥必须要用VBS临时文件的方法而不用`tkinter.messagebox.showinfo(title,message)`呢？那样多简单，只需要一门代码就够了。其实这么做也是可以的，但是会影响效果，使用时一次会弹出两个框，效果不好。我建议大家在使用messagebox时，使用上Tk，效果不错。
![showinfo效果
](https://img-blog.csdnimg.cn/20200710130625253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

> 注：当时不太懂，后期才知道了。

