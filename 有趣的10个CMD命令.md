@[TOC]

# 前言
什么是CMD？它有什么用？？如何使用？？？

> Windows 命令提示符（cmd.exe）是 Windows NT 下的一个用于运行 Windows 控制面板程序或某些 DOS 程序的shell程序；或在 Windows CE 下只用于运行控制面板程序的外壳程序。      ——360百科

网上一打开，都是这种无聊的玩意儿：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/79b05bd41eed43d6b67b60689dd0b77e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
在这些文章中，CMD失去了它本来的意义。

> 今天我来给大家分享10个**有趣的CMD命令**，在关键时刻都有重大的作用。

OK，开始吧。

<hr>

# 正文
首先打开你的CMD：

 1. `Ctrl+Shift+Esc`，呼出任务管理器。
 2. 点击文件，**点击运行新任务**。
 3. 输入`cmd.exe`，以管理员身份运行（可选，本文中不用使用管理员身份了）。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0924918beb404d9e828eb2e2e4bf4ecb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
## 一、测试网络用的`ping`命令

```cpp

用法: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS]
            [-r count] [-s count] [[-j host-list] | [-k host-list]]
            [-w timeout] [-R] [-S srcaddr] [-c compartment] [-p]
            [-4] [-6] target_name

选项:
    -t             Ping 指定的主机，直到停止。
                   若要查看统计信息并继续操作，请键入 Ctrl+Break；
                   若要停止，请键入 Ctrl+C。
    -a             将地址解析为主机名。
    -n count       要发送的回显请求数。
    -l size        发送缓冲区大小。
    -f             在数据包中设置“不分段”标记(仅适用于 IPv4)。
    -i TTL         生存时间。
    -v TOS         服务类型(仅适用于 IPv4。该设置已被弃用，
                   对 IP 标头中的服务类型字段没有任何
                   影响)。
    -r count       记录计数跃点的路由(仅适用于 IPv4)。
    -s count       计数跃点的时间戳(仅适用于 IPv4)。
    -j host-list   与主机列表一起使用的松散源路由(仅适用于 IPv4)。
    -k host-list    与主机列表一起使用的严格源路由(仅适用于 IPv4)。
    -w timeout     等待每次回复的超时时间(毫秒)。
    -R             同样使用路由标头测试反向路由(仅适用于 IPv6)。
                   根据 RFC 5095，已弃用此路由标头。
                   如果使用此标头，某些系统可能丢弃
                   回显请求。
    -S srcaddr     要使用的源地址。
    -c compartment 路由隔离舱标识符。
    -p             Ping Hyper-V 网络虚拟化提供程序地址。
    -4             强制使用 IPv4。
    -6             强制使用 IPv6。
```
我们可以使用它来测试网络是否可用，输入命令`ping 网址`。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d0977c67038d4038a40181f212844d29.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
也可以用于延时，但是不是那么精准。

```cpp
C:\Users\86139>ping baidu.com /n 5

正在 Ping baidu.com [220.181.38.251] 具有 32 字节的数据:
来自 220.181.38.251 的回复: 字节=32 时间=11ms TTL=49
来自 220.181.38.251 的回复: 字节=32 时间=11ms TTL=49
来自 220.181.38.251 的回复: 字节=32 时间=11ms TTL=49
来自 220.181.38.251 的回复: 字节=32 时间=11ms TTL=49
来自 220.181.38.251 的回复: 字节=32 时间=11ms TTL=49

220.181.38.251 的 Ping 统计信息:
    数据包: 已发送 = 5，已接收 = 5，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 11ms，最长 = 11ms，平均 = 11ms

```
## 二、显示或隐藏文件的`attrib`命令
这个东西我们不多说，只说两种用法。
好比我这里有个文件`test.txt`，里面有一些内容。我们如何隐藏它？
![就像这样](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b8d02134149243c6bf42a7ee90030297.gif#pic_center)
其实，我在cmd里面，输入了一行命令：`attrib +s +h /s /d test.txt`。`+s`的意思就是添加系统属性，`+h`添加隐藏属性。

但是这个文件并不是没有了，只需要再输入一行命令：`attrib -s -h /s /d test.txt`即可恢复。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3ab2428703c94c52bfce8dc0790b5c64.png)
## 三、删除文件无影无踪的`del`命令
这个我记得我以前讲过。这里有好多文件：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/bf86330436c84f338deafe4b2332d32a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
如何删除掉里面的exe文件呢？需要使用删除命令`del /q /s /f *.exe`。`*`是通配符，这句命令的意思就是删除所有匹配后缀为`.exe`的文件。同理，当我们想删除所有文件时，即可使用通配符`*.*`。

