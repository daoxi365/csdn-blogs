方法很简单，一直在后台读取即可。删除时会提示无法访问，关掉就可以删掉了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7fe75e37f098433d8426d4a723a4aa17.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```python
f = open("a.txt","r")
while True:
    f.read()
```
需要在同目录下创建一个`a.txt`，再运行这个文件将无法删除，`pyinstaller`以后可以关闭黑色窗口，伪装成无法删除。可以从任务管理器中关闭。
