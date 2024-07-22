![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210714152133879.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n,sum;
	cin >> n;
	int arr[n];
	
	for (int i = 1;i <= n;i ++){
		cin >> arr[i];
	}
	for (int i = 0;i <= n;i ++){
		sum += arr[i];
	}
	
	double avg = sum / n;
	for (int i = 0;i <= n;i ++){
		if (arr[i] > avg) cout << arr[i] << " ";
	}
	return 0;
```

