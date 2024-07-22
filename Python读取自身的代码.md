今天（刚才）写程序时突然想到是不是可以读取当前文件自己的代码，然后再写到一个新文件里面，然后我就愣住了，这能行吗？？
我一番尝试**还真行**，成功了，代码就如下。

```python
with open(__file__,"r",encoding="utf-8") as r:
	with open("copy.py","r",encoding="utf-8") as w: 
		w.write(r.read())
```

上面的`__file__`就是当前文件的绝对路径。

