我们今天使用Python发送网络请求到百度人脸识别API接口。

> 我们需要requests模块，它需要安装，代码是
> `pip3 install requests`

**注意：不好意思各位，我的配额没了！如需使用请在`getToken`里边更换为自己的`key`！**
首先我们先来介绍一下API是什么：

> API就是操作系统留给应用程序的一个调用接口，应用程序通过调用操作系统的 API 而使操作系统去执行应用程序的命令。

介绍完了，我们开始写代码：

```python
#导入所需模块
from tkinter import Tk
from tkinter.messagebox import showinfo,showerror
from tkinter.filedialog import askopenfilename
from requests import post,get
from base64 import b64encode

#声明变量
totalList = []

#获取百度人脸识别接口
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
               '&client_id=T1KUrVlob1vUuLpQ0sOYrfoB&client_secret=obx6I60FomQIHqRwlx3mp1GXTGKOkHPu'
    response = get(host)
    content = response.json()
    content = content['access_token']
    return content


#获取人脸识别数据
def getData(img):
    global beauty,path,level
    requestUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    token = getToken()
    params = {'access_token': token}
    f = open(img, 'rb')
    temp = f.read()
    image = b64encode(temp)
    data = {
        'image':image,
        'image_type':'BASE64',
        'face_field':'beauty'
    }
    response = post(requestUrl, params=params, data=data)
    print('响应结果：', response)
    content = response.json()
    print('解析结果：', content)
    #可以将颜值加上20
    beauty = content['result']['face_list'][0]['beauty']
    if beauty <= 50 and beauty > 0:
        level = '一般般吧！'
    elif beauty <= 60:
        level = '有些漂亮了！'
    elif beauty <= 70:
        level = '挺漂亮！'
    elif beauty <= 80:
        level = '好漂亮！'
    elif beauty > 90:
        level = '漂亮的爆表了！'
    tempDict = {'image': img,'beauty':beauty,'level':level}
    path = tempDict['image']
    totalList.append(tempDict)
    
    
#创建页面 
window = Tk()
window.withdraw()
image = askopenfilename(title = '请选择一张图片！',initialdir = 'C:/Windows')
try:
    if not image != 0:
        showerror(title = '错误',message = '请上传一张图片！')
    else:
        getData(img = image)
        showinfo(title = '通知',message = '您的颜值是：{0}。\n颜值等级：{1}\n您上传的图片路径是：{2}。'.format(beauty,level,path))
except FileNotFoundError:
    showerror(title = '错误',message = '请上传一张图片！')
window.mainloop()
```
实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820130329430.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820130405378.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820130511211.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
我上传的是一张钟汉良的照片，如果换个人的话，数值可能就变了，**注意，一定要上传一张清晰的人脸照片，否则会报错。**
![钟汉良](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200820130657725.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)

