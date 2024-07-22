![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210715154946374.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
😅还是做一做吧，虽然有点幼稚
```cpp
#include <iostream>
using namespace std;

int main(){
	int arr[5][3] = {78,67,34,99,44,88,66,66,44,33,33,99,78,87,66};
	int sum1 = 0,sum2 = 0;
	for (int i = 0;i < 5;i ++){
		sum1 = arr[i][0] + arr[i][1] + arr[i][2];
		if (sum2 < sum1){
			sum2 = sum1;
		}
	}
	cout << sum2 << endl;
	return 0;
} 
```
