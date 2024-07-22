> 有时候我们要是进行登录操作的话，需要使用加密方法，以确保安全。
> 今天我们来说一种加密解密的方法：`base64`，实际上它是一种应用于图片的编码格式。
> 本次我们需要在Windows系统上的Python3。

一如既往，老操作：打开开发工具，新建一个空的Python文档，输入以下代码：

```python
from base64 import b64encode,b64decode

message = '我是潘道熹'
encod = b64encode(message.encode())
decod = b64decode(encod).decode('utf-8')

print('加密后：',encod)
print('解密后：',decod)
```
效果：

```
加密后： b'5oiR5piv5r2Y6YGT54a5'
解密后： 我是潘道熹
```
代码完成了！

