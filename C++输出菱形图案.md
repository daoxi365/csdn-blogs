![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210715142514468.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	for (int i = 1;i <= n;i ++){
		for (int j = 1;j <= n - i;j ++){
			cout << " ";
		}
		for (int k = 1;k <= 2 * i - 1;k ++){
			cout << "*";
		}
		cout << endl;
	}
	for (int i = 1;i <= n - 1;i ++){
		for (int j = 1;j <= i;j ++){
			cout << " ";
		}
		for (int k = 1;k <= 2 * (n - i) - 1;k ++){
			cout << "*";
		}
		cout << endl;
	}
	return 0;
} 
```

