小学四年级的教材中，有一个叫做“质数”的东西。至于质数是什么，自己百度搜索。
今天写代码我们来输出指定数一下的质数。

> 本次我们不需要准备任何库！

实现效果如下：
![效果图](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200710170428918.png)
![效果图
](https://img-blog.csdnimg.cn/20200710170612601.png)
步骤：
1.打开开发工具，新建一个空白Python文件。
2.输入代码：

```python
#创建prime函数，里面有一个参数maxNumber
def prime(maxNumber):
	#创建所需变量
    list = []
    min = 2
    #嵌套循环
    while min <= maxNumber:
    	#创建新开关
        is_prime = True
        #嵌套第二层循环，这里不再细说
        for i in range(2,min):
            if (min % i) == 0:
                is_prime = False
                break
        #判断开关是否为True
        if is_prime == True:
            list.append(min)
        min += 1
    #输出列表
    print('{0} 以下的质数有：'.format(maxNumber))
    print(list)
    print()

#调用函数，别忘了里面要传入参数
prime(50)
prime(30)
```
代码完成了。
注：可以用这种方式，也可以用双重for循环，输出的方法不唯一。

