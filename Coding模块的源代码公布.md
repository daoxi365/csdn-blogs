```python
from os import system,name
from os.path import exists
from time import sleep,strftime,localtime,time
from tkinter import Tk,Label
from easygui import enterbox,buttonbox,textbox,msgbox
from sys import path

'''The coding library can help you run other code on Python!'''

system('chcp 65001 >nul')
print('Welcome to Coding Library ! \t current state : {0}'.format(__name__))
print('current coordinate : {0} \t current system : {1}'.format(path[0],name))
print()
file = []
data = ['utf-8 (65001)','2.2',__name__,path[0],name]
inks = ['calc','regedit','powershell','explorer','iexplore','see','cmd','title','color','echo','read','start','help','cls','md','cd','copy','delete','dir','cmd_exit','pause','lock','shutdown','taskkill','ping','sleep']
title = 'Coding Library'
button = 'Okay'

class Vbs_Code():
    def __init__(self):
        self.file_name = 'vbs_program.vbs'
        self.program = 'vbs'
        self.encoding = 'ANSI'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as vbs_file:
            vbs_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del "' + str(self.file_name) + '"')

class Batch_Code():
    def __init__(self):
        self.file_name = 'batch_program.bat'
        self.program = 'batch'
        self.encoding = 'UTF-8'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as batch_file:
            batch_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del /q /s /f "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del /q /s /f "' + str(self.file_name) + '"')
        
class HTML_Code():
    def __init__(self):
        self.file_name = 'html_program.html'
        self.program = 'HTML5.0'
        self.encoding = 'UTF-8'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as html_file:
            html_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del /q /s /f "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del /q /s /f "' + str(self.file_name) + '"')

class JavaScript_Code():
    def __init__(self):
        self.file_name = 'javascript_program.js'
        self.program = 'javascript'
        self.encoding = 'UTF-8'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as js_file:
            js_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del /q /s /f "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del /q /s /f "' + str(self.file_name) + '"') 

class CSS_Code():
    def __init__(self):
        self.file_name = 'css_program.css'
        self.program = 'css'
        self.encoding = 'UTF-8'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as css_file:
            css_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del /q /s /f "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del /q /s /f "' + str(self.file_name) + '"')

class Python_Code():
    def __init__(self):
        self.file_name = 'python_program.py'
        self.program = 'python'
        self.encoding = 'UTF-8'
    def new(self,code):
        with open(str(self.file_name),'w+',encoding = str(self.encoding)) as css_file:
            css_file.write(str(code))
        sleep(2)
    def call(self):
        if exists(str(self.file_name)) == True:
            system('call "' + str(self.file_name) + '"')
        else:
            system('del /q /s /f "' + str(self.file_name) + '"')
        sleep(2)
    def delete(self):
        system('del /q /s /f "' + str(self.file_name) + '"')

class Error(Exception):
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Sorry, something went wrong, please check your code.'

def calc(math):
    try:
        calc = eval(math)
        msgbox('Calculation results: \n\n{0}'.format(calc),title,button)
        return calc
    except ZeroDivisionError:
        msgbox('Error : \nZeroDivisionError\n\nPlease try again.',title,button)
    except ValueError:
        msgbox('Error : \nValueError\n\nPlease try again.',title,button)
    except NameError:
        msgbox('Error : \nValueError\n\nPlease try again.',title,button)
    except SyntaxError:
        msgbox('Error : \nSyntaxError\n\nPlease try again.',title,button)
        
class Shortcuts():
    def __init__(self):
        self.type = 'shortcuts'
    def calc(self):
        system('calc')
    def regedit(self):
        system('regedit')
    def powerShell(self):
        system('powershell')
    def explorer(self,path):
        system('explorer "{0}"'.format(path))
    def iexplore(self,web):
        system('start iexplore "{0}"'.format(web))
    def see(self):
        system('set')
    def cmd(self):
        system('start "%windir%\\System32\\cmd.exe"')
    def title(self,title_text):
        system('title {0}'.format(title_text))
    def color(self,attr):
        system('color {0}'.format(attr))
    def echo(self,text):
        system('echo {0}'.format(text))
    def read(self,path):
        system('type {0}'.format(path))
    def start(self,path_or_Ink):
        system('call {0}'.format(path_or_Ink))
    def help(self):
        system('help')
    def cls(self):
        system('cls')
    def md(self,folder):
        system('md "{0}"'.format(folder))
    def cd(self,path):
        system('cd "{0}"'.format(path))
    def copy(self,paths):
        system('xcopy "{0}" "{1}"'.format(paths[0],paths[1]))
    def delete(self,file):
        system('del /q /s /f "{0}"'.format(file))
    def dir(self,dir):
        system('dir /s "{0}"'.format(dir))
    def pause(self):
        system('pause')
    def cmd_exit(self):
        system('exit')
    def lock(self):
        system('rundll32.exe user32.dll,LockWorkStation')
    def shutdown(self,command):
        system('shutdown {0}'.format(command))
    def taskkill(self,program):
        system('taskkill /im {0} /f /t'.format(program))
    def ping(self,web,number):
        system('ping {0} /n {1}'.format(web,number))
    def sleep(self,seconds):
        system('ping 127.0.1 /n {0}'.format(seconds))

class Help():
    def __init__(self):
        self.color = 'blue'
        self.font = ('Courier New',18)
        self.justify = 'left'
        self.Vbs_Code = '''This class can help you call VBS code.

usage method:

import coding 
# Import coding Library.
code = coding.Vbs_Code() 
# Using variables to call objects of this class.
code.file_name = "MyFile.vbs" 
# Rename file.
code.new('Msgbox "Hello,world!",64,"Coding Library"') 
# Create a new file and write code.
code.call() 
# Run code.
code.delete() 
# Delete code.

Please run this program as an administrator.
If no error is reported, a text box with the words "Hello, world" will pop up.
(Anti virus software may intercept)'''
        self.Batch_Code = '''This class can help you call Batch code.

usage method:

import coding 
# Import coding Library.
code = coding.Batch_Code() 
# Using variables to call objects of this class.
code.file_name = "MyFile.bat" 
# Rename file.
code.new('echo Hello,world!') 
# Create a new file and write code.
code.call() 
# Run code.
code.delete() 
# Delete code.

Please run this program as an administrator.'''
        self.Python_Code = '''This class can help you call Python code.

usage method:

import coding 
# Import coding Library.
code = coding.Python_Code() 
# Using variables to call objects of this class.
code.file_name = "MyFile.py" 
# Rename file.
code.new() 
# Create a new file and write code.
code.call() 
# Run code.
code.delete() 
# Delete code.

Please run this program as an administrator.'''
        self.front_end = '''This class can help you call HTML,JavaScript,and CSS code.

usage method:

import coding 
# Import coding Library.
code = coding.HTML_Code() 
# Using variables to call objects of this class.
code.file_name = "MyFile.html" 
# Rename file.
code.new('<center><font face="Microsoft YaHei" color="Red" size="20">Hello,world!</font></center>') 
# Create a new file and write code.
code.call() 
# Run code.
code.delete() 
# Delete code.'''
        self.allInk = inks
        self.InkHelp_Text = '''We sort out some common CMD commands.

usage method:

import coding
ink = coding.Shortcuts()
ink.cmd()

Please run this program as an administrator.

All function:
{0}'''.format(self.allInk)
    def VbsCodeHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = self.Vbs_Code,
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()
    def BatchCodeHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = self.Batch_Code,
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()
    def PythonCodeHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = self.Python_Code,
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()
    def FrontEndHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = self.front_end,
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()
    def calcHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = '''Do some simple calculations.''',
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()
    def InkHelp(self):
        window = Tk()
        window.resizable(0,0)
        window.title(title)
        Lab = Label(window,
                    text = self.InkHelp_Text,
                    font = self.font,
                    foreground = self.color,
                    justify = self.justify)
        Lab.pack()
        window.mainloop()

class GUI():
    def __init__(self):
        self.title = 'Coding Library - GUI'
        self.button = 'Okay'
        self.temp = 'temp.py'
        self.encoding = 'utf-8'
        self.type = 'w+'
        self.file_name = ' '
    def calc(self):
        try:
            math = enterbox('Enter a formula : ',self.title)
            calc = eval(math)
            msgbox('Output results : \n\n{0}'.format(calc),self.title,self.button)
        except ZeroDivisionError:
            msgbox('Error : \nZeroDivisionError\n\nPlease try again.',self.title,self.button)
        except ValueError:
            msgbox('Error : \nValueError\n\nPlease try again.',self.title,self.button)
        except NameError:
            msgbox('Error : \nValueError\n\nPlease try again.',self.title,self.button) 
    def enterCode(self,type):
        if type == 'VBS':
            self.file_name = 'MyFile.vbs'
            self.initText = "'Please enter your code below!"
            input = textbox('Coding Library -- GUI \n',self.title,text = self.initText,codebox = True)
            with open(self.file_name,self.type,encoding = self.encoding) as temp:
                temp.write(input)
            sleep(2)
            system('call "' + str(self.file_name) + '"')
            sleep(5)
            system('del /q /s /f ' + str(self.file_name))
        elif type == 'Batch':
            self.file_name = 'MyFile.bat'
            self.initText = "::Please enter your code below!"
            input = textbox('Coding Library -- GUI \n',self.title,text = self.initText,codebox = True)
            with open(self.file_name,self.type,encoding = self.encoding) as temp:
                temp.write(input)
            sleep(2)
            system('call "' + str(self.file_name) + '"')
            sleep(5)
            system('del /q /s /f ' + str(self.file_name))
        elif type == 'Python':
            self.file_name = 'MyFile.py'
            self.initText = "#Please enter your code below!"
            input = textbox('Coding Library -- GUI \n',self.title,text = self.initText,codebox = True)
            with open(self.file_name,self.type,encoding = self.encoding) as temp:
                temp.write(input)
            sleep(2)
            system('call "' + str(self.file_name) + '"')
            sleep(5)
            system('del /q /s /f ' + str(self.file_name))
        elif type == 'HTML':
            self.file_name = 'MyFile.html'
            self.initText = "<!--Please enter your code below.-->"
            input = textbox('Coding Library -- GUI \n',self.title,text = self.initText,codebox = True)
            with open(self.file_name,self.type,encoding = self.encoding) as temp:
                temp.write(input)
            sleep(2)
            system('call "' + str(self.file_name) + '"')
            sleep(5)
            system('del /q /s /f ' + str(self.file_name))
        else:
            msgbox('The code information was not found!',self.title,self.button)
    
def about():
    author = 'Pan Daoxi'
    date = '2020-6-15'
    url = 'http://pandaoxi2020.360doc.com/'
    version = '2.2'
    email = '3362157322@qq.com'
    description = 'The code library can help you run other code on Python!'
    system('start iexplore "{0}"'.format(url))
    print('author : {0}\tdate : {1}\nurl : {2}\tversion : {3}\nemail : {4}\tdescription : {5}'.format(author,date,url,version,email,description))
    return 'author : {0}\tdate : {1}\nurl : {2}\tversion : {3}\nemail : {4}\tdescription : {5}'.format(author,date,url,version,email,description)
    print()
    for i in inks:
        print(i)
    
class Note():
    def __init__(self):
        self.product = 'Coding Library'
        self.version = '(2.2)'
        self.time = strftime("%Y.%m.%d", localtime())
        self.type = 'txt'
    def write(self,note):
        print(self.time)
        try:
            with open('{0}_{1}_{2} - journal.{3}'.format(self.product,self.version,self.time,self.type),'w+') as note_file:
                note_file.write(note)
        except OSError:
            print('Error!\nPlease try again!\n')
            raise Error
        except SyntaxError:
            print('Error!\nPlease try again!\n')
            raise Error
    def delete(self,note_name):
        system('del /q /s /f "{0}"'.format(note_name))



```

