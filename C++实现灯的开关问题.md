![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210714141508449.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n,arr[101];
	cin >> n;
	
	for (int a = 1;a <= n;a ++){
		arr[a] = 1;
	} 
	for (int b = 1;b <= n;b ++){
		for (int c = 2;c <= 5;c ++){
			if (b % c == 0) arr[b] = 1 - arr[b];
		}
	}
	for (int d = 1;d <= n;d ++){
		if (arr[d] == 1) cout << d << " ";
	}
	return 0;
} 
```

