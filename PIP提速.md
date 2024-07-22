我们打开一个路径：`%USERPROFILE%`，找到文件夹中名为`pip`的文件夹，如果没有，那就新建一个文件夹。

我们进入这个文件夹，创建一个文件：`pip.txt`，输入以下代码：

```python
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```
或

```python
[global]
index-url=http://mirrors.aliyun.com/pypi/simple

[install]
trusted-host=mirrors.aliyun.com
```

我们重命名这个文件为`pip.ini`。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210208184808608.png)
我们再测试一下，速度明显增快：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210208184949581.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
另外，直接使用`pip install 包名`即可。

<hr>

另外，送给大家一段清理垃圾的代码：

```html
<font color="red" face="楷体" onmousedown="alert('清理成功！')">清理垃圾</font>
```

