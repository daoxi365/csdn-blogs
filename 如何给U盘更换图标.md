千篇一律的U盘图标：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a292eaad11fe41bd99f09ac6eb24b388.png)
焕然一新的U盘图标：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/30856b2d9e4b4a569a26af0d1b96f4f8.png)
不只是U盘，磁盘也能行，但是需要重启一下。

<hr>

## 认识`autorun.inf`
相信大家听说过“暴风一号”这个U盘病毒，它利用了`autorun.inf`，当我们打开某个文件夹时，**这个安装信息会自动地打开病毒程序，感染更多文件**。
当然啦，这个时代谁还敢制作传染性病毒呢？这个文件我们只要好好利用，也能干出花样来。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/418446aa8301479aaf59e7f37b2933ac.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/653f3fc70149405193fb715e8b9ac6e4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2796492fa9ed40e886935da7329c4cb9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/38957bb71d0948fab9ab3d3d5a9ff1ce.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

<hr>

## 上手操作！
这里换一个U盘（不管配置）做例子，首先把U盘插进电脑，可见此时的图标尚未变化：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fbd5bc3d14134e9ab9e4681b97ed013f.png)
这时候我们需要准备一个图标文件，可以从网上找，也可以把图片修改成`.ico`格式，从网上找对应的网站，下载下来。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/07b69da463694d2e9e0dabcf65dab325.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4201925fd7304d698ba8491d7debc933.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
把它拷到U盘里，创建一个文本文档，重命名为`autorun.inf`，双击打开编辑。中间杀毒软件可能提醒，点击允许即可。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/da5526280498416197fffa197d555802.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b987b2e06b9b494596bd482143594dcb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_18,color_FFFFFF,t_70,g_se,x_16)
输入以下内容：

```bash
[autorun]
icon=icon.ico,0
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3ed11807b14544fabf1a75158b6ff1ef.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
退出后选择这两个文件，点击属性，选择隐藏。
或使用命令`attrib +s +h icon.ico & atrib +s +h autorun.inf`。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/eb3b2db3f73447f784ccd7cf9b47aef7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
拔掉重插。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/473eb31a90e94f68a9ae4291dcb858e5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
呃………………这画风………………

<hr>

## 想删掉了怎么整
打开命令提示符，输入命令`attrib -s -h *.*`，会显示出来：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/91109b8bffdd430dbd7f55e08c632ec5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
直接删掉即可。
