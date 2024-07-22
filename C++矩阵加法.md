![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2021071614484238.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210716144845105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int a[100][100],b[100][100],n,m;
	cin >> n >> m;
	
	for (int i = 0;i < n;i ++){
		for (int j = 0;j < m;j ++){
			cin >> a[i][j];
		}
	}
	
	for (int i = 0;i < n;i ++){
		for (int j = 0;j < m;j ++){
			cin >> b[i][j];
		}
	}
	for (int i = 0;i < n;i ++){
		for (int j = 0;j < m;j ++){
			cout << a[i][j] + b[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
} 
```
从下一章起，我的代码将变为紧凑的风格。
