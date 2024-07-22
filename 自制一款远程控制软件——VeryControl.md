注意，文中链接已经转移至[Github](https://github.com/PanDaoxi/very-control)，原链接失效。

@[toc]

# 前言
**前排提醒：这篇文章有点儿长，如果直接想看效果可以[来此下载](https://pandaoxi.coding.net/public/pandaoxi/Projects/git/files/master/Very_Control)，代码看看就行了。**
```
                                                                         _..._       .-'''-.                                    .-'''-.
                                                                      .-'_..._''.   '   _    \                                 '   _    \  .---.
 .----.     .----.   __.....__                                      .' .'      '.\/   /` '.   \    _..._                     /   /` '.   \ |   |
  \    \   /    /.-''         '.         .-.          .-           / .'          .   |     \  '  .'     '.                  .   |     \  ' |   |
   '   '. /'   //     .-''"'-.  `. .-,.--.\ \        / /          . '            |   '      |  '.   .-.   .     .|  .-,.--. |   '      |  '|   |
   |    |'    //     /________\   \|  .-. |\ \      / /           | |            \    \     / / |  '   '  |   .' |_ |  .-. |\    \     / / |   |
   |    ||    ||                  || |  | | \ \    / /            | |             `.   ` ..' /  |  |   |  | .'     || |  | | `.   ` ..' /  |   |
   '.   `'   .'\    .-------------'| |  | |  \ \  / /             . '                '-...-'`   |  |   |  |'--.  .-'| |  | |    '-...-'`   |   |
    \        /  \    '-.____...---.| |  '-    \ `  /               \ '.          .              |  |   |  |   |  |  | |  '-                |   |
     \      /    `.             .' | |         \  /                 '. `._____.-'/              |  |   |  |   |  |  | |                    |   |
      '----'       `''-...... -'   | |         / /                    `-.______ /               |  |   |  |   |  '.'| |                    '---'
                                   |_|     |`-' /                              `                |  |   |  |   |   / |_|
                                            '..'                                                '--'   '--'   `'-'

```
<center><font color="gray">VeryControl 软件的 Logo</font></center>
<br>

我最近多少有点儿闲得慌，前两天出去玩儿了一圈，路上就一直盘算着这事儿，前两天做了个雏形，今天完善好了，分享给大家一起看着玩儿。

这个程序感觉还凑合，制作了一个网页端。虽然设计不咋样吧（我是初学者），但是至少能在手机、电脑等各种设备上成功访问并进行远程命令执行。

用到的语言是 $Python$  和 $HTML$，使用了 $Django$ 框架，及一些其他的小功能。
 
软件截图： ![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5341c25dea4f43968882cca2a9edd0d7.jpeg)
# 软件下载
> 建议阅读里面的注意事项，很重要。

软件下载地址：<https://download.csdn.net/download/PanDaoxi2020/86265805>
软件官方网站：<https://pandaoxi-project.github.io/very-control/>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e11873091ec445089515cef422062638.jpeg)

# 代码展示
让我们一起来看看这个小项目的源代码叭~

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/02d90a09ab394aab8a3b36b4312112ae.gif)
##  $HTML$ 前端部分
$HTML$ 部分主要是客户端的一些东西，直接在网页上访问，并传回相应的内容给后端 $API$ 。
### 1.客户端主页
最基本的内容，可以直接在主页填写命令的表单，然后 $POST$ 给后端的 $API$ `/run`。

$$
\begin{cases}
  & \text command=普通执行命令 \\
  & \text echo=输入命令，并返回输出内容 \\
  & \text code=执行批处理命令 \\
  & \text runf=运行应用程序（需要应用程序提交工具） \\
\end{cases}
$$

```html
<!--设置标题-->
<title>Very Control</title>
<!--CSS样式-->
<style>
/*给页面添加背景图片，还是随机的（这是一个风景壁纸API）*/
.bg{
background-image: url(https://api.ixiaowai.cn/gqapi/gqapi.php);
}
/*这是给输入框设置透明度的，这样设置正好能看清文字也能欣赏背景*/
input,textarea{
filter:alpha(Opacity=30);
-moz-opacity:0.4;
opacity:0.6;
}
</style>
<!--设置的div，显示背景和文字-->
<div class="bg">
	<!--表单-->
    <form id="run" action="/run" method="post" enctype="multipart/form-data">    
    <h1>Very Control 多对一远程控制平台</h1>    
    <p>输入命令： <input type="text" name="command" placeholder="输入 Windows 命令 "/></p>
    <p>带有回显的命令：<input type="text" name="echo" placeholder="输入命令，并返回输出内容 "/>
    <p>提交批处理文件的源代码：</p>
    <p><textarea name="code" rows="10" cols="75" placeholder="输入你的 Windows Batch 代码"></textarea></p>
    <p>或者使用<b><a href="https://pandaoxi2020.lanzouy.com/iCMJm07i76ti" target="_blank">应用程序提交工具</a></b></p>
    <input type="submit" value="运行"/>
    </form>
    <br><br>
    <p>当前软件信息：</p>
    <p>版本： 1.3.0.0 [2022-7-22 Update]</p>
    <p>开发者：<b><font face="Consolas"><a href="https://pandaoxi.github.io/" target="_blank">PanDaoxi</a></font></b></p>
    <p>开源地址：<a href="https://pandaoxi.coding.net/public/pandaoxi/Projects/git/files/master/Very_Control">点击这里去访问</a>！</p>
    <p>开发者邮箱（欢迎意见反馈和技术支持）：<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=5paHiIKHiZ6P1NbU1KaXl8iFiYs" style="text-decoration:none;"><img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_02.png"/></a></p>
</div>
<hr>
<!--其他功能的超链接-->
<center><p>其他功能：<a href="ss">截取屏幕</a>		<a href="inf">查看被控制者信息</a>		<a href="cam">捕获摄像头</a>		<a href="sendm">发送消息</a>		<a href="rn">阅读官方通知</a></p></center>
```
### 2.拍照、截图

> 这两个功能的页面基本相同。

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3e75ad6375754a9bbec428718f0b4cbc.png)

