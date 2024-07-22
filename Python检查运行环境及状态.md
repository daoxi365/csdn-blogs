> 在运行程序的时候，我们必须要检查环境以及程序的状态。比如说我写了一个只可以在Windows上运行的程序，如果在Mac上运行，那是肯定不行的。如果这个程序是被调用而不是使用者自己打开，里面的一些函数可能会发生“不良反应”。今天我们来说一说怎样检查程序的状态。



首先，让我们来看`检查系统`方面的，方法有2种，哪种都可以：

```python
from platform import system
if system() == 'Windows':
	print('使用的是Windows系统！')
```
或者这样也行：

```python
from os import name
if name == 'nt':
	print('使用的是Windows系统！')
```

下面我们来说如何查看运行状态：

```python
if __name__ == '__main__':
	print('程序自主运行！')
```

我们来判断Python系统的版本：

```python
from platform import python_version
version = python_version().split('.')
if int(version[0]) >= 3 and int(version[1]) >= 6: # 如果版本低于 3.6 ，则不会显示
	print('版本是可以使用的！')
else:
	print('版本过低，请尽快更新！')
```
获取版本是32位还是64位：

```python
from platform import architecture
print(architecture()[0].split('bit')[0] + '位系统')
```

---
（额外赠送的小知识，和上面的内容没有关系）获取计算机名：

```python
from platform import node
print(node())
```


