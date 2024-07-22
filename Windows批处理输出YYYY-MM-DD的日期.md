```bash
@echo off
echo %date:~0,4%-%date:~5,2%-%date:~8,2%
pause
```
不要问我怎么写的，我一个一个试出来的。

我看到网上有人直接用`%date%`的，我试了一下结果是`2022/05/14 周六`，我想把前面的年月日提取出来，就类似于Python的列表切片。

实现的效果就像这样：YYYY-MM-DD
如果要修改连起来的符号，就修改中间的内容。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9a171b05ce6a47e79e040277168611d1.png)

进一步研究，我们可以重新编写程序，给我快速创建一个练习用的文件夹。

```bash
@echo off
set t=%date:~0,4%-%date:~5,2%-%date:~8,2%
md "%t%"
for /l %%i in (1,1,15) do echo // Author:PanDaoxi>>"%t%\%%i.cpp"
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/ff982cd95e713f20c867e75ec43f01ad.gif#pic_center)
总之，还有很多其他的用法，等待着大家去发掘。
