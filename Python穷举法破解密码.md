现在我有一个密码`y`（随机数），
不知道密码是什么，
但已知`100000 ≤ y ≤ 999999`，
使用穷举大法破解密码。

<hr>

首先，我们有一个判断密码是否正确的函数。

```python
y = randint(100000,999999)
def password(n):
    if n == y:
        return '密码正确'
    else:
        return '密码错误'
```
于是，我们可以通过范围内循环来依次尝试破解密码，如果正确即可输出：

```python
for i in range(100000,999999,1):
    x = password(i)
    if x == '密码正确':
        print('密码是%d，成功破解' % i)
        break
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/87129b81598a4e05bc67fe47552a6da9.png)

