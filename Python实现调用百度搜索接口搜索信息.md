> 今天我们来写一个简单的搜索程序，需要os模块
> 必须使用Windows系统

步骤：
1.获取百度搜索接口：`http://www.baidu.com/s?wd=`（360接口是`https://www.so.com/s?ie=utf-8&src=hao_360so_b_cube&shb=1&hsid=ab61903f5523b973&q=`），比如在wd后面加一个“Python”，那么就会在浏览器里使用百度（360）搜索“Python”的结果。
2.打开开发工具，新建一个Python文档。
3.输入代码如下：

```python
from os import system
search = input('请输入您要搜索的内容（输入end退出）：')
interface = 'http://www.baidu.com/s?wd='

while search != 'end':
    system('start iexplore "{0}"'.format(interface + search))
    search = input('请输入您要搜索的内容（输入end退出）：')
else:
    print('已经退出程序！')
    exit()
```
代码完成了！
