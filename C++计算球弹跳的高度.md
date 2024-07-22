![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210709191315128.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
程序：

```cpp
//Author:PanDaoxi (File 2) 
#include <iostream>
using namespace std;

int main(){
	double ten,h,sum;
	cin >> h;
	sum += h;
	
	int n = 10;
	while (n - 1 > 0){
		sum += h;
		h /= 2;
		n --;
	}
	ten = h;
	cout << sum << endl;
	cout << ten << endl;
	return 0;
} 
```

