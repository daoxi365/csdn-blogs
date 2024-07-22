@[TOC]
<hr>

# 前言
好家伙，这个程序我做了整整一中午！看我搞得我的QQ邮箱，乌烟瘴气，全是测试用的邮件……
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0599e776d23341e7b2cd83b572d882d2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
直到看到成功了，我才高兴地蹦了起来，然后发了这篇博客。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/36ff7c46025d440ba50bbebec68aa0a3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
这个程序使用`django`制作，具体结构如下：

```python
D:.
│  putMessage.py
│
└─template
    │  db.sqlite3
    │  manage.py
    │  users
    │
    └─template
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
话不多说，看下有修改的地方。


# 程序

> 运行前，请安装`django`、`pywebio`、`requests`模块。

**（产品名称可以一键修改）**
## `django`配置
最原始的配置，直接`django-admin startproject template`。修改一下以下程序：
## `settings.py`
程序需要修改`FOLLOW_HOSTS`，添加元素`*`。
## `urls.py`
服务器的主要部分。

```python
from django.shortcuts import HttpResponse
from django.urls import path
from random import randint
from json import dumps
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

isLogin = False  # 已登录开关
product = 'xxx'  # 产品名称一键修改
passwordNew = 0  # 验证码

def main(request): # 主页面（没啥用，随便写）
    return HttpResponse('<center><b><h1><font face="Microsoft YaHei" color="red">欢迎使用%s！</font></h1></b></center>' % product)

def VC(request): # 发送邮箱验证码
    global passwordNew
    email = request.GET['m']
    sender = "qingfengstudio@yeah.net"    # 私人邮件配置，请勿商用
    password = "GMDCFHTPQHBEZFCH"         # 私人邮件密码，请勿商用
    v = randint(100000,999999)            # 验证码
    # 邮件内容
    mailContent = '''%s产品的用户：
您的登录验证码为%d，打死也不要告诉别人哦！''' % (product,v)
    ret = True
    passwordNew = v
    try:
        msg = MIMEText(mailContent, "plain", "utf-8")
        msg["From"] = formataddr(["老潘的消息", sender])
        msg["To"] = formataddr(["FK", email])
        msg["Subject"] = "%s软件登录验证" % product

        server = smtplib.SMTP_SSL("smtp.yeah.net", 465)
        server.login(sender, password)
        server.sendmail(sender,[email,],msg.as_string(),)
        server.quit()
    except Exception as e:
        ret = False
        err = str(e)
        print('遇到错误：%s' % err)
    return HttpResponse(dumps({'state':str(ret)}))
    
def login(request):
    # 定义全局变量：登录开关
    global isLogin
    # 获取已有的用户名、密码
    with open('users','r',encoding = 'utf-8') as f:
        a = f.read()
    b,c,temp = [],[],[]
    b = a.splitlines()
    
    #=============================================================================
    # 这后面的东西，是以前根据用户名密码来设置的，这里不用c                       
    # for i in range(0,len(b)):                                                
    #     temp = b[i].split(':')                                              
    #     c.append({'username':temp[0],'password':temp[1]})                  
    #=============================================================================
    
    # 判断用户端发送的get请求发送的用户名密码是否匹配，因为无重要隐私信息使用get请求
    wantU = request.GET['u']
    wantP = request.GET['p']
    loginer = False
    verificationCode = str(passwordNew)
    print(verificationCode)
    if wantP == verificationCode:
        if wantU in b:
            loginer = True
    isLogin = loginer
    # 返回验证结果
    if loginer == True:
        return HttpResponse(dumps({'state':'Okay','text':'You have successfully logged in, welcome!'}))
    else:
        return HttpResponse(dumps({'state':'Error','text':'Failed to log in successfully. The possible reasons are: (1) the user is not registered; (2) Wrong user name or password.'}))
    
def loginOkay(request):
    if isLogin == True:
        return HttpResponse('<p><b><center><font face="仿宋" color="red"><h1>您好，用户！</h1></font></center></b></p>')
    else:
        return HttpResponse('<p><b><center><font face="仿宋" color="red"><h1>请先登录！</h1></font></center></b></p>')
        
urlpatterns = [
    path('',main),
    path('login/',login),
    path('vc/',VC),
    path('okay/',loginOkay),
]

```

## 客户端程序`putMessage.py`

```python
from requests import get
from pywebio.input import *
from pywebio.output import *
import webbrowser

product = 'xxx'  # 产品名称
serverIP = 'http://127.0.0.1:8000/'  # 默认IP
put_markdown('**您好，欢迎使用%s**！' % product)
email = input('输入您的邮箱')

r1 = get(serverIP + 'vc/',params = {'m':email,}).json()
if r1['state'] == 'True':
    ps = input('输入您的验证码')
    r2 = get(serverIP + 'login/',params = {'u':email,'p':ps}).json()
    if r2['state'] == 'Okay':
        put_markdown('message from SERVER:%s' % r2['text'])
        webbrowser.open_new_tab(serverIP + 'okay/')
    else:
        put_markdown('您的登录出现错误，如下：\n%s' % r2['text'])
else:
    put_markdown('验证码发送失败！')
```

# 运行效果展示
先运行服务器，`python manage.py runserver`.
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6fca2e6172e54efba87b54e8ae5393c3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
运行客户端。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9b981c40ea2545eaa22667047584b1c3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
输入邮箱点击提交，两三秒后提示输入验证码，与此同时在邮箱里收到验证码，在网页上输入。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8be3bb0d268740ae81164683835b1911.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（模仿百度）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4b7574162b4248d39b09b121a022e86e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e379ae51551e4e559c557dd17eb0f7d3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0c45e5f0766346d198dd8131a4041d6f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

我提供了很多地方可以供自定义，大家需要，尽管拿去使用，别忘了修改邮箱的密码，请勿商用（这是我自己的小号）。

## 下载
[需要下载请看我的资源。](https://download.csdn.net/download/PanDaoxi2020/79571453)
