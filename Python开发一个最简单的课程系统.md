2022年1月16日修改：
请注意，最近有网友反应称该程序无法运行，本程序最低要求需Python3.6，请安装`easygui`、`pillow`，在windows环境下运行。

<hr>

我们来制作一个大项目：课堂系统。
下面的“腾飞课堂”可以改成您想要的名字，`text.txt`里面的内容可以随便改。

> 本次我们需要使用到 requests 模块、 easygui 模块和 PIL 库。
> pyinstaller命令。


**首先我们要创建很多Python文件：**
![目录树](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813085500535.png#pic_center)

**下面是系统的具体制作方法：**
1、创建如上的所有文件和文件夹（都是空的）。
2、打开开发工具，导入该工程文件夹。
3、将下面图片复制到同一文件夹，重命名为上面的，黑板的图片为`blackboard.png`，背景图片命名为`background.jpg`。
![黑板](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813090444523.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![背景图片](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813090444393.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
4、打开`login.py`，输入以下代码：

```python
#导入包
from easygui import msgbox,multpasswordbox,buttonbox,passwordbox
from os import system,name

#声明所需变量
title = '腾飞线上课平台'
#账号密码
users = [
         ['学生账号01','01'],
         ['学生账号02','02'],
         ['学生账号03','03'],
         ]
#调整活页码
system('chcp 65001 >nul')
#登录所需函数
def login():
	#选择框
    choice = buttonbox('欢迎使用线上课平台！\n如果您需要进行操作，请先登录或注册！',title,('登录','注册'))
	#判断按钮是否为“登录”
    if (choice == '登录'):
    	#输入用户名和密码
        loginUser = []
        loginUser = multpasswordbox('请输入用户名和密码：',title,('用户名：','密码：'))
    	#判断用户名和密码是否相符
        for user in range(len(users)):
            if (loginUser[0] == users[user][0]) and (loginUser[1] == users[user][1]):
                msgbox('登录成功！按下下面的按钮即可跳转到主页面！',title,'确定')
                #打开主页面，退出循环
                system('cd "files" & call "choice.py"')
                break
        else:
        	#反馈
            msgbox('用户名或密码错误！',title,'确定')
    
    elif (choice == '注册'):
    	#如果点击“注册”，就弹出文字框让用户填写注册信息
        register = []
        register = multpasswordbox('请填写下面的注册信息：',title + ' - 注册',('用户名：','密码'))
        #确认密码
        ispassword = passwordbox('请确认密码：',title + ' - 注册')
        #如果密码一样
        if (register[1] == ispassword):
            #注册成功
            msgbox('注册成功！',title,'确定')
        else:
        	#反馈
            msgbox('两次输入密码不同！',title,'确定')
        #生成储存用户名和密码的文件
        with open('register.txt','w+') as fileWrite:
            fileWrite.write('{0}\n{1}\n\n'.format(register[0],register[1]))
        #添加元素
        users.append([register[0],register[1]])
        #打开主页面
        system('cd "files" & call "choice.py"')
        
    else:
    	#如果点“×”就退出
        exit()

#如果被打开且系统为Windows
if (__name__ == '__main__' and name == 'nt'):
	#运行
    login()
```
5、打开文件夹`files`，打开`choice.py`文件，输入代码如下：

```python
#导入包
from tkinter import Tk,Label,Button
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo,showerror,askyesno
from os import system
from os.path import splitext
from PIL import Image,ImageTk
from sys import exit
#声明标题，调整活页码
title = '线上课平台'
system('chcp 65001 >nul')
# tkinter框
window =  Tk()
window.title(title)
window.resizable(0,0)
    
    if yn == True:
        system('python "create.py"')
        window.destroy()
    else:
        pass
def homework():
    system('python homework.py')
    window.destroy()
    
def exercise():
    system('python exam.py')
    window.destroy()

def gotoclass():
    system('python class.py')
    window.destroy()
    
img = ImageTk.PhotoImage(file = 'background.jpg')
text = '您好，尊敬的客户！\n请选择服务：'
#设置属性
Label(window,image = img,text = text,foreground = 'blue',font = ('华文新魏',35),compound = 'center').pack()
Button(window,bd = 0,text = '做作业',command = homework,font = ('楷体',20)).place(x = 192,y = 405)
Button(window,bd = 0,text = '去练习',command = exercise,font = ('楷体',20)).place(x = 392,y = 405)
Button(window,bd = 0,text = '去上课',command = gotoclass,font = ('楷体',20)).place(x = 592,y = 405)

window.mainloop()
```
6、打开`homework.py`，输入代码如下：

```python
from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('homework')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的作业名称：\n')
    for topic in dir:
        print('{0}'.format(topic))
    name = input('\n>>>')
    for topic in dir:
        if name == topic:
            print('找到了作业：',topic,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(topic))
                system('chcp 65001')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的作业名称！')
else:
    print('没有未完成的作业！\n去休息一下吧！')
    system('pause')
```
7、`exam.py`输入代码：

```python
from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('topic')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的考试文件名称：\n')
    for exam in dir:
        print('{0}'.format(exam))
    name = input('\n>>>')
    for topic in dir:
        if name == topic:
            print('找到了考试文件：',topic,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(topic))        
                system('pause')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的考试名称！')
else:
    print('没有未完成的考试！\n去休息一下吧！')
    system('pause')
```
8、`class.py`内容：

```python
from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('class')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的课程文件名称：\n')
    for classes in dir:
        print('{0}'.format(classes))
    name = input('\n>>>')
    for classes in dir:
        if name == classes:
            print('找到了课程文件：',classes,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(classes))        
                system('pause')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的课程名称！')
else:
    print('没有未完成的课程！\n去休息一下吧！')
    system('pause')
```
9、`welcome.py`：

```python
from easygui import textbox

with open('text.txt','r',encoding = 'utf-8') as file:
    text = file.read()
    
textbox('下面是一封给您的信。','腾飞课堂',text = text,codebox = False)
```
10、文本文档

```
尊敬的用户，您好！
欢迎使用 腾飞课堂1.0 软件！

您可以使用此软件进行课堂管理，作业、考试等设备一应俱全。
您可以查看技术文档以学会更多操作！

联系方式：
邮箱： 3362157322@qq.com
QQ： 3362157322
官方网页（在这里查看官方技术文档）： http://pandaoxi.360doc.com/

更多信息：
开发语言：Python
原有账户（格式： [用户名,密码]）：[学生账号01,01],[学生账号02,02],[学生账号03,03]
需求：Windows环境、Python环境、网络
开发者：潘道熹
如果您有困难可以随时联系作者！                                                
        


                    腾飞课堂 开发者
                      2020/8/13
```
实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813103309765.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813103353997.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813103408161.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813103430134.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
其他效果大家自己尝试。

**教师版**
新建一个空白Python文档，输入以下内容：

```python
from easygui import buttonbox,msgbox,textbox,enterbox,multenterbox
from os import system,name
from sys import path
from requests import get

class_url = 'http://pub.idqqimg.com/pc/misc/groupgift/fudao/pc/EduLiteInstall_1.0.3.34_sign.exe'
download_name = 'Tencent Classroom Software 1.0.3.34.exe'
currentPath = path[0]
title = '线上课平台 - 插件'
button = '确定'

def download():
    getFile = get(class_url)
    with open(download_name,'wb') as download:
        download.write(getFile)

def new_exam():
    data = []
    data = multenterbox('请设置考试的信息：',title,('考试科目：','考试主题：','主考老师：','考试介绍：'))
    text = textbox('请输入考试的代码：',title,codebox = True,text = 'from easygui import *')
    code = """# *-* coding : utf-8 *-*
dict = {
    'subject' : '%s',
    'theme' : '%s',
    'teacher' : '%s',
    'introduce' : '%s',
    'application' : '%s'
        }
%s
""" % (data[0],data[1],data[2],data[3],'线上课平台-2020年8月新版',text)
    with open(data[1] + '.py','w+',encoding = 'utf-8') as file:
        file.write(code)
    msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\topic文件夹下即可被学生发现！'.format(currentPath),title,button)

def contact():
    askyn = buttonbox('联系我们：\n开发者：潘道熹\nQQ：3362157322\n网址：https://me.csdn.net/PanDaoxi2020\n邮箱：3362157322@qq.com\n当前系统版本：1.0',title,('联系作者邮箱','打开官方网页'))
    if askyn == '联系作者邮箱':
        system('start iexplore -incognito "http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=c0BARUFCRkRAQUEzAgJdEBwe"')
    elif askyn == '打开官方网页':
        system('start iexplore "http://pandaoxi.360doc.com/"')
        system('start iexplore "https://me.csdn.net/PanDaoxi2020"')
    
def new_homework():
    letter = textbox('请在下方写入您的作业Python代码：',title,text = 'from easygui import *\n',codebox = True)
    msgbox('# 这是您写入的Python代码\n\n{0}'.format(letter),title,button)
    homework_name = enterbox('请您为该作业命名：',title)
    if homework_name != None:
        with open('{0}.py'.format(homework_name),'w+',encoding = 'utf-8') as file:
            file.write(letter)
        msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\homework文件夹下即可被学生发现！'.format(currentPath),title,button)
    elif len(homework_name) >= 20:
        msgbox('名字超长！最多20个字符！',title,button)
    elif len(homework_name) <= 2:
        msgbox('名字超短！最少2个字符！',title,button)
    
def new_class():
    class_data = []
    class_data = multenterbox('请输入您要创建的课程信息：',title,('您要上课的主题：','课程URL：'))
    yn = buttonbox('您是否需要下载：腾讯课堂（Tencent Classroom Software）？',title,('下载','取消'))
    
    if yn == '下载':
        download()
    elif yn == '取消':
        pass
    else:
        msgbox('请选择一个按钮！',title,'确定')
        
    code = """# *-* coding : utf-8 *-*
from os import system,name
from easygui import buttonbox,msgbox

title = '去上课'
select = buttonbox('您的课程信息是否是： {1}。 ？',title,('是','否'))
list = [__name__,name]

def yes():
    system('start "C:\\Program Files\\Internet Explorer\\iexplore.exe" "{0}"')

def main():
    if (select == '是'):
        yes()
    elif (select == '否'):
        exit()
    else:
        msgbox('请选择一个按钮！',title,'确定')

if list[0] == "__main__" and list[1] == "nt":
    main()""".format(class_data[1],class_data[0])
    
    with open('{0}.py'.format(class_data[0]),'w+',encoding = 'utf-8') as file:
        file.write(code)
    msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\class文件夹下即可被学生发现！'.format(currentPath),title,button)
    
def main():    
    choice = buttonbox('您好，欢迎使用线上课平台！\n此程序适用于教师版。\n您可以通过此插件选择一些关于学生版的服务！',title,('新建作业','新建课程','新建练习','联系作者'))
    
    if choice == '新建作业':
        new_homework()
    elif choice == '新建课程':
        new_class()
    elif choice == '新建练习':
        new_exam()
    elif choice == '联系作者':
        contact()
    else:
        msgbox('请选择其中的一个按钮！',title,button)

if __name__ == '__main__' and name == 'nt':
    main()
    
```

**此系统的安装包**
我们来个这个系统写一个安装包，新建一个Python文档命名为`setup.py`，输入内容如下：

```python
# ShiJiaZhuang TengFei Online Class Platform 2020.8 New Edition Setup Tool
# The Code of The Installer by Pan Daoxi
# Product Version : 1.0 , Time : 2020/8/20
from tkinter import Tk
from tkinter.messagebox import askyesno,showinfo,showerror
from tkinter.filedialog import askdirectory
from os import system,makedirs,mkdir,name
from requests import get
from sys import path

data = {
        'path':path[0],
        'system' : name,
        'brand' : 'SJZ TengFei Online Class Platform',
        'trademark' : 'https://img-blog.csdnimg.cn/20200808104402354.jpg'
        }
coding = {
          'class' : r'''from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('class')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的课程文件名称：\n')
    for classes in dir:
        print('{0}'.format(classes))
    name = input('\n>>>')
    for classes in dir:
        if name == classes:
            print('找到了课程文件：',classes,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(classes))        
                system('pause')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的课程名称！')
else:
    print('没有未完成的课程！\n去休息一下吧！')
    system('pause')''',
          'exam' : r'''from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('topic')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的考试文件名称：\n')
    for exam in dir:
        print('{0}'.format(exam))
    name = input('\n>>>')
    for topic in dir:
        if name == topic:
            print('找到了考试文件：',topic,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(topic))        
                system('pause')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的考试名称！')
else:
    print('没有未完成的考试！\n去休息一下吧！')
    system('pause')''',
          'homework' : r'''from os import system,walk
from os.path import splitext,join

dir = []

def files(file_dir):
    for root, dirs, files in walk(file_dir):
        for file in files:
            if splitext(file)[1] == '.py':
                dir.append(join(root, file))
files('homework')
system('chcp 65001 >nul')
if len(dir) != 0:
    print('请输入您选择的作业名称：\n')
    for topic in dir:
        print('{0}'.format(topic))
    name = input('\n>>>')
    for topic in dir:
        if name == topic:
            print('找到了作业：',topic,'\n您要打开它吗（输入“YES”打开，输入“NO”不打开）？')
            yn = input('\n>>>').upper()
            if yn == 'YES':
                print('已经打开！\n')
                system('python "{0}"'.format(topic))
                system('chcp 65001')
                break
            else:
                system('python "choice.py"')
                print('未打开该文件！')
                break
    else:
        print('未找到您输入的作业名称！')
else:
    print('没有未完成的作业！\n去休息一下吧！')
    system('pause')''',
          'background' : 'https://img-blog.csdnimg.cn/20200811100802744.jpg',
          'blackboard' : 'https://img-blog.csdnimg.cn/20200811110557793.png',
          'text' : '''尊敬的用户，您好！
欢迎使用 腾飞课堂1.0 软件！

您可以使用此软件进行课堂管理，作业、考试等设备一应俱全。
您可以查看技术文档以学会更多操作！

联系方式：
邮箱： 3362157322@qq.com
QQ： 3362157322
官方网页（在这里查看官方技术文档）： http://pandaoxi.360doc.com/

更多信息：
开发语言：Python
原有账户（格式： [用户名,密码]）：[学生账号01,01],[学生账号02,02],[学生账号03,03]
需求：Windows环境、Python环境、网络
开发者：潘道熹
如果您有困难可以随时联系作者！                                                
        


                    腾飞课堂 开发者
                      2020/8/20''',
          'welcome' : r'''from easygui import textbox

with open('text.txt','r',encoding = 'utf-8') as file:
    text = file.read()
    
textbox('下面是一封给您的信。','腾飞课堂',text = text,codebox = False)''',
          'choice' : r'''from tkinter import Tk,Label,Button
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo,showerror,askyesno
from os import system
from os.path import splitext
from PIL import Image,ImageTk
from sys import exit

title = '线上课平台'
system('chcp 65001 >nul')

window =  Tk()
window.title(title)
window.resizable(0,0)

def homework():
    system('python homework.py')
    window.destroy()
    
def exercise():
    system('python exam.py')
    window.destroy()

def gotoclass():
    system('python class.py')
    window.destroy()
    
img = ImageTk.PhotoImage(file = 'background.jpg')
text = '您好，尊敬的客户！\n请选择服务：'

Label(window,image = img,text = text,foreground = 'blue',font = ('华文新魏',35),compound = 'center').pack()
Button(window,bd = 0,text = '做作业',command = homework,font = ('楷体',20)).place(x = 192,y = 405)
Button(window,bd = 0,text = '去练习',command = exercise,font = ('楷体',20)).place(x = 392,y = 405)
Button(window,bd = 0,text = '去上课',command = gotoclass,font = ('楷体',20)).place(x = 592,y = 405)

window.mainloop()''',  
          'login' : r'''from easygui import msgbox,multpasswordbox,buttonbox,passwordbox
from os import system,name

title = '腾飞线上课平台'
users = [
         ['学生账号01','01'],
         ['学生账号02','02'],
         ['学生账号03','03'],
         ]

system('chcp 65001 >nul')
def login():
    choice = buttonbox('欢迎使用线上课平台！\n如果您需要进行操作，请先登录或注册！',title,('登录','注册'))

    if (choice == '登录'):
        loginUser = []
        loginUser = multpasswordbox('请输入用户名和密码：',title,('用户名：','密码：'))
    
        for user in range(len(users)):
            if (loginUser[0] == users[user][0]) and (loginUser[1] == users[user][1]):
                msgbox('登录成功！按下下面的按钮即可跳转到主页面！',title,'确定')
                system('cd "files" & call "choice.py"')
                break
        else:
            msgbox('用户名或密码错误！',title,'确定')
                
    elif (choice == '注册'):
        register = []
        register = multpasswordbox('请填写下面的注册信息：',title + ' - 注册',('用户名：','密码'))    
        ispassword = passwordbox('请确认密码：',title + ' - 注册')
        if (register[1] == ispassword):
            msgbox('注册成功！',title,'确定')
        else:
            msgbox('两次输入密码不同！',title,'确定')
            
        with open('register.txt','w+') as fileWrite:
            fileWrite.write('{0}\n{1}\n\n'.format(register[0],register[1]))
        users.append([register[0],register[1]])
        system('cd "files" & call "choice.py"')
        
    else:
        exit()
        
if (__name__ == '__main__' and name == 'nt'):
    login()''',
          'ctr_bg' : 'https://img-blog.csdnimg.cn/20200819074310688.jpg',
          'ctr' : r'''from tkinter import Tk,Label
from os import system
from PIL import ImageTk
from tkinter.messagebox import showinfo,showerror
from random import choice

#请在这里更改学生的名字以点名，格式就像下面的
list = ['学生1','学生2','学生3']
student = choice(list)

def say(student):
    with open('say.vbs','w+',encoding = 'ANSI') as file:
        file.write('set say = CreateObject("SaPi.SpVoice")\nsay.Speak "请{0}同学回答老师的问题！"'.format(student))
    system('call "say.vbs" & del /q /s /f "say.vbs" >nul')    
    
say(student)
window = Tk()
window.resizable(0,0)
window.title('点名系统')
bg = ImageTk.PhotoImage(file = 'ctr_bg.jpg')
Label(window,image = bg).pack()
text = Label(window,text = '请 ' + student + ' 同学回答老师的问题',font = ('楷体',20),foreground = 'black')
text.pack()
text.place(x = 200,y = 270)
window.mainloop()''',
          'teacher' : r'''from easygui import buttonbox,msgbox,textbox,enterbox,multenterbox
from os import system,name
from sys import path
from requests import get

class_url = 'http://pub.idqqimg.com/pc/misc/groupgift/fudao/pc/EduLiteInstall_1.0.3.34_sign.exe'
download_name = 'Tencent Classroom Software 1.0.3.34.exe'
currentPath = path[0]
title = '线上课平台 - 教师版'
button = '确定'

def download():
    getFile = get(class_url)
    with open(download_name,'wb') as download:
        download.write(getFile)

def new_exam():
    data = []
    data = multenterbox('请设置考试的信息：',title,('考试科目：','考试主题：','主考老师：','考试介绍：'))
    text = textbox('请输入考试的代码：',title,codebox = True,text = 'from easygui import *\nfrom os import system')
    code = """# *-* coding : utf-8 *-*
dict = {
    'subject' : '%s',
    'theme' : '%s',
    'teacher' : '%s',
    'introduce' : '%s',
    'application' : '%s'
        }
%s
""" % (data[0],data[1],data[2],data[3],'线上课平台-2020年8月新版',text)
    with open(data[1] + '.py','w+',encoding = 'utf-8') as file:
        file.write(code)
    msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\topic文件夹下即可被学生发现！'.format(currentPath),title,button)

def contact():
    askyn = buttonbox('联系我们：\n开发者：潘道熹\nQQ：3362157322\n网址：https://me.csdn.net/PanDaoxi2020\n邮箱：3362157322@qq.com\n当前系统版本：1.0',title,('联系作者邮箱','打开官方网页'))
    if askyn == '联系作者邮箱':
        system('start iexplore -incognito "http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=c0BARUFCRkRAQUEzAgJdEBwe"')
    elif askyn == '打开官方网页':
        system('start iexplore "http://pandaoxi.360doc.com/"')
        system('start iexplore "https://me.csdn.net/PanDaoxi2020"')
    
def new_homework():
    letter = textbox('请在下方写入您的作业Python代码：',title,text = 'from easygui import *\n',codebox = True)
    msgbox('# 这是您写入的Python代码\n\n{0}'.format(letter),title,button)
    homework_name = enterbox('请您为该作业命名：',title)
    if homework_name != None:
        with open('{0}.py'.format(homework_name),'w+',encoding = 'utf-8') as file:
            file.write(letter)
        msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\homework文件夹下即可被学生发现！'.format(currentPath),title,button)
    elif len(homework_name) >= 20:
        msgbox('名字超长！最多20个字符！',title,button)
    elif len(homework_name) <= 2:
        msgbox('名字超短！最少2个字符！',title,button)
    
def new_class():
    class_data = []
    class_data = multenterbox('请输入您要创建的课程信息：',title,('您要上课的主题：','课程URL：'))
    yn = buttonbox('您是否需要下载：腾讯课堂（Tencent Classroom Software）？',title,('下载','取消'))
    
    if yn == '下载':
        download()
    elif yn == '取消':
        pass
    else:
        msgbox('请选择一个按钮！',title,'确定')
        
    code = """# *-* coding : utf-8 *-*
from os import system,name
from easygui import buttonbox,msgbox

title = '去上课'
select = buttonbox('您的课程信息是否是： {1}。 ？',title,('是','否'))
list = [__name__,name]

def yes():
    system('start "C:\\Program Files\\Internet Explorer\\iexplore.exe" "{0}"')

def main():
    if (select == '是'):
        yes()
    elif (select == '否'):
        exit()
    else:
        msgbox('请选择一个按钮！',title,'确定')

if list[0] == "__main__" and list[1] == "nt":
    main()""".format(class_data[1],class_data[0])
    
    with open('{0}.py'.format(class_data[0]),'w+',encoding = 'utf-8') as file:
        file.write(code)
    msgbox('创建成功，文件在当前目录下： {0} 。\n请将此文件移动到：files\\class文件夹下即可被学生发现！'.format(currentPath),title,button)

def ctr():
    system('cd "点名器" & call "ctr.py"') 
    
def main():    
    choice = buttonbox('您好，欢迎使用线上课平台！\n此程序适用于教师版。\n您可以通过此插件选择一些关于学生版的服务！',title,('新建作业','新建课程','新建练习','点名系统','联系作者'))
    
    if choice == '新建作业':
        new_homework()
    elif choice == '新建课程':
        new_class()
    elif choice == '新建练习':
        new_exam()
    elif choice == '点名系统':
        ctr()
    elif choice == '联系作者':
        contact()
    else:
        msgbox('请选择其中的一个按钮！',title,button)

if __name__ == '__main__' and name == 'nt':
    main()
''',
            }

def create(cn):
    ec = 'utf-8'
    types = 'w+'
    dirs = cn + '/files/'
    bg = get(coding['background'])
    bb = get(coding['blackboard'])
    
    with open(dirs + 'homework.py',types,encoding = ec) as h:
        h.write(coding['homework'])
    
    with open(dirs + 'class.py',types,encoding = ec) as c:
        c.write(coding['class'])
        
    with open(dirs + 'exam.py',types,encoding = ec) as e:
        e.write(coding['exam'])
    
    with open(dirs + 'background.jpg','wb') as img:
        img.write(bg.content)
        
    with open(dirs + 'welcome.py',types,encoding = ec) as w:
        w.write(coding['welcome'])
        
    with open(dirs + 'blackboard.png','wb') as img:
        img.write(bb.content)
        
    with open(dirs + 'text.txt',types,encoding = ec) as t:
        t.write(coding['text'])
    
    with open(dirs + 'choice.py',types,encoding = ec) as c:
        c.write(coding['choice'])
    
    with open(cn + '/login.py',types,encoding = ec) as l:
        l.write(coding['login'])
        
    showinfo('通知','安装完成！\n您安装的位置是：\n{0}\n\n请先查看文件\n{1}/files/welcome.py'.format(cn,cn))
    pass

def teacher(cn):
    ctr = cn + '/教师版/点名器'
    dir = cn + '/教师版/'
    types = 'w+'
    ec = 'utf-8'
    ctr_bg = get(coding['ctr_bg'])
    makedirs(ctr)
    
    with open(dir + 'teacher.py',types,encoding = ec) as t:
        t.write(coding['teacher'])
        
    with open(dir + '/点名器/ctr.py',types,encoding = ec) as ctr:
        ctr.write(coding['ctr'])
    
    with open(dir + '/点名器/ctr_bg.jpg','wb') as ctr_img:
        ctr_img.write(ctr_bg.content)
    
def install():
    try:
        target = askdirectory(title = '请选择安装目录')
        dir = target + '/腾飞线上课平台'
        if target != 0:
            teacher_yn = askyesno('腾飞课堂','是否安装教师版？')
            if teacher_yn == True:
                teacher(dir)
            else:
                pass
            makedirs('{0}/files/homework'.format(dir))
            mkdir('{0}/files/class'.format(dir))
            mkdir('{0}/files/topic'.format(dir))
            create(dir)
        else:
            showerror('错误','请上传一个安装目录的路径。')
    except FileExistsError:
        showerror('错误','出现了错误，请您关闭程序后再重新打开。')
    
window = Tk()
window.withdraw()
system('color 0a')
print(data)
yn = askyesno('腾飞课堂','欢迎使用 腾飞课堂 安装向导！\n您是否要继续安装 腾飞课堂1.0 ？\n\n介绍：\n腾飞课堂1.0实现了简单的课堂系统，可以上课、做作业、考试。')
if yn == True:
    install()
else:
    pass
window.mainloop()

```
然后新建一个批处理文件，输入以下命令：
```powershell
@echo off
chcp 65001 >nul
call "dist\setup.exe"
exit
```
在![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813104658330.png#pic_center)
这里搜索“Windows PowerShell”，输入命令如下：

```powershell
cd "安装包目录"
pyinstaller setup.py -F
```
等一会后，我们就可以在文件夹里发现：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200813110031137.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
在文件夹`dist`里面可以看到`setup.exe`这个文件，大功告成。

如果大家需要完整的，可以从这里下载：`https://download.csdn.net/download/PanDaoxi2020/12726543`！
