（此程序需要`easygui`模块，请使用`pip install easygui`）
已知天气网站获取天气接口为`
'http://wthrcdn.etouch.cn/weather_mini?city=' + 城市名`，你知道代码咋写吗？

```python
#导入包
from requests import get
from easygui import enterbox,msgbox

#获取今天天气的函数
def getToday(cityName):
    #定义全局变量
    global weatherDict,city,temperature,sick,types
    #要访问的网络URL
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    #获取响应并解析
    response = get(url)
    weatherDict = response.json()
    #获取城市名
    city = weatherDict['data']['city']
    #将天气信息赋值给变量
    temperature = weatherDict['data']['wendu'] + '℃ '
    sick = weatherDict['data']['ganmao']
    types = weatherDict['data']['forecast'][0]['type']

#调用函数，输出天气信息
search = enterbox('请输入中国城市：','天气助手')
getToday(search)
#判断城市名是否存在
if weatherDict['desc'] == 'OK':
	#输出天气信息
    msgbox(city + '的天气情况如下：' + '\n温度： ' + temperature + '\n温馨提示： ' + sick + '\n天气： ' + types,'天气助手')
else:
	#反馈
    msgbox('您输入的城市名称不存在！','天气助手')
```
实现效果：

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/202011071559322.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2020110715594823.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)

