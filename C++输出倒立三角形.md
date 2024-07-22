![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210715155754693.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	for (int i = 1;i <= 4;i ++){
		for (int j = 2;j <= i;j ++) cout << 1;
		for (int k = 2 * i - 1;k <= 7;k ++) cout << 0;
		for (int l = 2;l <= i;l ++) cout << 1;
		cout << endl;
	}
	return 0;
} 
```

