我们来写一个寻找文件的Python程序。
首先，让我们来创造一些文件：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201024184318655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201024184356501.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
如图，我们创造了很多文件，且它们都是空的。下面我们打开`python.py`，输入以下代码：

```python
#导入包
from os import walk
from os.path import splitext,join

#创建储存文件的列表
file_list = []

#遍历文件夹里的文件
for filepath,dirnames,filenames in walk(r'files'):
    #二次循环
    for filename in filenames:
        #将拓展名是 .cpp 的文件添加至列表
        if splitext(filename)[1] == '.cpp':
            file_list.append(join(filepath,filename))
        
#遍历输出列表
print('下面是文件列表：')
for i in file_list:
	print(i)

#输出一共有多少个文件
print('\n','一共有',len(file_list),'个文件！')
```
完成！
