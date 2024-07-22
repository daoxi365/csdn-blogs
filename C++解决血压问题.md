![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210713154742225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n,a,b,c,d;
	cin >> n;
	
	for (int i = 1;i <= n;i ++){
		cin >> a >> b;
		if (90 <= a && a <= 140 && 60 <= b && b <= 90) {
			c ++;
		}
		else {
			d = c;
			c = 0;
		}
	}
	if (d > c) cout << d << endl; 
	else cout << c << endl;
	return 0;
}
```

