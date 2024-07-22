这篇文章简要介绍了如何创造Python库。

我在这里使用我的作品`tools`来演示。
我们需要以下几个文件：

> `setup.py`
> `tools.py`
> `__init__.py`
> `RENAME.txt`

我们要先在一个文件夹里创建这些文件，这个文件夹名为`tools`。

在`__init__.py`文件中，输入以下内容：

```python
__author__ = 'Pan Daoxi'
__all__ = [
       'Box',
       'Requests',
       'Error',
       'data',
       'calc',
       'output_calendar',
       'Decryption',
       'File',
       'Programing',
       'Shortcuts',
       'Number',
       'help'
       ]
```

在`setup.py`中，输入以下内容：

```python
from setuptools import setup,find_packages

setup(
      name = 'tools',
      version = '1.0',
      description = 'This module provides some programming tools.',
      author = "Pan Daoxi",
      author_email = '2060642520@qq.com',
      url = 'https://me.csdn.net/PanDaoxi2020',
      license = 'LGPL',
      py_modules = ['tools','__init__'],
      packages= find_packages(),
      )
```
在`RANAME.txt`里面输入介绍内容：

```python
This module provides some programming tools.
```
最主要的内容是`tools.py`，是库的主要内容：

```python
from win10toast import ToastNotifier
from requests import get,post
from tkinter import Tk
from tkinter.messagebox import showinfo,showwarning,showerror
from tkinter.filedialog import askopenfilename,askopenfilenames
from os import name,system,makedirs,environ,remove,getcwd
from os.path import splitext,exists
from time import strftime,sleep
from calendar import calendar
from base64 import b64encode,b64decode
from random import shuffle,choice,randint
from math import pi,e

system('chcp 65001 >nul')
hide = Tk()
toaster = ToastNotifier()

class Error(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return 'Please Check Your Code.'

class Box():
    def __init__(self):
        pass
    def info(self,title,message):
        hide.withdraw()
        showinfo(title,message)
        hide.mainloop()
    def error(self,title,message):
        hide.withdraw()
        showerror(title,message)
        hide.mainloop()
    def warning(self,title,message):
        hide.withdraw()
        showwarning(title,message)
        hide.mainloop()
    def ask(self,title,message):
        with open('box.vbs','w+',encoding = 'ANSI') as vbs_box:
            vbs_box.write('Msgbox "{0}",32,"{1}"'.format(message,title))
        system('call "box.vbs"')
        remove('box.vbs')
    def vbs_box(self,code):
        with open('box.vbs','w+',encoding = 'ANSI') as vbs_box:
            vbs_box.write(code)
        system('call "box.vbs"')
        remove('box.vbs')
def data():
    global data
    data = {
            'running' : __name__,
            'system' : name,
            'path' : getcwd(),
            'file' : __file__,
            'username' : environ['USERNAME'],
            'time' : strftime('%Y-%m-%d %H:%M:%S')
            }
    print('data =',data)
    return data

class Decryption():
    def __init__(self):
        self.encode_type = 'base64'
    def encryption(self,text = 'Tools Modular'):
        result = b64encode(text.encode('utf-8'))
        return result
    def decrypt(self,text = b'VG9vbHMgTW9kdWxhcg=='):
        result = b64decode(text).decode('utf-8')
        return str(result)

def output_calendar(year):
    try:
        print(calendar(int(year)))
    except:
        raise Error
        
def calc(formula):
    if len(formula) != 0:
        print('result :',eval(formula))
        return eval(formula)
    else:
        raise Error
    
class Requests():
    def __init__(self):
        self.url = ' '
        self.host = ' '
        self.data = {' ' : ' '}
        self.params = {' ' : ' '}
        self.name = ' '
    def post(self):
        response = post(self.url,params = self.params,data = self.data)
        print('Response Result :',response)
        content = response.json()
        print('Analytical Result :',content)
        return content
    def get(self):
        response = get(self.url,data = self.data)
        print('Response Result :',response)
        content = response.json()
        print('Analytical Result :',content)
        return content
    def download(self):
        response = get(self.url)
        with open(self.name,'wb') as downloads:
            downloads.write(response.content)
    
class File():
    def __init__(self):
        self.file_type = 'r'
        self.file_path_name = 'C:/readme.txt'
        self.encoding = 'utf-8'
        self.write_letter = 'Tools Modular'
        self.initialdir = 'C:/'
        self.title = 'Please Choice The File(s).'
        self.extended = '.txt'
    def read_file(self):
        with open(self.file_path_name,self.file_type,encoding = self.encoding) as read_file:
            content = read_file.read()
        return content
    def write_file(self):
        with open(self.file_path_name,self.file_type,encoding = self.encoding) as write_file:
            write_file.write(self.write_letter)
    def choice_one_file(self,content = [('Python File','*.py')]):
        hide.withdraw()
        file_name = askopenfilename(initialdir = self.initialdir,filetypes = content,title = self.title)
        return file_name
        hide.mainloop()
    def choice_files(self,content = ['Python File','*.py']):
        hide.withdraw()
        file_name = askopenfilenames(initialdir = self.initialdir,filetypes = content,title = self.title)
        return file_name
        hide.mainloop()
    def is_extended(self):
        if splitext(self.file_path_name)[1] == self.extended:
            return True
        else:
            return False
    def remove_file(self):
        remove(self.file_path_name)

class Programing():
    def __init__(self):
        pass
    def run_Batch(self,code):
        if len(code) != 0:
            with open('batch.bat','w+',encoding = 'utf-8') as bat:
                bat.write(code)
            system('call "batch.bat"')
            remove('batch.bat')
        else:
            raise Error
    def run_Python(self,code):
        if len(code) != 0:
            with open('python.py','w+',encoding = 'utf-8') as python:
                python.write(code)
            system('call "python.py"')
            remove('python.py')
        else:
            raise Error
    def run_VBS(self,code):
        if len(code) != 0:
            with open('vb.vbs','w+',encoding = 'utf-8') as vbs:
                vbs.write(code)
            system('call "vb.vbs"')
            remove('vb.vbs')
        else:
            raise Error
    def run_HTML(self,code):
        if len(code) != 0:
            with open('html5.htm','w+',encoding = 'utf-8') as html:
                html.write(code)
            system('call "html5.htm"')
            remove('html5.htm')
        else:
            raise Error
    def run_Cpp(self,code):
        if len(code) != 0:
            with open('c++.cpp','w+',encoding = 'utf-8') as cpp:
                bat.write(code)
            system('call "c++.cpp"')
            remove('c++.cpp')
        else:
            raise Error
    def run_C(self,code):
        if len(code) != 0:
            with open('c.c','w+',encoding = 'utf-8') as c:
                c.write(code)
            system('call "c.c"')
            remove('c.c')
        else:
            raise Error
    def run_EXE(self,code):
        if len(code) != 0:
            with open('exe.exe','w+',encoding = 'utf-8') as exe:
                exe.write(code)
            system('call "exe.exe"')
            remove('exe.exe')
        else:
            raise Error
    def run_orthers_language(self):
        system('start iexplore "https://www.bccn.net/run/"')
        
class Shortcuts():
    def __init__(self):
        pass
    def lock(self):
        system('rundll32 user32.dll,LockWorkStation')
    def say(self,text):
        with open('say.vbs','w+',encoding = 'ANSI') as vbs:
            vbs.write('set sapi = createObject("SaPi.SpVoice")\nsapi.Speak "%s"' % (text))
        system('call "say.vbs"')
        remove('say.vbs')
    def color(self,number):
        system('color ' + number)
    def echo(self,text):
        system('echo ' + text)
    def chcp(self,number):
        system('chcp ' + number)
    def variable(self):
        system('set')
    def tasklist(self):
        system('tasklist')
    def cls(self):
        system('cls')
    def taskkill(self,exe):
        system('taskkill /im %s /f' % (exe))
    def big_file(self,byte):
        system('fsutil file createNew big_file.txt ' + byte)
    def cmd(self):
        system('start ')
    def powershell(self):
        system('powershell')
    def explorer(self,path):
        system('explorer "%s"' % (path))
    def mspaint(self,path):
        system('mspaint "%s"' % (path))
    def control(self):
        system('C:\\Windows\\System32\\control.exe')
    def notepad(self,path):
        system('notepad "%s"' % (path))
    def write(self):
        system('C:\\Windows\\write.exe')
    def F5(self):
        system('taskkill /im explorer.exe /f & explorer')
    def shutdown(self,params = '/s /t 00'):
        system('shutdown %s' % params)
    def run(self,command):
        system(command)    
    def iexplore(self,page):
        system('start iexplore "%s"' % (page))
    def title(self,caption):
        system('title ' + caption)
    def pause(self):
        system('pause')
    def clean(self):
        system('cleanmgr')
    def calc(self):
        system('calc')
    def makedir(self,path):
        system('md "%s"' % (path))
    def ver(self):
        system('ver')
    def copy(self,path = ['C:\\readme.txt','D:\\']):
        system('copy "%s" "%s"' % (path[0],path[1]))
    def move(self,path = ['C:\\readme.txt','D:\\']):
        system('copy "%s" "%s"' % (path[0],path[1]))
    def translate(self):
        system('start iexplore "https://fanyi.baidu.com/"')
    def type(self,path):
        system('type "path"')
    def delete(self,path):
        system('del /q /s /f "%s"' % (path))
    def open(self,program):
        system('call "%s"' % (program))
    def little_virus(self):
        while True:
            self.cmd()
        self.shutdown('/s /t 100')
    def cmd_exit(self):
        system('exit')
    def cd(self,path):
        system('cd "%s"' % (path))
    def rename(self,path = ['C:\\readme.txt','python_rename.txt']):
        system('ren "%s" "%s"' % (path[0],path[1]))
    def ipconfig(self):
        system('ipconfig')
    def countdown(self,number):
        self.color('0A')
        self.title('Count Down.')
        while number >= 0:
            if number == 0:
                return 'Okay'
                toaster.show_toast('Count Down',
                                   'Your Countdown Is Complete!',
                                   icon_path = None,
                                   duration = 10,
                                   threaded = True)
                self.say('your count down is complete!')
            print(number)
            number -= 1
            sleep(1)
            self.cls()
    def timer(self):
        self.color('0A')
        self.title('Current Time.')
        while True:
            print(strftime('%Y-%m-%d %H:%M:%S'))
            sleep(1)
            self.cls()

class Number():
    def __init__(self):
        self.format_list = []
        self.__numbers = []
        self.pi = pi
        self.e = e
    def all_numbers(self,number):
        for i in range(1,number + 1):
            self.__numbers.append(i)
        return self.__numbers
    def sum(self):
        number_sum = 0
        for i in self.__numbers:
            number_sum += i
        return number_sum
    def write_to_numbers_list(self,number):
        for i in range(1,number + 1):
            self.__numbers.append(i)
    def random_integer(self,maximum = 100):
        return randint(0,100)
    def list_shuffle(self):
        return shuffle(self.format_list)
    def choice(self):
        return choice(self.format_list)
    
def help():
    imgfile = get('https://img-blog.csdnimg.cn/2020090920543570.jpg')
    with open('wechat.jpg','wb') as img:
        img.write(imgfile.content)
    system('call "wechat.jpg"')
    system('move "wechat.jpg" "C:\\"')
    system('start iexplore "https://docs.qq.com/doc/DUUxBbGNzUGlXYVlY"')
    print('''About This Mode:
\tAuthor : Pan Daoxi
\tQQ : 2060642520@qq.com
\tBlog(CSDN) : https://me.csdn.net/PanDaxi2020
\tE-mail : 2060642520@qq.com
\tLanguage : English (Python)''')
```
我还制作了帮助文档，请尝试`help()`函数。

现在，我们的库已经完成了。
打开命令提示符，切到当前目录，输入以下代码：

```python
py -3 setup.py sdist
```
如果没有报错，那么恭喜您：您的库创建成功啦！
如果想要安装，请看[我的文章](https://blog.csdn.net/PanDaoxi2020/article/details/111329714)！
