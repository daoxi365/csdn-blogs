题目：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2021070919242468.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
程序：

```cpp
//Author:PanDaoxi (File 3) 
#include <iostream>
using namespace std;

int main(){
	int day;
	cin >> day;
	
	int money,n = 0;
	while (day > 0){
		n ++;
		day -= n;
		money += n * n;
	}
	money += day * n;
	cout << money << endl;
	return 0;
}
```

