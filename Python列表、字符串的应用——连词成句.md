我现在有一句话：`His lips are soft and his heart is soft.`，你能用程序打乱顺序并完成做题的要求吗？
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/92f917f8c7a7483aa4201db8b52c66f6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
注意`I`要大写，其他的暂不考虑。
我把代码放出来，大家看看：

```python
from random import shuffle
a = input('请输入一个英文句子：').split(' ')
if a[0] != 'I':
    a[0] = a[0].lower()
b = list(a[len(a) - 1])
c = b[len(b) - 1]
d = ''.join(b)
list(b[len(b) - 1]).pop()
b.pop()
b = ''.join(b)
a.pop()
e = []
for i in a:
    e.append(i)
e.append(b)
shuffle(e)
print('连词成句是：',end = ' ')
for i in e:
    print(i,end = ',')
print('(%s)' % c)
```
主要是列表和字符串的知识。