```html

<title>摄像头捕获</title>
<center>
	<!--此处正常的话，如果有摄像头应该显示默认摄像头的画面。为了保护隐私，我用开发者模式放了一张图片替换了摄像头图像。-->
    <img src="https://pandaoxis.coding.net/p/pdxres/d/pdxres/git/raw/master/RESOURCE/20220729_picture.png" alt="摄像头捕获" height="450" width="800"/>
    <br><br>
    <p>该功能可能会比较卡顿；如果不能正常显示出摄像头图像，可能是因为被控制设备的摄像头无法访问。</p>
    <br><hr>
    <a href="jump">回到主页</a>		<a href="cam">重新拍照</a>
</center>
```

```html
<title>Screen Shot</title>
<center>
	<!--使用图片的base64显示，因为太长我就不写了-->
    <img src="data:image/png;base64, ..." alt="截图" height="576" width="1024"/>
    <br><br><hr>
    <a href="jump">回到主页</a>		<a href="ss">重新截图</a>
</center>
```

## $Python$ 后端部分
目录树：

```python
D:.
│  db.sqlite3
│  main.py
│  manage.py
│
└─VeryControl
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
我特意给它做了一个[应用程序版](https://pandaoxi.coding.net/p/pandaoxi/d/Projects/git/raw/master/Very_Control/VeryControl_Server.exe)的，内置 第 $1.3.0.0$ 的服务器版本 它会自己更新，不用管它。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8ea6ca2342cd496ea367d64659817a1e.png)

 ### 1. $/main.py$


>  这个程序的主要功能是：
>  - 绘制 $LOGO$ 。😉
>  - 生成服务器，使得前端可以访问。😊
>  - 检查是否有更新，如果没有直接运行服务器；如果有，就强制更新。😑
> <br>
> 第三条性质感觉有那么一种 $Windows$ 的传奇色彩~ 😂

```python
# Copyright 2022 by PanDaoxi. All rights reserved.
from socket import socket, AF_INET, SOCK_DGRAM
from os import system, name
from time import strftime, sleep
from colorama import init, Fore, Back
from requests import get

