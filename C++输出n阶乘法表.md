![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210713143430104.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
C++ 版：
```cpp
#include <iostream>
using namespace std;

int main(){
	int x;
	cin >> x;
	
	for (int n = 1;n <= x;n ++){
		for (int m = 1;m < n + 1;m ++){
			cout << n << "×" << m << "=" << n * m << " ";
		}
		cout << endl;
	}
	return 0;
} 
```
Python 版：

```py
for o in range(1,10):
	for t in range(1,o+1): 
		print('{0}×{1}={2}'.format(o,t,o * t),end = '')
	print() 
```
