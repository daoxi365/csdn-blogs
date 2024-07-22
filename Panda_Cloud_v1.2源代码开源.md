大家好，我经过了认真的考虑，决定将我自己的局域网文件储存项目**熊猫云（英文名 Panda Cloud）** 的主要代码开源。
现我已开发至 1.2 版本，可能还有一些缺点，我后面会修改，也欢迎大家提出。

<font color="red" face="仿宋"><b>一定要注意！！我的项目未经允许不得转载！！！仅供学习和参考！！！</b></font>
贴上原来的仓库地址：[我是传送门](https://pandaoxi.coding.net/public/pandaoxi/PanDaoxi/git/files/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud)。

我的项目的内部版本目录树：

```python
D:.
│  Application_Program.zip
│  README.md
│
├─Encryption_Client
│      main.py
│      URL_Generation_Tool.py
│
├─Encryption_Server
│  │  BITURL
│  │  USE.py
│  │
│  ├─files
│  └─panda
│      │  db.sqlite3
│      │  manage.py
│      │
│      └─panda
│          │  asgi.py
│          │  settings.py
│          │  urls.py
│          │  wsgi.py
│          │  __init__.py
│          │
│          └─__pycache__
│                  settings.cpython-36.pyc
│                  urls.cpython-36.pyc
│                  wsgi.cpython-36.pyc
│                  __init__.cpython-36.pyc
│
├─Original_Client
│  │  main.py
│  │  URL_Generation_Tool.py
│  │
│  └─__pycache__
│          URL_Generation_Tool.cpython-36.pyc
│
└─Original_Server
    │  BITURL
    │  USE.py
    │
    ├─files
    └─panda
        │  db.sqlite3
        │  manage.py
        │
        └─panda
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

详细使用文档，请看项目仓库，如果看不懂，请百度翻译（我为了显得高大上整了个全英文……）
# 客户端源代码
## USE.py

```python
# Use this program to open Panda Cloud.
# Copyright 2022 by PanDaoxi.All rights reserved.
# E-mail: 2060642520@qq.com
# See https://pandaoxi.blog.csdn.net/
# Date: 2022-3-20  Time: 13:05

# Import package
from os import name, system
from time import strftime
from socket import socket, AF_INET, SOCK_DGRAM

# Get LAN IP address
def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


# Create server
def main():
    ip = getIP()
    port = strftime("%Y")
    setIP = ip + ":" + port
    print("Get IP address: http://%s/\nPort number: %s (Current year)" % (ip, port))
    print("Creating server, please wait...\n\n")
    system(r"python .\panda\manage.py runserver %s" % setIP)


# Run the current program
if __name__ == "__main__" and name == "nt":
    main()
    input("")
else:
    print(
        "Your PC can't run this program because:\n(1) Non autonomous operation procedures;\n(2) You are not using a Windows operating system.\nIf it cannot be solved, please contact the developer."
    )
    input("")

```
## panda\panda\urls.py
核心服务器软件。源码如下：

```python
# This is Panda Cloud internal code. Don't modify it.
# Copyright 2022 by PanDaoxi.All rights reserved.
from django.shortcuts import HttpResponse
from django.urls import path
from json import dumps
from base64 import b64encode, b64decode ,a85encode ,a85decode
from os import walk, mkdir
from os.path import exists, join
from colorama import *
from hashlib import md5
from random import randint

# The encryption algorithm made by the author.
marks = {}
string = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~@#$%^&*()_+{}|\/{}[]<>?:;"\'=+-.,!'

# Generate character mapping dictionary
for i in range(0,len(string)):
    if i <= 9:
        marks['0' + str(i)] = string[i]
    else:
        marks[str(i)] = string[i]

# Encryption algorithm program - the first generation of DX algorithm.
class __Daoxi():
    def __init__(self):
        self.content = 'Daoxi Encode'.encode()
        self.interval_mark = '-'
        self.ec = 'UTF-8'
        self.marks = marks
    # Encryption program.
    def encode(self):
        try:
            text = a85encode(self.content).decode(self.ec)
            letters = []
            for i in text:
                letters.append(list(marks.keys())[list(marks.values()).index(i)])
            return ['OKAY',self.interval_mark.join(letters)]
        except Exception as e:
            return ['ERROR',e]
    # Decryption program.
    def decode(self):
        try:
            text = self.content.split(self.interval_mark)
            letters = []
                
            for i in text:
                letters.append(marks[i])
            result = ''.join(letters)
            return ['OKAY',a85decode(result.encode(self.ec))]
        except Exception as e:
            return ['ERROR',e]

# Generate objects.
daoxi = __Daoxi()

# ColorAMA Console palette
init()


class Colors:
    def __init__(self):
        pass

    def red(self, s):
        return Fore.RED + s + Fore.RESET

    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    def black(self, s):
        return Fore.BLACK

# Generate objects.
color = Colors()

# Create MD5 texts
getHash = lambda s: md5(s).hexdigest()

# Check whether the file is normal.
if not exists("files"):
    mkdir("files")
if not exists("BITURL"):
    with open("BITURL", "w", encoding="utf-8") as f:
        f.write("")

# When the user accesses IP:PORT/
def main(request):
    # Output the text
    print(color.magenta("A user visited the home page."))
    # Return the HTML code of the home page.
    return HttpResponse("<center><h1><b>PanDa Cloud</b></h1></center><hr>")


# When the user accesses IP:PORT/visitall
def visitall(request):
    filesTemp = []
    # Traverse the file directory and merge the names of each file into the list.
    for root, dirs, files in walk("files", topdown=False):
        for name in files:
            filesTemp.append(name)
    # Merge lists into strings for JSON.
    fileString = "/".join(filesTemp)
    # Output the text
    print(color.yellow("A user gets all the files."))
    return HttpResponse(
        dumps({"state": "okay", "files": b64encode(fileString.encode()).decode()})
    )


# When the user accesses IP:PORT/download
def download(request):
    # Set the file path to judge whether the file you want to download exists.
    want = "files\\" + request.GET.get("file")
    data = {"state": "?", "file": "", "md5": ""}
    # If the file does not exist, an error message is returned.
    if not exists(want):
        data["state"] = "THE FILE NOT FOUND"
    else:
        # Open the file you want, perform Base64 operation, and return the encrypted file field.
        with open(want, "r", encoding="utf-8") as f:
            # Panda Cloud v1.2 Improvement: encrypted storage
            daoxi.content = f.read()
            result = daoxi.decode()
            if result[0] == "OKAY": temp = result[1]
            else: 
                print(color.cyan("Error: File Read Error. %s" % want),result[1])
                return HttpResponse(dumps({'error':'yes',}))
        # Add to dictionary send to JSON.
        data["state"] = "okay"
        data["file"] = b64encode(temp).decode("utf-8")
        data["md5"] = getHash(temp).upper()
        # Output the text
        print(color.blue("A user downloaded the file: %s" % data["md5"]))
    return HttpResponse(dumps(data))


# When the user accesses IP:PORT/upload
def upload(request):
    data = {"state": "", "name": "", "md5": ""}
    # Obtain the network request sent by the client and capture the file uploaded by the user.
    want = request.POST.get("name")
    fileText = request.POST.get("text")
    with open("files/%s" % want, "w", encoding="utf-8") as f:
        # Panda Cloud v1.2 Improvement: encrypted storage.
        daoxi.content = b64decode(fileText.encode())
        text = daoxi.encode()[1]
        md5Text = getHash(text.encode()).upper()
        f.write(text)
    # Output information: a file is uploaded here.
    print(color.red("The user uploaded a file: %s" % md5Text))
    # Return request.
    data["state"] = "okay"
    data["name"] = want
    data["md5"] = md5Text
    return HttpResponse(dumps(data))


# When the user accesses IP:PORT/biturl
def biturl(request):
    want = request.GET.get("url")
    # Randomly generate a 6-character string.
    temp = []
    for i in range(0, 6):
        temp.append(
            chr([randint(65, 90), randint(97, 122)][randint(0, 1)])
        )
    tempS = "".join(temp)
    # Write short URL.
    biturl = "%s\n" % tempS
    with open("BITURL", "a", encoding="utf-8") as f:
        f.write("%s <=> %s" % (want, biturl))
    print(color.magenta("A user generated a short URL, numbered %s" % tempS))
    return HttpResponse(
        dumps(
            {
                "text": "okay",
                "biturl": "readurl?url=%s" % tempS,
            }
        )
    )


# When the user accesses IP:PORT/readurl
def readurl(request):
    # Read URL.
    with open("BITURL", "r", encoding="utf-8") as f:
        a = f.read()
    b = a.splitlines()
    c = {}
    d = ""
    e = []
    for i in b:
        d = i
        e = d.split(" <=> ")
        c[e[1]] = e[0]
    want = request.GET.get("url")
    # Open URL.
    if want in c.keys():
        print(color.magenta("A user visited a short web address, numbered %s" % want))
        return HttpResponse(' <meta http-equiv="refresh" content="0;url=%s">' % c[want])
    else:
        return HttpResponse("<h1><b>Invalid link.</b></h1>")


# Url Patterns
urlpatterns = [
    path("", main),
    path("visitall", visitall),
    path("download", download),
    path("upload", upload),
    path("biturl", biturl),
    path("readurl", readurl),
]

```

# 客户端

```python
# Import package.
from requests import post, get
from tkinter import Tk
from tkinter.filedialog import *
from os import remove, environ, name, system
from os.path import exists, splitext
from time import strftime
from easygui import *
from socket import socket, AF_INET, SOCK_DGRAM
from base64 import b64encode, b64decode
from sys import exit
from re import compile
from webbrowser import open as openW

# Declare the settings of variables and packages that the program depends on.
title = "Panda Cloud (Client)"
hide = Tk()
hide.withdraw()
desktop = environ["USERPROFILE"] + "\\Desktop"

# Declare the settings of variables and packages that the program depends on.
def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


# First, use file search to obtain the server. If not, use the LAN IP of the current computer.
if exists("url"):
    with open("url", "r", encoding="utf-8") as f:
        ip = f.read()
else:
    ip = "http://%s:%s/" % (getIP(), strftime("%Y"))

# File upload function
def upload():
    upd = askopenfilename(title=title, filetypes=[("All Files", "*.*")])
    with open(upd, "rb") as f:
        temp = b64encode(f.read()).decode()
    up = upd.split("/")
    data = {
        "name": up[len(up) - 1],
        "text": temp,
    }
    res1 = post(ip + "upload", data=data).json()["state"]
    if res1 == "okay":
        msgbox("File upload succeeded.", title)


# File download function
def download():
    res1 = get(ip + "visitall").json()["files"]
    file_list = b64decode(res1.encode()).decode().split("/")
    if res1 != "":
        cho = choicebox("Please select the file to download.", title, choices=file_list)
        res2 = get(ip + "download?file=%s" % cho).json()
        fileText = b64decode(res2["file"].encode())
        types = splitext(cho)[1]
        dow = asksaveasfilename(
            title=title,
            filetypes=[("All Files", types)],
            initialfile=cho,
            initialdir=desktop,
        )
        with open(dow, "wb") as f:
            f.write(fileText)
        msgbox("File download succeeded.", title)
    else:
        msgbox("You haven't uploaded any files yet. Please upload one first.", title)

# Short URL function
def biturl():
    url = enterbox("Enter the original URL you need to generate a short URL:", title)
    comp = r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
    if not compile(url):
        msgbox("The URL you entered is incorrect. Please re-enter it.", title)
        exit()
    res1 = get(
        ip + "biturl",
        params={
            "url": url,
        },
    ).json()
    if res1["text"] == "okay":
        bitu = ip + res1["biturl"]
        msgbox(
            "Your short URL was generated successfully! You can visit the following website.\n\nOriginal website: %s\nShortened URL: %s"
            % (url, bitu),
            title,
        )


# Main function (task assignment function)
def main():
    t = ["File Upload", "File Download", "Short URL", "About", "Switch Server", "Exit"]
    cho = buttonbox("Please select the service you need.\nServer: %s" % ip, title, t)
    if cho == t[0]:
        upload()
    elif cho == t[1]:
        download()
    elif cho == t[2]:
        biturl()
    elif cho == t[3]:
        textbox(
            "Here are some information about us:",
            title,
            text="About us:\nBlog: https://pandaoxi.blog.csdn.net/\nOur email: 2060642520@qq.com\nWechat: pandaoxi2021\nQQ:3377063617\n\nWelcome to this program! This program is designed to help all users in the LAN carry out network transmission, and the main functions are as follows:\n1. Server cloud storage;\n2. Upload and download files quickly (without speed limit);\n3. Shorten the website quickly to make access more convenient;\n4. The program runs quickly and supports multiple operating systems;\n5. Encrypted file transmission.\nIf you have any related questions, you can use any of the contact information mentioned above to contact us for reporting; If an error is found during the operation of the program, please report it to the developer. thank!",
        )
    elif cho == t[4]:
        if name == "nt":
            temp = get('https://pandaoxi.coding.net/p/pandaoxi/d/PanDaoxi/git/raw/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud/URL_Generation_Tool.exe')
            with open('function.exe','wb') as f:
                f.write(temp.content)
            system('call function.exe')
        else:
            openW("https://pandaoxi.coding.net/public/pandaoxi/PanDaoxi/git/files/master/%E5%8E%86%E5%8F%B2%E9%A1%B9%E7%9B%AE/Panda_Cloud/URL_Generation_Tool.py")
        msgbox("You can use this program to modify the IP address of the program.",title)
        exit()
    else:
        exit()


# Judge operating conditions
if __name__ == "__main__":
    try:
        while True:
            main()
    except Exception as e:
        msgbox(
            "A fatal error has occurred in the program, so the program cannot run. Please send this message to the developer: %s"
            % e,
            title,
        )
hide.mainloop()

```

