![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210713163950235.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int a[101],n,max,min;
	cin >> n;
	for (int i = 0;i < n;i ++){
		cin >> a[i];
	}
	
	max = a[0],min = a[0];
	for (int i = 0;i < n;i ++){
		if (max < a[i]) max = a[i];
		if (min > a[i]) min = a[i];
	}
	
	cout << max << " " << min << endl;
	return 0;
} 
```