version = "1.3.5.0"
updateFiles = {
    "./manage.py": "https://pandaoxi-project.github.io/very-control/Very_Control/manage.py",
    __file__: "https://pandaoxi-project.github.io/very-control/Very_Control/main.py",
    "./VeryControl/asgi.py": "https://pandaoxi-project.github.io/very-control/Very_Control/VeryControl/asgi.py",
    "./VeryControl/settings.py": "https://pandaoxi-project.github.io/very-control/Very_Control/VeryControl/settings.py",
    "./VeryControl/urls.py": "https://pandaoxi-project.github.io/very-control/Very_Control/VeryControl/urls.py",
    "./VeryControl/wsgi.py": "https://pandaoxi-project.github.io/very-control/Very_Control/VeryControl/wsgi.py",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
}

def update():
    for i in updateFiles.keys():
        with open(i, "wb") as f:
            f.write(get(updateFiles[i], headers=headers).content)
        sleep(0.3)

def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip

if __name__ == "__main__" and name == "nt":
    temp = get('https://pandaoxi-project.github.io/very-control/Very_Control/VeryControl/VERSION',headers=headers)
    temp.encoding = 'utf-8'
    latest = temp.text
    if latest != version:
        print('Please wait a moment, we are updating the software for you ...')
        update()
    system('cls')
    print(
        """                                                                         _..._       .-\'\'\'-.                                    .-\'\'\'-.          
                                                                      .-'_..._''.   '   _    \                                 '   _    \  .---. 
 .----.     .----.   __.....__                                      .' .'      '.\/   /` '.   \    _..._                     /   /` '.   \ |   | 
  \    \   /    /.-''         '.         .-.          .-           / .'          .   |     \  '  .'     '.                  .   |     \  ' |   | 
   '   '. /'   //     .-''"'-.  `. .-,.--.\ \        / /          . '            |   '      |  '.   .-.   .     .|  .-,.--. |   '      |  '|   | 
   |    |'    //     /________\   \|  .-. |\ \      / /           | |            \    \     / / |  '   '  |   .' |_ |  .-. |\    \     / / |   | 
   |    ||    ||                  || |  | | \ \    / /            | |             `.   ` ..' /  |  |   |  | .'     || |  | | `.   ` ..' /  |   | 
   '.   `'   .'\    .-------------'| |  | |  \ \  / /             . '                '-...-'`   |  |   |  |'--.  .-'| |  | |    '-...-'`   |   | 
    \        /  \    '-.____...---.| |  '-    \ `  /               \ '.          .              |  |   |  |   |  |  | |  '-                |   | 
     \      /    `.             .' | |         \  /                 '. `._____.-'/              |  |   |  |   |  |  | |                    |   | 
      '----'       `''-...... -'   | |         / /                    `-.______ /               |  |   |  |   |  '.'| |                    '---' 
                                   |_|     |`-' /                              `                |  |   |  |   |   / |_|                          
                                            '..'                                                '--'   '--'   `'-'                               \n\n"""
    )

    init(autoreset=True)
    print(
        "Welcome to Very_Control !\nControlled end:",
        Fore.RED + "http://%s:%s/\n" % (getIP(), strftime("%Y")),
    )
    system("python manage.py runserver %s:%s" % (getIP(), strftime("%Y")))
    input()
```
### 2. $/VeryControl/urls.py$ 
这是服务器的核心，我们靠它进行一系列的控制。

```python
from django.urls import path as site
from django.shortcuts import HttpResponse
from os import system, remove, environ
from base64 import a85decode, b64encode
from sys import path
from requests import get
from pyautogui import screenshot
from tkinter import Tk
from time import strftime, sleep
from cv2 import VideoCapture, imwrite
from pyttsx3 import init as ttsInit

