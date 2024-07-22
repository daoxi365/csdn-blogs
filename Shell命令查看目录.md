这个代码常常被人用来耍帅，把背景颜色调一下，然后跑目录，让别人羡慕得不行，可是也不过如此。今天我就来告诉大家怎样跑目录。

打开`C:\Windows\System32\cmd.exe`，首先把背景颜色改变以下：

```powershell
color 0a
```
然后输入以下代码：

```powershell
dir /s C:\
```
这样就完了。要是想输出到文本文档，请输入以下代码：

```powershell
cd "%USERPROFILE%\Desktop"
dir /s C:\ >> Your_Files.txt
```
这样，你就会在桌面上看到一个名为`Your_Files.txt`的文件（此方法仅限于桌面名称没修改过的，比如把桌面上的文件同步，那就不一样了，路径就是`%USERPROFILE%\OneDrive\Desktop`）！
