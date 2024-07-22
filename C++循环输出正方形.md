![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210715143338145.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n;
	cout << "请输入边长：";
	cin >> n;
	
	for (int i = 1;i <= n;i ++){
		if (i == 1 || i == n){
			for (int j = 1;j <= n;j ++){
				cout << "*";
			}
			cout << endl;
		}
		if (i >= 2 && i <= n - 1){
			cout << "*";
			for (int k = 1;k <= n - 2;k ++){
				cout << " ";
			} 
			cout << "*" << endl;
		}
	}
	
	return 0;
} 
```