# 定义 TTS 朗读者
tts_name = []
engine = ttsInit()
voices = engine.getProperty('voices') 
for voice in voices:
    tts_name.append(voice.name) 
engine.stop()
del engine
tts_name.append('Windows <kbd>SAPI.spVoice</kbd>')

# 求最大公因数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 适配图片比例
def change(a, b):
    x = gcd(a, b)
    a /= x
    b /= x
    while a < 500 or b < 500:
        a *= 2
        b *= 2
    return (a, b)


# 拍照
def get_photo():
    cap = VideoCapture(0)
    f, frame = cap.read()
    imwrite("./photo.png", frame)
    with open("./photo.png", "rb") as f:
        temp = b64encode(f.read()).decode()
    remove("./photo.png")
    cap.release()
    return "data:image/png;base64,%s" % temp


# 主页
def main(request):
    return HttpResponse(
        """<title>Very Control</title>
<style>
body{
background-image: url(https://pic1.zhimg.com/80/v2-fbbb97b977b5cebc66dc3cefab0ac981_1440w.jpg?source=1940ef5c);
}
input,textarea{
filter:alpha(Opacity=30);
-moz-opacity:0.4;
opacity:0.6;
}
</style>
    <form id="run" action="/run" method="post" enctype="multipart/form-data">    
    <h1>Very Control 多对一远程控制平台</h1>    
    <p>输入命令： <input type="text" name="command" placeholder="输入 Windows 命令 "/></p>
    <p>带有回显的命令：<input type="text" name="echo" placeholder="输入命令，并返回输出内容 "/>
    <p>上传应用程序：<input type="file" name="runf"/></p>
    <p>提交批处理文件的源代码：</p>
    <p><textarea name="code" rows="10" cols="75" placeholder="输入你的 Windows Batch 代码"></textarea></p>
    <input type="submit" value="运行"/>
    </form>
    <br><br>
<hr>
<center><p>其他功能：<a href="ss">截取屏幕</a>\t\t<a href="inf">查看被控制者信息</a>\t\t<a href="cam">捕获摄像头</a>\t\t<a href="sendm">发送消息</a>\t\t<a href="rn">阅读官方通知</a></p></center>
"""
    )


# 阅读通知
def readNotice(request):
    return HttpResponse(
        """<title>阅读官方通知</title>
<h1>官方通知</h1>
<hr><br>
<iframe src="https://pandaoxi-project.github.io/very-control/" width="800" height="450"></iframe>
<p>页面加载较慢是正常现象，请耐心等候。</p>
<br><hr>
<p>软件信息：</p>
<p>开发者：<b><font face="Consolas"><a href="https://pandaoxi.github.io/" target="_blank">PanDaoxi</a></font></b></p>
<p>开发者邮箱（欢迎意见反馈和技术支持）：<a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=5paHiIKHiZ6P1NbU1KaXl8iFiYs" style="text-decoration:none;"><img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_02.png"/></a></p>
<p><a href="https://github.com/pandaoxi-project/very-control/tree/main/Very_Control"><kbd>Very_Control</kbd>软件已经开源，欢迎前来查看😀</a></p>
<center><a href="jump">回到主页</a></center>
"""
    )


