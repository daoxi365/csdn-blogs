看代码：

```python
from os import environ

for a,b in environ.items():
    print(a,'==>',b)
```
其他信息：

```python
from platform import uname
print(uname())
```