这个命令是这样使用的。

```cpp
删除一个或多个文件。

DEL [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names
ERASE [/P] [/F] [/S] [/Q] [/A[[:]attributes]] names

  names         指定一个或多个文件或者目录列表。
                通配符可用来删除多个文件。
                如果指定了一个目录，该目录中的所
                有文件都会被删除。

  /P            删除每一个文件之前提示确认。
  /F            强制删除只读文件。
  /S            删除所有子目录中的指定的文件。
  /Q            安静模式。删除全局通配符时，不要求确认
  /A            根据属性选择要删除的文件
  属性          R  只读文件            S  系统文件
                H  隐藏文件            A  准备存档的文件
                I  无内容索引文件      L  重新分析点
                O  脱机文件            -  表示“否”的前缀

如果命令扩展被启用，DEL 和 ERASE 更改如下:

/S 开关的显示句法会颠倒，即只显示已经
删除的文件，而不显示找不到的文件。
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5b1a2e433b484a1d887067a638566c56.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
瞬间，`.exe`的文件都没了。

这个命令不要随便使用，因为它不会把删除的文件放入回收站，而是直接删除。
当你有足够的权限，您甚至可以干掉`%windir%`目录下的文件，但是您的电脑系统就废了。

> 老潘电脑课堂开课啦，随便瞎删电脑里的东西，多半是废了！

另外，这里还有一个奇妙的玩法，那就是`del %0`批处理自删除，效果如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7703f9c17a90466a892fb3709e0fbc3c.gif#pic_center)


## 四、神奇的目录树`tree`命令
这个东西不难，而且很实用，我以前的文章中展现目录树，就用的它。

```cpp
以图形显示驱动器或路径的文件夹结构。

TREE [drive:][path] [/F] [/A]

   /F   显示每个文件夹中文件的名称。
   /A   使用 ASCII 字符，而不使用扩展字符。

```
我展开一个我的文件夹，各位请上演！

```cpp
D:\编程代码\共享文件夹>tree /f
卷 Data 的文件夹 PATH 列表
卷序列号为 90AF-CB35
D:.
│  a8ab838aade1be7763e20d8a6e4cc85e9bda8b5ef2e29d4f9f2be38fefb37065.zip
│  lframeCNDocs.zip
│  NSudo_9.0_Preview1_9.0.2676.0.zip
│
├─battoexe
│      Bat_To_Exe_Converter.exe
│      settings
│
└─System Volume Information
```
嗯，这样展示很清楚的。

## 五、说没就没的命令`taskkill`
我没说清，这个命令是让进程说没就没。

```cpp

TASKKILL [/S system [/U username [/P [password]]]]
         { [/FI filter] [/PID processid | /IM imagename] } [/T] [/F]

描述:
    使用该工具按照进程 ID (PID) 或映像名称终止任务。

参数列表:
    /S    system           指定要连接的远程系统。

    /U    [domain\]user    指定应该在哪个用户上下文执行这个命令。

    /P    [password]       为提供的用户上下文指定密码。如果忽略，提示
                           输入。

    /FI   filter           应用筛选器以选择一组任务。
                           允许使用 "*"。例如，映像名称 eq acme*

    /PID  processid        指定要终止的进程的 PID。
                           使用 TaskList 取得 PID。

    /IM   imagename        指定要终止的进程的映像名称。通配符 '*'可用来
                           指定所有任务或映像名称。

    /T                     终止指定的进程和由它启用的子进程。

    /F                     指定强制终止进程。

    /?                     显示帮助消息。