# 运行
def run(request):
    system("chcp 65001 >nul")
    text = request.POST.get("command")
    code = request.POST.get("code")
    runf = request.FILES.get("runf")
    echo = request.POST.get("echo")
    if code:  # 优先级最高的 执行批处理脚本
        with open("temp.bat", "w", encoding="utf-8") as f:
            f.write(code + "\nexit")
        system("start %s\\temp.bat" % path[0])
    if runf:  # 次之的应用程序
        with open("temp.exe", "wb") as f:
            f.write(b"")
        with open("temp.exe", "wb") as f:
            for i in runf.chunks():
                f.write(i)
        system("start %s\\temp.exe" % path[0])
    if text:  # 最后是直接执行命令
        system(text)
    if echo:  # 带回显的执行命令
        try:
            remove("temp.txt")
        except:
            pass
        system("%s >> temp.txt" % echo)
        with open("temp.txt", "r", encoding="utf-8") as f:
            ret = f.read().splitlines()
        s = ""
        for i in ret:
            s += "<p>%s</p>\n" % i
        return HttpResponse(
            """<title>程序运行结果</title>
%s
<br><hr><br>
<center><a href="jump">回到主页</a></center>"""
            % s
        )
    return HttpResponse('<center><h1>运行成功！🎉🎉</h1></center><meta http-equiv="refresh" content="2;url=jump"/>')


# 截图
def ss(request):
    window = Tk()
    window.withdraw()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    image = screenshot(region=(0, 0, width, height))
    image.save("./screenshot.png")
    with open("./screenshot.png", "rb") as f:
        content = b64encode(f.read()).decode()
    remove("./screenshot.png")
    w, h = change(width, height)
    return HttpResponse(
        """<title>Screen Shot</title>
<center>
    <img src="data:image/png;base64,%s" alt="截图" height="%d" width="%d">
    <br><br><hr>
    <a href="jump">回到主页</a>\t\t<a href="ss">重新截图</a>
</center>
    """
        % (content, h, w)
    )
    window.mainloop()


# 环境信息
def inf(request):
    system("chcp 65001 >nul")
    s1 = ""
    for i in environ.keys():
        s1 += "<p>%s\t%s</p>\n" % (i, environ[i])
    try:
        remove("temp.txt")
    except:
        pass
    system("tasklist>>temp.txt")
    with open("temp.txt", "r", encoding="utf-8") as f:
        s2 = f.read().splitlines()
    remove("temp.txt")
    s3 = ""
    for i in s2:
        s3 += "<p>%s</p>\n" % i
    return HttpResponse(
        """<title>Os_Environ</title>
<h1>系统环境变量 </h1>
%s
<br><br><hr>
<h1>运行的进程（如需对齐可以看此网页的源代码） </h1>
%s
<br><br><hr>
<center><a href="jump">返回主页</a></center>
"""
        % (s1, s3)
    )


# 拍照
def camera(request):
    return HttpResponse(
        """<title>摄像头捕获</title>
<center>
    <img src="%s" alt="摄像头捕获" height="450" width="800">
    <br><br>
    <p>该功能可能会比较卡顿；如果不能正常显示出摄像头图像，可能是因为被控制设备的摄像头无法访问。</p>
    <br><hr>
    <a href="jump">回到主页</a>\t\t<a href="cam">重新拍照</a>
</center>
    """
        % get_photo()
    )


# 发送消息文本
def sendMessage(request):
    return HttpResponse(
        """<title>发送消息文本</title>
<style>
body{
background-image: url(https://pic1.zhimg.com/80/f56513788384645db768d0ec542dec33_1440w.jpg);
}
input,textarea{
filter:alpha(Opacity=30);
-moz-opacity:0.4;
opacity:0.6;
}
</style>
    <form id="show" action="/showm" method="post" enctype="multipart/form-data">    
    <h1>Very Control - 消息发送器</h1>    
    <p>发送语音消息（内容将会在被控制端朗读，您可以<b><a href="/settts">自定义朗读者</a></b>，或使用默认值）：<input type="text" name="reader" placeholder="输入要发送的内容"/></p>
    <p>输入发送给被控制端的消息，消息将会以<b>警示框</b>的形式表现：</p>
    <p><textarea name="msg" rows="25" cols="100" placeholder="输入你的 消息文本"></textarea></p>
    <input type="submit" value="发送"/>  
    <br><br>
<br><br><hr>
<center><a href="jump">回到主页</a></center>  
"""
    )


