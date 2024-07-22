# `MD5`加密

> MD5的全称是Message-Digest Algorithm 5(信息-摘要算法)，在90年代初由MIT Laboratory for Computer Science和RSA Data Security Inc的Ronald L. Rivest开发出来，经MD2、MD3和MD4发展而来。 
>  —— [360百科](https://baike.so.com/doc/5463650-5701981.html)


```python
from hashlib import md5
message = '这是需要MD5加密的内容'
print('加密结果：',md5(message.encode('utf-8')).hexdigest())
```
我这里解密的结果是`4065bc3afc1b669257075a260b42482b`，可以将代码改为：

```python
from hashlib import md5
message = '这是需要MD5加密的内容'
print('加密结果：',md5(message.encode('utf-8')).hexdigest().upper())
```
这样，结果就是`4065BC3AFC1B669257075A260B42482B`了。
<hr>

# `SHA-1`加密
我们再看代码：

```python
from hashlib import sha1
message = '这是需要SHA-1加密的内容'
print('加密结果：',sha1(message.encode('utf-8')).hexdigest())
```
我获得结果`8f3739d8026ab4d948ac0d4e246c9c132bd32fac`，使用以下代码可以转换为大写，得到结果`8F3739D8026AB4D948AC0D4E246C9C132BD32FAC`：

```python
from hashlib import sha1
message = '这是需要SHA-1加密的内容'
print('加密结果：',sha1(message.encode('utf-8')).hexdigest().upper())
```

