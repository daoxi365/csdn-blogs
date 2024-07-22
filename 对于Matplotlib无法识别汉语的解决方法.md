上次我们实现用英文制作了天气走势图，但是许多朋友都发现一个问题：它不能识别汉语，如果是汉语的内容，就会发生这样的事情：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201110205611284.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)
上面的文字不会显示，而是小方块。下面我就来告诉大家遇到这种问题时的解决方法：

我们使用`RC设置`（就是 `自定义设置`），插入这两行代码：

```python
# 这是 Windows 版的
plt.rcParams['font.sans-serif'] = 'SimHei' 
plt.rcParams['axes.unicode_minus'] = False

# 这是 Mac 版的
plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False
```
我们再来看完整版：

```python
#导入包和模块
import matplotlib.pyplot as plt
#储存温度和日期
datas = {
         '1' : [22,25,19,18,25,27,20],
         '2' : ['周日','周一','周二','周三','周四','周五','周六']
         }
#绘制出图形，大小是 (15,15)
plt.figure(figsize = (15,15))
#绘制出图形    x轴     y轴
plt.plot(datas['2'],datas['1'])
#设置x和y轴的文字颜色
plt.xticks(size = 10,color = 'red')
plt.yticks(size = 10,color = 'blue')
#设置x轴和y轴的标签
plt.xlabel('日期（天）',size = 12,color = 'black')
plt.ylabel('温度（℃）',size = 12,color = 'black')
#设置标题
plt.title('未来天气温度走势图',size = 20,color = 'black')
#自定义设置
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
#使用风格 bmh
plt.style.use('bmh')
#绘制出统计图
plt.show()
```
效果截图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20201110210247513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70#pic_center)

