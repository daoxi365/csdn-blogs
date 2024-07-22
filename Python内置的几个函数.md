说到字符串（`string`），相信大家都很熟悉了。
它是我们最常用的数据类型之一，括在引号内。
但是Python中的字符串操作，具体应该怎么搞呢？

```python
string1 = 'xxx\\yyy\\zzz' #字符串1，类似于路径
string2 = '123.456.789'   #字符串2，类似于版本
string3 = '|'             #字符串3，将下面的列表内容添加到里面
joinInString3 = ['a','b','c','d','e']   #列表，我们会把它插入到字符串里

#对字符串1的操作
string1 = string1.replace('\\','/') #把'\\'替换成'/'
#对字符串2的操作
string2 = string2.split('.')[0] #以'.'为分隔符，将字符串分割成3部分，取其中的第一份
#对字符串3的操作
string3 = string3.join(joinInString3) #将列表加入

#输出
print('',string1,'\n',string2,'\n',string3)
```
效果，大家自己尝试！
