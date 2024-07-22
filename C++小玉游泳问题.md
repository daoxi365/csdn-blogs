题目是这样的：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210709184820761.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
我的解题方法：

```cpp
//Author:PanDaoxi (File 1) 
#include <iostream>
using namespace std;

int main(){
	double m,step;
	cin >> m;
	
	int n;
	step = 2;
	while (m > 0){
		n += 1;
		step *= 0.98;
		m -= step;
	}
	cout << n << endl;
	return 0;
} 
```

