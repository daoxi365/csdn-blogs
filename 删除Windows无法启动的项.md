以前电脑出现问题，使用的是云骑士修复，安装在了本地磁盘，然后不用了，看着不舒服，就想给他删了。可是按照网上的方法（即通过系统实用程序`msconfig`删除多余的启动项），我删除了其中一个，但是`YunQishi Support`这个项无法删除，也无法打开，缺失引导，每次开机都需要选择系统。我很苦恼，在今天看到了`bcdedit`命令，于是记录了这次的修复过程。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/caa27b3edd9349f78442f450abdd3f0b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（启动时遇到的问题）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a9584e07fed74fe6b0b9d7c104d3d4d0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（网上的方法没有成功）
打开管理员模式的命令提示符，输入`bcdedit`，找到出现问题的一项
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a542c1dcba8e43da83d198497cfe3d27.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f7cf67b0553d4e82a5453b04246175a5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
复制这一项，输入命令`bcdedit /delete 复制的东西`（每台电脑都不一样，注意不要瞎删别的东西），一般就可以修复了。如果还不行的话，找一个PE，修复一下引导即可修复。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/74e60443a6c646a4b4962a48ab5e11ff.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（删除完成后的显示）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e2c36fba8e1447ca8d2ca8461880817b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（正确的内容）

如果实在不行，就把启动管理器的等待时间设为0，也可以解决，效果就是启动管理器一闪而过。
