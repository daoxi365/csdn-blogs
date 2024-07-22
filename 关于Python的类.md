很多时候我们需要类。
[大家要是需要看帮助文档，请点击这里。](https://docs.python.org/zh-cn/3.6/tutorial/classes.html)

下面看一个简单的例子：

```python
#注意，创建类的关键字是class
#有个要求，Python类的第一个字母必须大写
class Person(): #创建“人”的类
	def __init__(self,name,age,school,grade,classes,number): #储存属性（可以为空）
		self.name = name  #属性，可以设任意个，任意数据类型
		self.age = age
		self.school = school
		self.grade = grade
		self.classes = classes #避免命名为关键字
		self.number = number
	def output(self):
		print('%s学校%s年级%s班的%s同学，%s岁，学号是%s' % (self.school,self.grade,self.classes,self.name,self.age,self.number)) #输出信息

#对象调用
person = Person('潘道熹',11,'石家庄市长安区行知小学',4,3,'123456789')
person.output()
```
效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20200823110521500.png#pic_center)

