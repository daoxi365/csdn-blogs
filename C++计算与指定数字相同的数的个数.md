![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210712143329257.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n,m,a,ans = 0;
	cin >> n >> m;
	while (n --){
		cin >> a;
		if (a == m) {
			ans ++;
		}
	}
	cout << ans << endl;
	return 0;
} 
```

