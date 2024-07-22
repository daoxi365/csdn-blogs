```python
请使用if-elif-else判断用户输入的年龄，如果年龄≥18，输出“成年人”；如果年龄≥45，输出“中年人”；如果年龄≥60且年龄≤100，那么输出“老年人”，不考虑其他情况。
```

```python
age = int(input('请输入您的年龄：'))
if age >= 18:
	print('成年人')
elif age >= 45:
	print('中年人')
elif age >= 60 and age <= 100:
	print('老年人')
else:
	pass
```

<hr>
注：下次我们要学习一个很神奇的东西！请留出足够的内存！