# 显示信息
def showMessage(request):
    msg = request.POST.get("msg")
    reader = request.POST.get("reader")
    if msg:
        with open("temp.py", "w+", encoding="utf-8") as f:
            f.write("from easygui import msgbox\nmsgbox('''%s''',\"Very Control\")" % msg)
        system("start /min cmd /c temp.py")
    if reader:
        tts_config = []
        try:
            with open("TTS_config", "r", encoding="utf-8") as f:
                tts_config = f.read().splitlines()
            c1, c2, c3 = int(tts_config[0]), int(tts_config[1]), float(tts_config[2])
        except:
            c1, c2, c3 = 0, 100, 1.0
        if tts_config[0] == "2":
            with open("say.vbs", "w", encoding="ANSI") as f:
                f.write("set sapi = createObject(\"SAPI.SpVoice\")\nsapi.Speak \"%s\"" % reader)
            system("start /min cmd /c call \"say.vbs\"")
        else:
            engine = ttsInit()
            engine.setProperty("rate", c2)
            engine.setProperty("volume", c3)
            voices = engine.getProperty("voices") 
            engine.setProperty("voice", voices[c1].id)
            engine.say(reader)
            engine.runAndWait()
            engine.stop()
    return HttpResponse("""<center><h1>发送成功！✨</h1></center><meta http-equiv="refresh" content="2;url=sendm"/>""")


def setupTTS(request):
    temps = ""
    for i in range(len(tts_name)-1, -1, -1):
        temps += "  <input type=\"radio\" name=\"tts_id\" value=\"%d\" checked>%s<br>\n" % (i, tts_name[i])
    return HttpResponse(
        """<title>自定义 TTS</title>
<style>
body{
background-image: url(https://pic1.zhimg.com/80/f56513788384645db768d0ec542dec33_1440w.jpg);
}
input,textarea{
filter:alpha(Opacity=30);
-moz-opacity:0.4;
opacity:0.6;
}
</style>
    <form id="setup" action="/upd_tts" method="post" enctype="multipart/form-data">    
    <h1>Very Control - 自定义 TTS 朗读者</h1>    
    <p>设置朗读者音色：<br><br>
    %s
    </p>
    <p>以下设置，仅对非 <kbd>SAPI</kbd> 有效；错误的设置将使用默认值。</p>
    <p>语速：<input type="text" name="tts_speed" placeholder="输入正整数，默认为 100"/><p>
    <p>音量：<input type="text" name="tts_volume" placeholder="输入小数，默认为 1.0"/><p>
    <p><a href="/upd_tts">恢复默认设置</a></p>
    <input type="submit" value="保存"/>  
    <br><br>
<br><br><hr>
<center><a href="javascript:history.back(-1)"">回到上一页</a></center>  
"""
        % temps
    )


def updateTTS(request):
    tts_id = request.POST.get("tts_id")
    tts_speed = request.POST.get("tts_speed")
    tts_volume = request.POST.get("tts_volume")
    if tts_id == None and tts_speed == None and tts_volume == None:
        tts_id = "0"
        tts_speed = "100"
        tts_volume = "1.0"
    with open("TTS_config", "w", encoding="utf-8") as f:
        f.write("%s\n%s\n%s" % (tts_id, tts_speed, tts_volume))
    return HttpResponse("""<center><h1>保存完成！🎈</h1></center><meta http-equiv="refresh" content="2;url=sendm"/>""")

urlpatterns = [
    site("", main),
    site("jump", main),
    site("run", run),
    site("ss", ss),
    site("inf", inf),
    site("cam", camera),
    site("sendm", sendMessage),
    site("showm", showMessage),
    site("rn", readNotice),
    site("settts", setupTTS),
    site("upd_tts", updateTTS),
]

```

# 最后
有些时候，有些BUG，总也改不掉。还是需要专业的力量的😅。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c892ff73572c4eb59a84872f18e2c862.jpeg)
对此感谢博客园和菜鸟教程的帮助！
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6ccac558726141cb806e9a87a2abc080.jpeg)
完美结束。