筛选器:
    筛选器名      有效运算符                有效值
    -----------   ---------------           -------------------------
    STATUS        eq, ne                    RUNNING |
                                            NOT RESPONDING | UNKNOWN
    IMAGENAME     eq, ne                    映像名称
    PID           eq, ne, gt, lt, ge, le    PID 值
    SESSION       eq, ne, gt, lt, ge, le    会话编号。
    CPUTIME       eq, ne, gt, lt, ge, le    CPU 时间，格式为
                                            hh:mm:ss。
                                            hh - 时，
                                            mm - 分，ss - 秒
    MEMUSAGE      eq, ne, gt, lt, ge, le    内存使用量，单位为 KB
    USERNAME      eq, ne                    用户名，格式为 [domain\]user
    MODULES       eq, ne                    DLL 名称
    SERVICES      eq, ne                    服务名称
    WINDOWTITLE   eq, ne                    窗口标题

    说明
    ----
    1) 只有在应用筛选器的情况下，/IM 切换才能使用通配符 '*'。
    2) 远程进程总是要强行 (/F) 终止。
    3) 当指定远程机器时，不支持 "WINDOWTITLE" 和 "STATUS" 筛选器。

例如:
    TASKKILL /IM notepad.exe
    TASKKILL /PID 1230 /PID 1241 /PID 1253 /T
    TASKKILL /F /IM cmd.exe /T
    TASKKILL /F /FI "PID ge 1000" /FI "WINDOWTITLE ne untitle*"
    TASKKILL /F /FI "USERNAME eq NT AUTHORITY\SYSTEM" /IM notepad.exe
    TASKKILL /S system /U 域\用户名 /FI "用户名 ne NT*" /IM *
    TASKKILL /S system /U username /P password /FI "IMAGENAME eq note*"
```
我们来试试。我现在写了一个弹窗。如何关闭？直接点叉就行。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5153896bb0414986be371fb47d83cc94.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
当我们加了个死循环，效果就变了。点叉，关不完的。
这时候，我们可以使用命令`taskkill /im python.exe /f`，就关掉了。

```cpp
成功: 已终止进程 "python.exe"，其 PID 为 3440。
```
## 六、可爱的循环`for`命令
这个大家都熟，谁都知道。

```cpp
对一组文件中的每一个文件执行某个特定命令。

FOR %variable IN (set) DO command [command-parameters]

  %variable  指定一个单一字母可替换的参数。
  (set)      指定一个或一组文件。可以使用通配符。
  command    指定对每个文件执行的命令。
  command-parameters
             为特定命令指定参数或命令行开关。

在批处理程序中使用 FOR 命令时，指定变量请使用 %%variable
而不要用 %variable。变量名称是区分大小写的，所以 %i 不同于 %I.

如果启用命令扩展，则会支持下列 FOR 命令的其他格式:

FOR /D %variable IN (set) DO command [command-parameters]

    如果集中包含通配符，则指定与目录名匹配，而不与文件名匹配。

FOR /R [[drive:]path] %variable IN (set) DO command [command-parameters]

    检查以 [drive:]path 为根的目录树，指向每个目录中的 FOR 语句。
    如果在 /R 后没有指定目录规范，则使用当前目录。如果集仅为一个单点(.)字符，
    则枚举该目录树。

FOR /L %variable IN (start,step,end) DO command [command-parameters]

    该集表示以增量形式从开始到结束的一个数字序列。因此，(1,1,5)将产生序列
    1 2 3 4 5，(5,-1,1)将产生序列(5 4 3 2 1)

FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
FOR /F ["options"] %variable IN ('command') DO command [command-parameters]

    或者，如果有 usebackq 选项:

FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
FOR /F ["options"] %variable IN ('command') DO command [command-parameters]

    fileset 为一个或多个文件名。继续到 fileset 中的下一个文件之前，
    每份文件都被打开、读取并经过处理。处理包括读取文件，将其分成一行行的文字，
    然后将每行解析成零或更多的符号。然后用已找到的符号字符串变量值调用 For 循环。
    以默认方式，/F 通过每个文件的每一行中分开的第一个空白符号。跳过空白行。
    你可通过指定可选 "options" 参数替代默认解析操作。这个带引号的字符串包括一个
    或多个指定不同解析选项的关键字。这些关键字为:

        eol=c           - 指一个行注释字符的结尾(就一个)
        skip=n          - 指在文件开始时忽略的行数。
        delims=xxx      - 指分隔符集。这个替换了空格和制表符的
                          默认分隔符集。
        tokens=x,y,m-n  - 指每行的哪一个符号被传递到每个迭代
                          的 for 本身。这会导致额外变量名称的分配。m-n
                          格式为一个范围。通过 nth 符号指定 mth。如果
                          符号字符串中的最后一个字符星号，
                          那么额外的变量将在最后一个符号解析之后
                          分配并接受行的保留文本。
        usebackq        - 指定新语法已在下类情况中使用:
                          在作为命令执行一个后引号的字符串并且一个单
                          引号字符为文字字符串命令并允许在 file-set
                          中使用双引号扩起文件名称。

    某些范例可能有助:

FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt) do @echo %i %j %k

    会分析 myfile.txt 中的每一行，忽略以分号打头的那些行，将
    每行中的第二个和第三个符号传递给 for 函数体，用逗号和/或
    空格分隔符号。请注意，此 for 函数体的语句引用 %i 来
    获得第二个符号，引用 %j 来获得第三个符号，引用 %k
    来获得第三个符号后的所有剩余符号。对于带有空格的文件
    名，你需要用双引号将文件名括起来。为了用这种方式来使
    用双引号，还需要使用 usebackq 选项，否则，双引号会
    被理解成是用作定义某个要分析的字符串的。

    %i 在 for 语句中显式声明，%j 和 %k 是通过
    tokens= 选项隐式声明的。可以通过 tokens= 一行
    指定最多 26 个符号，只要不试图声明一个高于字母 "z" 或
    "Z" 的变量。请记住，FOR 变量是单一字母、分大小写和全局的变量；
    而且，不能同时使用超过 52 个。

    还可以在相邻字符串上使用 FOR /F 分析逻辑，方法是，
    用单引号将括号之间的 file-set 括起来。这样，该字符
    串会被当作一个文件中的一个单一输入行进行解析。

    最后，可以用 FOR /F 命令来分析命令的输出。方法是，将
    括号之间的 file-set 变成一个反括字符串。该字符串会
    被当作命令行，传递到一个子 CMD.EXE，其输出会被捕获到
    内存中，并被当作文件分析。如以下例子所示:

      FOR /F "usebackq delims==" %i IN (`set`) DO @echo %i

    会枚举当前环境中的环境变量名称。

