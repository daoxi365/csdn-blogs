祝大家新年快乐，虎年大吉，诸事顺利！

```python
from pywebio.input import *
from pywebio.output import put_text
from os import system,remove
try:
    code = textarea('Code Edit Online', code={'mode': "python",'theme': 'darcula'}, value='# input your code here\n')
    with open('temp.py','w',encoding = 'utf-8') as f:
        f.write(code)
    system('python temp.py')
    put_text('成功运行程序')
except Exception as e:
    put_text('运行：错误 at %s' % e)
```
主要使用了`pywebio`程序，实现了Python的简陋在线编辑器。
相对C++编辑器就比较复杂，需要调用`g++.exe`，可能在您的电脑上，就不见得能用了，需要把Dev-C++安装到我这个位置，程序才可以运行，您可以修改程序。

```python
from pywebio.input import *
from pywebio.output import put_text
from sys import path
from os import system,remove
try:
    system('chcp 65001 >nul')
    code = textarea('Code Edit Online ( C++ )', code={'mode': "python",'theme': 'darcula',}, value='// input your code here.\n')
    with open('temp.cpp','w',encoding='utf-8') as f:
        f.write(code)
    put_text('成功运行程序')
    system(r'D:\Dev-C++\Dev-cpp\MinGW64\bin\g++.exe "%s\temp.cpp" -o "%s\temp.exe" && call "%s\temp.exe" && pause' % (path[0],path[0],path[0]))
    remove('temp.cpp')
    remove('temp.exe')
except Exception as e:
    put_text('运行：错误 at %s' % e)
```

运行时会报一个错，不用管它，跟咱们的程序无关。如果不是这个错，那就是您的程序有BUG。
```python
ERROR:tornado.application:Exception in callback functools.partial(<bound method IOLoop._discard_future_result of <tornado.platform.asyncio.AsyncIOMainLoop object at 0x0000025DC4382AC8>>, <Task finished coro=<start_server_in_current_thread_session.<locals>.wait_to_stop_loop() done, defined at D:\python\lib\site-packages\pywebio\platform\tornado.py:420> exception=AttributeError("module 'asyncio' has no attribute 'all_tasks'",)>)
Traceback (most recent call last):
  File "D:\python\lib\site-packages\tornado\ioloop.py", line 741, in _run_callback
    ret = callback()
  File "D:\python\lib\site-packages\tornado\ioloop.py", line 765, in _discard_future_result
    future.result()
  File "D:\python\lib\site-packages\pywebio\platform\tornado.py", line 440, in wait_to_stop_loop
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task() and not t.done()]
AttributeError: module 'asyncio' has no attribute 'all_tasks'
```

<hr>

测试程序，直接运行第一个，输入一段Python代码：

```python
maxNumber = 100
numbers = []
min = 2
numberSum = 0
for i in range(1,101):
    numbers.append(i)
    
while min <= maxNumber:
    is_prime = True
    for i in range(2,min):
        if (min % i) == 0:
            is_prime = False
            break
    if is_prime == True:
        numbers.remove(min)
    min += 1
print(numbers)

```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/845bdd05b64e44568e4a5e49d884a48b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

点击蓝色按钮，观察控制台：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e12f85ad237f440784f9748c5bd41e16.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/53351400161a422aba439435a2b2e70d.png)
成功。


<hr>

再测C++，测试代码如下（C++：画桃心）：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	for(double y=1.5;y>-1.5;y-=0.1){
		for(double x=-1.5;x<1.5;x+=0.05){
			double a=x*x+y*y-1;
			char b=(a*a*a-x*x*y*y*y<=0.0?'*':' ');
			cout<<b;
		}
		cout<<endl;
	}
	
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1607ebf3f8b84591a914c0838f9fabef.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
输入测试程序并提交，观察控制台：

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ae5b790b4a5249899a1aedfb40b0242d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/69e3656822194dde99da16ee3ef94cc4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
控制台上多了个大桃心，成功运行。
