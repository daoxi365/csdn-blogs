![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210716140049717.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int a[100][100],r,c,n,m;
	cin >> r >> c;
	for (int i = 0;i < r;i ++){
		for (int j = 0;j < c;j ++){
			cin >> a[i][j];
		}
	}
	cin >> n >> m;
	for (int i = 0;i < r;i ++){
		swap(a[n - 1][i],a[m - 1][i]);
	}
	for (int i = 0;i < r;i ++){
		for (int j = 0;j < c;j ++){
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
} 
```

