我们上一次用进度条表示模拟下载，这一次就来一个真的下载。

> 我们这一次需要用到第三方库：requests

步骤：
1.WIN+R唤出“运行”，输入“cmd.exe”。
2.打开小黑框cmd.exe后输入：`pip3 install requests`。
3.等待下载完成后关闭cmd.exe。
4.打开开发工具，创建一个新的空白的Python文档。
5.输入代码如下：

```python
from requests import get #导入 requests.get()
def download(url,name): #创建 download 函数
	get = get(url) #获取 url 参数
	#下面开始对文件进行写入
	with open(name,'wb') as download:
		download.write(get.content)

#调用 download 函数
download(url = 'https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe',name = 'python-3.8.3.exe')
```
代码完成了。

实现效果：
等待一会后，在当前文件夹会出现“python-3.8.3.exe”这个文件，这是从官网上下载的。如果想要将文件移动到指定位置，代码可以这么写：

```python
from os import mkdir,system
from requests import get

def move(folder,name):
	try:
		mkdir(folder)
		system('move "{0}" "{1}"'.format(name,folder))
	except FileExistsError:
		pass
		
def download(url,name,folder = 'D:/download files'):
	get = get(url)
	with open(name,'wb') as download:
		download.write(get.content)
	move(folder = folder,name = name)

download(url = 'https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe',name = 'python-3.8.3.exe')
```

