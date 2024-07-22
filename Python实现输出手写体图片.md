话说我在研究`pywhatkit`时搞了一下源程序，发现了这个：

```python
data = requests.get(
    f"https://pywhatkit.herokuapp.com/handwriting?text={string}&rgb={rgb[0]},{rgb[1]},{rgb[2]}"
)
```
然后，我掏出了`apifox`，一试：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/07c0d3b592414b47a3b5a5dd2489b6c4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
ohhhhhhhhhhh ！
来，说说我发现的东西！

<hr>

这是一个GET请求的API接口`https://pywhatkit.herokuapp.com/handwriting`，两个参数，分别是`text`（文字）和`rgb`（颜色）。
我找了一段简短的英文小故事来测试。接口无法处理中文。

> A child was careless ramie stabbed, he rushed home and told his mother: I only lightly Pengyi what, it was my painful thorns.Mom said: Because of this, it will thorn you. if the next time you met Ramie, to a courageous and seize it, it will be in your hands become soft as silk, you will no longer be stabbed.It is said that many people are serving hard against soft.
> ![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5ba64b2063c740b89d8fa088789fe2e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

我把它写成一个程序，一起来看：

```python
from requests import get
t = input('Enter some English >>> ')
if len(t) > 1035:
    print('The content you entered is too long.')
    input()
    exit()

color = (30,30,150)
params = {
          'text':t,
          'color':'%d,%d,%d' % (color[0],color[1],color[2])
          }
try:
    res = get('https://pywhatkit.herokuapp.com/handwriting',params=params)
    with open('text.png','wb') as f:
        f.write(res.content)
    
    print('\nSuccessful production.')
    input()
except Exception as e:
    print('Error :',e)
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/012dbf6ed9da4b45b8bbdae7b9c2c391.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1b1ab42eafad45419d643a3e908fe17a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

