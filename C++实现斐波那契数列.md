![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2021071414112096.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream> 
using namespace std;

int main(){
	int n,arr[101];
	cin >> n;
	
	arr[1] = 1,arr[2] = 1;
	for (int i = 3;i <= n;i ++){
		arr[i] = arr[i - 1] + arr[i - 2];
	}
	cout << arr[n] << endl;
	return 0;
}
```

