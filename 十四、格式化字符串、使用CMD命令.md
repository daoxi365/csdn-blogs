## 第一部分：格式化字符串
一直使用字符串拼接符是不是很麻烦？学了今天这课，你会觉得轻松百倍！
# ①使用`%s`、`%d`、`%f`

> %s 指 字符串，是将字符串插入字符串。
> %d 指 整数类型，是将整数改为字符串再插入。
> %f  指 浮点数类型，将浮点数改为字符串再插入。

我们来看下语法格式：
`'%s，%d，%f' % ('str','int','float')` 
字符串内怎么写，我一律不管了，只要插入就得与字符串外`%`后面的内容对应。

```python
print('Hello,%s!' % (input('Your Name:')))
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210126112150495.png)
## ②使用`字符串.format()`
在字符串内插入几个大括号`{}`，字符串格式化也可以这样写：

`'{0}{1}{2}'.format('str1','str2','str3')`
里面的数字用于指定`format`中格式化字符的位置，可以这样写：

```python
s1 = 'hello'
s2 = 'world'

#通过位置访问
print('{1} {0}'.format(s1,s2))
print('{0} {1}'.format(s1,s2))

#或者通过关键字也可以访问
print('{hello} {world}'.format(hello = s1,world = s2))
```

## 二、第二部分：使用`CMD`命令
我们如何在一种语言中使用另一种语言？我们今天要使用`os.system()`，如果电脑不是`Windows`系统，代码是无效的。
<hr>
我们先导入：

```python
from os import system
```
我们直接调用，括号里面放命令，前缀是`r`，因为路径的间隔符是`\`，为了避免被编译器识别成需要转义，加上这个前缀。

```python
system(r'dir /s "C:\"')
```
这样就可以看到“跑目录”了。
<hr>

打开另一个文件的命令是什么？请看：
`python 文件名`
我们直接敲代码：

```python
system(r'python "01.py"')
```
可能因为没有这个文件，无法使用，但是是可以使用的。

<hr>

```python
练习题
调整窗口颜色为0A，命令为color 0A。
```

