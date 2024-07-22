> 今天我们来用Python输出列表中的信息。
> 不用任何第三方和标准库。

我们输出的要求是：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2020082013224888.png#pic_center)
**在同一行内，隔两个空格再写内容！**

步骤：
1.打开开发工具，新建一个Python文档，输入代码如下：

```python
#首先声明一个列表
names = ['Python','C/C++','PHP','Java/JavaScript','C#','汇编','Shell','ActionScript','VbScript']

#方法一：直接输出里面的内容
print(names[0],' ',names[1],' ',names[2],' ',names[3],' ',names[4],' ',names[5],' ')
#缺点：很麻烦
print(names)
#缺点：不是想要的格式

#方法二：切片
print(names[0:6])
#优点：代码少
#缺点：不是想要的格式

#方法三：while循环、len()
record = 0
while record <= len(names) - 1:
	print(names[record],end = '  ')
	record += 1
#优点：实现了效果，运行完全正确
#缺点：代码量太大了，效率低

#方法四：range()、len()
for i in range(0,len(names) - 1):
	print(names[i],end = '  ')
#优点：实现了效果，运行完全正确，代码少
#缺点：逻辑容易搞不清，代码量还能更少

#方法五：遍历迭代
for i in names:
	print(i,end = '  ')
#优点：实现了效果，运行完全正确，代码极少
#缺点：无
```
我个人比较推荐使用`for ... in ...`循环，承包了所有优点！
当使用死循环时可以使用`while`循环：

```python
record = 0
while True:
    print('这是一个死循环，运行已经%s次了！' % (record))
    record += 1
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820133557148.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)

