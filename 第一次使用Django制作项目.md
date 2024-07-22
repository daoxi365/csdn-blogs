今天，我分享一下几天以前第一次使用`flask`框架制作一个简单小项目的流程。
我们先来创建一个文件夹：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210110083804763.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
好了，现在我们打开命令提示符，切换到当前目录：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210110083916824.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
安装`Django`：`pip3 install django`
（我这里已经安装过了，就不演示效果了）
如果没有报错，使用命令`pip list`，出现`django`一项即可。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210110084358100.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
<hr>
现在我们输入命令：

```powershell
django-admin startproject hw
```

`hw`是这个项目的名字。我们打开这个文件夹，发现其目录是这样的：
```python
D:.
└─hw
    │  manage.py
    │
    └─hw
            asgi.py
            settings.py
            urls.py
            wsgi.py
            __init__.py

```
现在，我们打开`hw\hw\urls.py`，发现其内容如下：

```python
"""hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```
现在，让我们做个小小的改动：
（上面的注释是帮助）
```python
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse

#注意参数request绝对不能少，少了就报错
def mainPage(request):
	#直接返回代码
	return HttpResponse('<font face="宋体" color="red" size=20><center>Hello,World!</center></font>')

def hw(request):
	return HttpResponse('<h1>你好，世界！</h1>')

urlpatterns = [
    path('',mainPage),
    path('hw/',hw),
]
```
现在，让我们打开命令提示符，切换到当前目录，输入代码如下：

```python
python manage.py runserver 127.0.0.1:8000
```
如果得到以下反馈：

```python
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 10, 2021 - 09:37:22
Django version 3.1.4, using settings 'hw.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
那么说明运行成功！
请打开上面提示的链接：`127.0.0.1:8000`
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210110093907696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
成功！再看`127.0.0.1:8000/hw`：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210110093952335.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
完事！
