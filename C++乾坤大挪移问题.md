![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210716143019198.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int a[10][10];
	for (int i = 0;i < 5;i ++){
		for (int j = 0;j < 5;j ++){
			cin >> a[i][j];
		}
	}
	for (int i = 0;i < 5;i ++){
		for (int j = 4;j > 0;j --){
			swap(a[i][j],a[i][j - 1]);
		}
	} 
	for (int i = 0;i < 5;i ++){
		for (int j = 0;j < 4;j ++){
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}
```

