@[toc]

# 前言
也是一个`django`/`pywebio`的项目。

```python
D:.
│  putMessage.py
│
└─server
    │  Data
    │  db.sqlite3
    │  manage.py
    │
    └─server
        │  asgi.py
        │  settings.py
        │  urls.py
        │  wsgi.py
        │  __init__.py
        │
        └─__pycache__
                settings.cpython-36.pyc
                urls.cpython-36.pyc
                wsgi.cpython-36.pyc
                __init__.cpython-36.pyc
```
实现了个什么效果？在线答题并统计答题结果。

# 正文
这个东西比我的那个登录验证模板要简单一些。但是，这个项目也有一个有趣的东西。我们来看看吧。。
创建项目的命令：

```python
django-admin startproject
```

## 1.`settings.py`
也是添加那一项`ALLOWED_HOSTS` 的元素`*`，这里不再赘述。
## 2.`urls.py`
主要的服务器程序。
```python
from django.shortcuts import HttpResponse
from django.urls import path
from json import dumps

avg = 0     # 记录平均分
humen = 0   # 记录人数
names = []  # 记录答题人名字
avgtime = 0 # 记录平均时间

def readAs(request): # 读取和写入
    global humen,avg,names,avgtime
    reads,data,temp = [],[],[]
    with open('Data','r',encoding='utf-8') as f:
        reads = f.read().splitlines()
    # 添加请求来的数据
    text = '%s的成绩是%s，%s' % (request.GET['name'],request.GET['score'],request.GET['time'])
    reads.append(text)
    for i in range(0,len(reads)):
        temp = reads[i].split('的成绩是')
        # 分割字符串、储存字典
        t = reads[i].split('，')
        data.append({'name':temp[0],'score':float(temp[1].split('，')[0]),'time':int(t[1])})
    del temp,reads
    # 储存数据
    humen = len(data)
    for i in range(0,humen):
        avg += data[i]['score']
    avg /= humen
    for i in range(0,humen):
        print(data[i]['name'])
        names.append(data[i]['name'])
    for i in range(0,len(data)):
        avgtime += data[i]['time']
    avgtime /= humen 
    # 重新写入
    with open('Data','a',encoding='utf-8') as f:
        f.write(text + '\n')
    return HttpResponse(dumps({'humen':str(humen),'avg':str(int(avg)),'time':str(int(avgtime))}))

def main(request):
    return HttpResponse('<p><b>当前答题情况：</b></p><font face="Courier New" color="green"><b><p>答题人数：%d</p><p>答题平均分：%d</p><p>平均用时：%s秒</p><p><a href="/answer" title="答题列表">答题列表</a></p></b></font>' % (humen,avg,avgtime))

def answerList(request): # 答题名单
    string = ''
    for i in range(0,len(names)):
        string += '%s\n' % names[i]
    return HttpResponse(string)
    
urlpatterns = [
    path('read/',readAs),
    path('',main),
    path('answer/',answerList)
]

```
## 3.`putMessage.py`
客户端，发送请求用的。

```python
from pywebio.input import *
from pywebio.output import *
from requests import get
from random import randint
from time import time

url = 'http://127.0.0.1:8000/' # 默认IP
operate,answer = [],[]
right = 0 # 正答
n = 5 # 五道题
tempSco = 100 / n # 一道题的分数

# 如果不能整除
if 100 % n:
    n = 5
    tempSco = 20 

# 随机生成运算题
for i in range(0,n):
    a,b,c = randint(1,9),randint(1,9),0
    if a < b: 
        c = b
        b = a
        a = c
    del c
    operate.append('%d%s%d' % (a,['+','-','*'][randint(0,2)],b))
    
# 计算答案
for i in range(0,len(operate)):
    answer.append(eval(operate[i]))

# 显示
put_markdown('请你认真答题！')
name = input('请输入你的名字：')
if ('的成绩是' in name) or ('，' in name):
     put_markdown('你的名字中含有非法字符，请修改。')
     exit()
last = time() # 计时开始
for i in range(0,len(operate)):
    ua = input('请回答：%s=?' % operate[i])
    if ua == str(answer[i]):
        right += 1
current = time() # 计时结束
right *= tempSco # 计算正确率

# 发送请求
x = int(current-last)
params = {
          'name':name,
          'score':right,
          'time':x,
          }
res = get(url + 'read/',params=params).json()
put_markdown('已经有%s人提交，平均分是：%s，平均用时：%s\n你的分数：%f，你的用时：%d' % (res['humen'],res['avg'],res['time'],int(right),x))
```

# 实现的效果
运行服务器，打开客户端。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ec5e92e95e574d798a65e4c1b72ee835.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/324caed404314bb3836a1ccc0ea2abd7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
5道题。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/dbcb388f2b044600bdff642aec6256c9.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a3ba78d4deff4bba866e5f0b49c4758f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/16e04a2eb9a144ddae60920e1d3d0e36.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)



## 下载
[点这下载。](https://download.csdn.net/download/PanDaoxi2020/80105410)
