直接看代码：

```python
from sys import argv
argv.pop(0)
params = argv

for i in params:
	print(i)
```
这样就完成了输出参数的操作。
我们现在打开命令提示符，切换到当前目录：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210112130717334.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
输入代码：`python 文件名 你要的参数`
文件名与参数自定义，可以设置多个参数。
可以进行判断，实现命令的效果。

