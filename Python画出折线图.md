今天我们来认识一个高级的模块——`Matplotlib`。它可以帮助我们来画出统计图。这是一个第三方模块，所以我们首先需要下载并安装它（`pip3 install matplotlib `）。下载安装完以后，我们打开编辑器，输入以下代码：

```python
#导入包和模块
import matplotlib.pyplot as plt
#储存温度和日期
datas = {
         '1' : [22,25,19,18,25,27,20],
         '2' : ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
         }
#绘制出图形，大小是 (15,15)
plt.figure(figsize = (15,15))
#绘制出图形    x轴     y轴
plt.plot(datas['2'],datas['1'])
#设置x和y轴的文字颜色
plt.xticks(size = 10,color = 'red')
plt.yticks(size = 10,color = 'blue')
#设置x轴和y轴的标签
plt.xlabel('Days',size = 12,color = 'black')
plt.ylabel('Temperature',size = 12,color = 'black')
#设置标题
plt.title('Future Weather Chart Temperature Trend',size = 20,color = 'black')
#使用风格 bmh
plt.style.use('bmh')
#绘制出统计图
plt.show()
```
效果截图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201107103218666.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
如果想要查看所有的风格，使用此代码：

```python
#导入包和模块
import matplotlib.pyplot as plt
#查看所有风格
print(plt.style.available)
```

共有26种，分别是：`['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']`。
