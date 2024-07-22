今天我们使用Python来获取当前的日期和时间。

> 本次我们需要标准模块`time`。

首先让我们先理解几个单词的意思：

```
单词            翻译            缩写 
year             年              Y
month            月              m
day              日              d
hour            小时             H
minut           分钟             M
second           秒              S
```

打开开发工具，新建一个Python文档。

**输出日期**
输入代码如下：
```python
from time import strftime
print(strftime('%Y-%m-%d')
```
实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200821140306471.png#pic_center)
如果想要换种格式，可以将第二行代码改成：

```python
print(strftime('%Y/%m/%d'))
```
可见运行后效果改变了：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200821140759772.png#pic_center)

**输出时间**
输入代码如下：

```python
from time import strftime
print(strftime('%H:%M:%S'))
```
实现效果如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200821141019879.png#pic_center)

**如果同时都带上日期和时间**
输入代码如下：

```python
from time import strftime
print('日期：%s\t时间：%s' % (strftime('%Y-%m-%d'),strftime('%H:%M:%S')))
```
代码完成了！
