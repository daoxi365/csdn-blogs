做这件事，理论上要实现三个功能：
①下载图片
②播放图片
③更新图片
这个恐怕以我的水平不能在一个程序里面实现，需要一些人工操作。

@[toc]

# 第一步：下载图片
这个要靠python啦，我又找了个可用的API。

```python
# Author:PanDaoxi 
from os import remove,walk,mkdir
from os.path import exists,join
from random import randint
from requests import get

url = 'https://api.ixiaowai.cn/gqapi/gqapi.php'
path = 'D:/每日壁纸/' # 保存路径
imgs = 15           # 15张图片
try:
    if not exists(path):
        mkdir(path)
        print('CRE OKK')
    else:
        dl = []
        for root,dirs,files in walk(path,topdown=False):
            for name in files:
                dl.append(join(root, name))
            for name in dirs:
                dl.append(join(root, name))
        print('DEL OKK')
except Exception as e:
    print('DEL ERR',e)

try:
    print('DOW ING')
    for i in range(0,imgs):
        res = get(url)
        with open(path + str(randint(100000,999999)) + '.jpg','wb') as f:
            f.write(res.content)
    print('DOW OKK')
    for i in range(0,len(dl)):
        remove(dl[i])
except Exception as e:
    print('DOW ERR',e)
```
默认保存到`D:/每日壁纸`这个文件夹中，可以修改`path`的保存地址，每次运行先判断如果有这个文件夹那么就记录下里面的东西，然后下载图片，最后删除旧的内容。

如果有需要更多壁纸，可以修改`imgs`变量。默认为15。
注意：做接下来的步骤前，请先运行一遍程序；
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c44e7e1188614fcfbd51567e000ec489.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

# 第二步：设置自启动
这个么，每日新鲜壁纸，放到电脑打开的时候，就运行一次，得到15张新的壁纸。
我觉得最简单快捷的办法就是把它放到自启动目录里面，为了这个程序似乎没必要去弄注册表。

> 使用快捷键<kbd>win+r</kbd>打开运行，输入<kbd>shell:startup</kbd>。
> 进入了一个文件夹，这就是快速自启动目录（也可以使用路径`%APPDATA%\Microsoft\Windows\Start
> Menu\Programs\Startup`进入），放在这里面的东西开机时都会自动运行。

准备好刚才写好的python文件的路径。
在文件夹里创建一个文件，命名为`随便想一个名字.bat`，右键编辑，输入命令：

```python
@echo off
start /min python "路径"  
```
最小化打开程序。

# 第三步：设置幻灯片壁纸
以Windows10为例，<kbd>Win+i</kbd>打开设置，个性化。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8ca68104667049a1b3f81d036628044b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
在这里，选择“幻灯片放映”；
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/631e9d72b6aa4533be4c96283185171f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

浏览，选择`D:\每日图片`；
图片切换频率设置为1分钟。

# 注意事项
**注意：个别图片可能发生错误，您可以忽略它。因为系统不会播放它。这个错误是新浪图片的bug。**