另外，FOR 变量参照的替换已被增强。你现在可以使用下列
选项语法:

     %~I          - 删除任何引号(")，扩展 %I
     %~fI        - 将 %I 扩展到一个完全合格的路径名
     %~dI        - 仅将 %I 扩展到一个驱动器号
     %~pI        - 仅将 %I 扩展到一个路径
     %~nI        - 仅将 %I 扩展到一个文件名
     %~xI        - 仅将 %I 扩展到一个文件扩展名
     %~sI        - 扩展的路径只含有短名
     %~aI        - 将 %I 扩展到文件的文件属性
     %~tI        - 将 %I 扩展到文件的日期/时间
     %~zI        - 将 %I 扩展到文件的大小
     %~$PATH:I   - 查找列在路径环境变量的目录，并将 %I 扩展
                   到找到的第一个完全合格的名称。如果环境变量名
                   未被定义，或者没有找到文件，此组合键会扩展到
                   空字符串

可以组合修饰符来得到多重结果:

     %~dpI       - 仅将 %I 扩展到一个驱动器号和路径
     %~nxI       - 仅将 %I 扩展到一个文件名和扩展名
     %~fsI       - 仅将 %I 扩展到一个带有短名的完整路径名
     %~dp$PATH:I - 搜索列在路径环境变量的目录，并将 %I 扩展
                   到找到的第一个驱动器号和路径。
     %~ftzaI     - 将 %I 扩展到类似输出线路的 DIR

在以上例子中，%I 和 PATH 可用其他有效数值代替。%~ 语法
用一个有效的 FOR 变量名终止。选取类似 %I 的大写变量名
比较易读，而且避免与不分大小写的组合键混淆。
```
好长！我们只说类似于`range()`的循环。
格式（管理员模式下，请将`%i`替换为`%%i`）`for /l %i in (开始的地方,步长step,结束的地方) do 命令`，结束的时候会停止到前一项，如`(1,1,10)`的循环为1~9。
现在我们来创建一批C++文件，10个。

```cpp
for /l %i in (1,1,10) do echo // Author:PanDaoxi>>%i.cpp
```

## 七、打开程序的`start`命令
打开程序的操作想必大家都很明白咯。

```cpp
启动一个单独的窗口以运行指定的程序或命令。

START ["title"] [/D path] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
      [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
      [/NODE <NUMA node>] [/AFFINITY <hex affinity mask>] [/WAIT] [/B]
      [command/program] [parameters]

    "title"     在窗口标题栏中显示的标题。
    path        启动目录。
    B           启动应用程序，但不创建新窗口。
                应用程序已忽略 ^C 处理。除非应用程序
                启用 ^C 处理，否则 ^Break 是唯一可以中断
                该应用程序的方式。
    I           新的环境将是传递
                给 cmd.exe 的原始环境，而不是当前环境。
    MIN         以最小化方式启动窗口。
    MAX         以最大化方式启动窗口。
    SEPARATE    在单独的内存空间中启动 16 位 Windows 程序。
    SHARED      在共享内存空间中启动 16 位 Windows 程序。
    LOW         在 IDLE 优先级类中启动应用程序。
    NORMAL      在 NORMAL 优先级类中启动应用程序。
    HIGH        在 HIGH 优先级类中启动应用程序。
    REALTIME    在 REALTIME 优先级类中启动应用程序。
    ABOVENORMAL 在 ABOVENORMAL 优先级类中启动应用程序。
    BELOWNORMAL 在 BELOWNORMAL 优先级类中启动应用程序。
    NODE        将首选非一致性内存结构(NUMA)节点指定为
                十进制整数。
    AFFINITY    将处理器关联掩码指定为十六进制数字。
                进程被限制在这些处理器上运行。

                将 /AFFINITY 和 /NODE 结合使用时，会对关联掩码
                进行不同的解释。指定关联掩码，以便将零位作为起始位置(就如将 NUMA
                节点的处理器掩码向右移位一样)。
                进程被限制在指定关联掩码和 NUMA 节点之间的
                那些通用处理器上运行。
                如果没有通用处理器，则进程被限制在
                指定的 NUMA 节点上运行。
    WAIT        启动应用程序并等待它终止。
    command/program
                如果它是内部 cmd 命令或批文件，则
                该命令处理器是使用 cmd.exe 的 /K 开关运行的。
                这表示运行该命令之后，该窗口
                将仍然存在。

                如果它不是内部 cmd 命令或批文件，则
                它就是一个程序，并将作为一个窗口化应用程序或
                控制台应用程序运行。

    parameters  这些是传递给 command/program 的参数。

注意: 在 64 位平台上不支持 SEPARATE 和 SHARED 选项。

通过指定 /NODE，可按照利用 NUMA 系统中的内存区域的方式
创建进程。例如，可以创建两个完全
通过共享内存互相通信的进程以共享相同的首选 NUMA 节点，
从而最大限度地减少内存延迟。只要有可能，
它们就会分配来自相同 NUMA 节点的
内存，并且会在指定节点之外的处理器上自由运行。

    start /NODE 1 application1.exe
    start /NODE 1 application2.exe

这两个进程可被进一步限制在相同 NUMA 节点内的指定处理器
上运行。在以下示例中，application1 在
节点的两个低位处理器上运行，而 application2
在该节点的其后两个处理器上运行。该示例假定指定节点至少具有四个逻辑处理器。请注意，节点号可更改为该计算机的任何有效节点号，
而无需更改关联掩码。

    start /NODE 1 /AFFINITY 0x3 application1.exe
    启动 /NODE 1 /AFFINITY 0xc application2.exe

如果命令扩展被启用，通过命令行或 START 命令的外部命令
调用会如下改变:

将文件名作为命令键入，非可执行文件可以通过文件关联调用。
    (例如，WORD.DOC 会调用跟 .DOC 文件扩展名关联的应用程序)。
    关于如何从命令脚本内部创建这些关联，请参阅 ASSOC 和
     FTYPE 命令。

执行的应用程序是 32 位 GUI 应用程序时，CMD.EXE 不等应用
    程序终止就返回命令提示符。如果在命令脚本内执行，该新行为
    则不会发生。

如果执行的命令行的第一个符号是不带扩展名或路径修饰符的
    字符串 "CMD"，"CMD" 会被 COMSPEC 变量的数值所替换。这
    防止从当前目录提取 CMD.EXE。

如果执行的命令行的第一个符号没有扩展名，CMD.EXE 会使用
    PATHEXT 环境变量的数值来决定要以什么顺序寻找哪些扩展
    名。PATHEXT 变量的默认值是:

        .COM;.EXE;.BAT;.CMD

    请注意，该语法跟 PATH 变量的一样，分号隔开不同的元素。

查找可执行文件时，如果没有相配的扩展名，看一看该名称是否
与目录名相配。如果确实如此，START 会在那个路径上调用
Explorer。如果从命令行执行，则等同于对那个路径作 CD /D。
```
这个东西我们只介绍`/min`和`/max`。我们如何最小化打开程序？`start /min cmd.exe & exit`运行这行命令后，当前cmd会消失，然后在任务栏中最小化弹出一个新的cmd。
当我们最大化创建一个cmd进程，命令应该这么写：`start /max cmd.exe`。

## 八、CMD下切换目录`cd`命令

```cpp
显示当前目录名或改变当前目录。

CHDIR [/D] [drive:][path]
CHDIR [..]
CD [/D] [drive:][path]
CD [..]

  ..   指定要改成父目录。

键入 CD drive: 显示指定驱动器中的当前目录。
不带参数只键入 CD，则显示当前驱动器和目录。

使用 /D 开关，除了改变驱动器的当前目录之外，
还可改变当前驱动器。

如果命令扩展被启用，CHDIR 会如下改变:

当前的目录字符串会被转换成使用磁盘名上的大小写。所以，
如果磁盘上的大小写如此，CD C:\TEMP 会将当前目录设为
C:\Temp。

CHDIR 命令不把空格当作分隔符，因此有可能将目录名改为一个
带有空格但不带有引号的子目录名。例如:

     cd \winnt\profiles\username\programs\start menu

与下列相同:

     cd "\winnt\profiles\username\programs\start menu"

在扩展停用的情况下，你必须键入以上命令。
```
我这里有个文件夹`tools`，如何切换？`cd 相对路径或绝对路径`即可。`cd tools`即可进入该文件夹。

## 九、创建文件夹的命令`md`
emm，不要想歪了。

```cpp
创建目录。

MKDIR [drive:]path
MD [drive:]path

如果命令扩展被启用，MKDIR 会如下改变:

如果需要，MKDIR 会在路径中创建中级目录。例如: 假设 \a 不
存在，那么:

    mkdir \a\b\c\d

与:

    mkdir \a
    chdir \a
    mkdir b
    chdir b
    mkdir c
    chdir c
    mkdir d

相同。如果扩展被停用，则需要键入 mkdir \a\b\c\d。
```
如何套娃？我们来套一个吧。

> 文件夹套娃：创建文件夹，并进入文件夹，创建文件夹，并进入文件夹……如此循环。

我们来创建深度100的套娃文件夹：`for /l %i in (1,1,100) do (md 第%i层&cd 第%i层)`。![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b6ba9a7aa36e45b8a4319b95de76ed0e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
如何进入呢？大家自行思考一下。

```cpp
for /l %i in (1,1,100) do cd 第%i层
```
## 十、操作注册表`reg`命令
不要随便使用。只介绍这两个：

```cpp
reg add
reg delete
```

```cpp

REG ADD KeyName [/v ValueName | /ve] [/t Type] [/s Separator] [/d Data] [/f]
        [/reg:32 | /reg:64]

  KeyName  [\\Machine\]FullKey
           Machine  远程机器名 - 忽略默认到当前机器。远程机器上
                    只有 HKLM 和 HKU 可用。
           FullKey  ROOTKEY\SubKey
           ROOTKEY  [ HKLM | HKCU | HKCR | HKU | HKCC ]
           SubKey   所选 ROOTKEY 下注册表项的完整名称。

  /v       所选项之下要添加的值名称。

  /ve      为注册表项添加空白值名称(默认)。

  /t       RegKey 数据类型
           [ REG_SZ    | REG_MULTI_SZ | REG_EXPAND_SZ |
             REG_DWORD | REG_QWORD    | REG_BINARY    | REG_NONE ]
           如果忽略，则采用 REG_SZ。

  /s       指定一个在 REG_MULTI_SZ 数据字符串中用作分隔符的字符
           如果忽略，则将 "\0" 用作分隔符。

  /d       要分配给添加的注册表 ValueName 的数据。

  /f       不用提示就强行覆盖现有注册表项。

 /reg:32  指定应该使用 32 位注册表视图访问的注册表项。

 /reg:64  指定应该使用 64 位注册表视图访问的注册表项。

例如:

  REG ADD \\ABC\HKLM\Software\MyCo
    添加远程机器 ABC 上的一个注册表项 HKLM\Software\MyCo

  REG ADD HKLM\Software\MyCo /v Data /t REG_BINARY /d fe340ead
    添加一个值(名称: Data，类型: REG_BINARY，数据: fe340ead)

  REG ADD HKLM\Software\MyCo /v MRU /t REG_MULTI_SZ /d fax\0mail
    添加一个值(名称: MRU，类型: REG_MULTI_SZ，数据: fax\0mail\0\0)

  REG ADD HKLM\Software\MyCo /v Path /t REG_EXPAND_SZ /d ^%systemroot^%
    添加一个值(名称: Path，类型: REG_EXPAND_SZ，数据: %systemroot%)
    注意: 在扩充字符串中使用插入符号 ( ^ )
```

```cpp
REG DELETE KeyName [/v ValueName | /ve | /va] [/f] [/reg:32 | /reg:64]

  KeyName    [\\Machine\]FullKey
    远程机器名 - 如果省略，默认情况下将使用当前机器。
             远程机器上只有 HKLM 和 HKU 可用。
    FullKey  ROOTKEY\SubKey
    ROOTKEY  [ HKLM | HKCU | HKCR | HKU | HKCC ]
    SubKey   所选 ROOTKEY 下面的注册表项的全名。

  ValueName  所选项下面的要删除的值名称。
             如果省略，则删除该项下面的所有子项和值。

  /ve        删除空值名称的值(默认)。

  /va        删除该项下面的所有值。

  /f         不用提示，强制删除。

  /reg:32    指定应使用 32 位注册表视图访问
             注册表项。

  /reg:64    指定应使用 64 位注册表视图访问
             注册表项。

示例:

  REG DELETE HKLM\Software\MyCo\MyApp\Timeout
    删除注册表项 Timeout 及其所有子项和值

  REG DELETE \\ZODIAC\HKLM\Software\MyCo /v MTU
    删除 ZODIAC 上的 MyCo 下面的注册表值 MTU
```
**注册表不能随便修改，可能会导致系统不稳定**。这里面有很多系统的设置，定期做备份，有些病毒通过修改注册表来禁用系统功能。我们来试一下用命令禁用任务管理器。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ea9ac802c3544f2b95fa9021abacab78.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
名称：`DisableTaskmgr`
类型：`REG_DWORD`

禁用：
```cpp
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /d 1 /t REG_DWORD /f 
```
恢复：

```cpp
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr"
```
手头没有虚拟机，就不演示了。运行后电脑的任务管理器将提示“**任务管理器已被管理员禁用。**”

更新：
现在有了虚拟机，我们来测试一下上面的程序：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b3e130e062dd47458ba7f5f67b715d96.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9fda715a2a5e4606b5273425390c8ecd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

