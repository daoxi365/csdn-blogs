![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210709201809639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
程序：

```cpp
//Author:PanDaoxi (File 7)
#include <iostream>
using namespace std;

int main(){
	int sh,sm,eh,em;
	cin >> sh >> sm >> eh >> em;
	int x = sh * 60 + sm;
	int y = eh * 60 + em;
	int z = y - x;
	cout << z / 60 << " " << z % 60 << endl; 
	return 0;
} 
```

