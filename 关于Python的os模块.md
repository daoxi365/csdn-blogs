> “os模块是Python内置的模块之一，功能非常强大”。
> 我们今天来一起研究一下os模块。
> 我们需要在Windows系统上的Python3。

**1.获取当前文件位置、目录**

```python
from os.path import dirname
print('文件位置：',__file__)
print('文件所在目录：',dirname(__file__))
```

**2.获取当前路径以及切换路径**

```python
from os import getcwd,chidir
print('当前路径：',getcwd())

#切换
chidir('C:\\')
print('当前路径：',getcwd())
```

**3.重命名、删除文件**

```python
from os import rename,remove

#新建2个文件
for i in range(1,3):
	with open(str(i) + '.txt','w+') as f:
		f.write('')

#删除 1.txt
remove('1.txt')

#重命名 2.txt
rename('2.txt','被程序更改后的文件.txt')
```

**4.查看指定的路径是否存在、判断所给路径是否为一个文件或目录**

```python
from os.path import exists,isfile
print(exists('C:\\Windows'))

print(isfile('C:\\Windows\\explorer.exe')) #文件
print(isdir('C:\\Windows')) #目录
```

**5.创建目录**

```python
from os import mkdir,makedirs
makedirs('D:/01/02/03/04/05') #创建多个目录

for i in range(1,11):
	mkdir('D:/01/02/03/04/05/' + str(i))
```

**6.获取环境变量**

```python
from os.environ import items
for a,b in items():
	print(a,'----->',b)
```

**7.判断系统**

```python
from os import name

if name == 'nt':
    print('windows')
else:
    exit()
```

**8.调用命令行**

```python
from os import system
system('color 0a & echo hello,world!')
```

