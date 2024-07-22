今天我们来输出1~100之间的一些**数学**信息。

> 本次我们不需要任何第三方库。

**输出1~100所有数字的和**

```python
sumNumber = 0
for i in range(1,101):
	sumNumber += i
print('1~100之间所有数字之和是：',sumNumber)
```
或者使用`sum`计算和方法：

```python
print('1~100之间所有数字之和是：',sum(range(1,101)))
```

**输出1~100之间所有奇数**

```python
numbers = []
for i in range(1,101):
	if (i % 2) == 1:
		numbers.append(i)
print(numbers)
```

**输出1~100之间所有偶数**

```python
numbers = []
for i in range(1,101):
	if (i % 2) == 0:
		numbers.append(i)
print(numbers)
```

**输出1~100之间所有奇数的和**

```python
numberSum = 0
for i in range(1,101):
	if (i % 2) == 1:
		numberSum += i
print(numberSum)
```

**输出1~100之间所有偶数的和**

```python
numberSum = 0
for i in range(1,101):
	if (i % 2) == 0:
		numberSum += i
print(numberSum)
```

**输出1~100之间所有质数**

```python
def prime(maxNumber):
    numbers = []
    min = 2
    while min <= maxNumber:
        is_prime = True
        for i in range(2,min):
            if (min % i) == 0:
                is_prime = False
                break
        if is_prime == True:
            numbers.append(min)
        min += 1
    print('{0} 以下的质数有：'.format(maxNumber))
    print(numbers)
    print()

#调用
prime(100)
```

**输出1~100之间所有质数的和**

```python
# coding : utf-8
def prime(maxNumber):
    numbers = []
    min = 2
    numberSum = 0
    while min <= maxNumber:
        is_prime = True
        for i in range(2,min):
            if (min % i) == 0:
                is_prime = False
                break
        if is_prime == True:
            numbers.append(min)
        min += 1
    for i in numbers:
        numberSum += i
    print('%s以内的质数和是：%s' % (maxNumber,numberSum))
    
prime(100)
```

**输出1~100所有合数**

```python
maxNumber = 100
numbers = []
min = 2
numberSum = 0
for i in range(1,101):
    numbers.append(i)
    
while min <= maxNumber:
    is_prime = True
    for i in range(2,min):
        if (min % i) == 0:
            is_prime = False
            break
    if is_prime == True:
        numbers.remove(min)
    min += 1
print(numbers)
```

**输出1~100所有合数的和**

```python
maxNumber = 100
numbers = []
min = 2
numberSum = 0
for i in range(1,101):
    numbers.append(i)
    
while min <= maxNumber:
    is_prime = True
    for i in range(2,min):
        if (min % i) == 0:
            is_prime = False
            break
    if is_prime == True:
        numbers.remove(min)
    min += 1
for i in numbers:
    numberSum += i
    
print('%s以内的合数和是：%s' % (maxNumber,numberSum))
```

**输出1~100所有数字**

```python
for i in range(1,101):
    print(i,end = ' ')
```

**输出圆周率**

```python
from math import pi
print('圆周率：',pi)
```

**输出自然常量**

```python
from math import e
print('自然常量：',e)
```

