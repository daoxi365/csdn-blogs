代码很简单，语法是：

```
以图形显示驱动器或路径的文件夹结构。

TREE [drive:][path] [/F] [/A]

   /F   显示每个文件夹中文件的名称。
   /A   使用 ASCII 字符，而不使用扩展字符。
```
如果想要看`C:\`的目录树，代码就是这样：

```powershell
tree C:\
```
这样你就可以看到效果了，如果想要输出到文本文档，请输入以下代码：

```powershell
cd "%USERPROFILE%\Desktop"
tree C:\ >> Your_Files.txt
```
这样，效果就实现出来了。

