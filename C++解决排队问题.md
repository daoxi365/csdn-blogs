![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210714145126858.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int n,i,state[51];
	cin >> n;
	for (i = 1;i <= n;i ++){
		state[i] = 1;
	}
	for (i = 1;i <= n;i ++){
		if (i % 2 == 0) state[i] = 1 - state[i];
		if (i % 5 == 0 && state[i] == 1) state[i] = 1 - state[i];
	}
	for (i = 1;i <= n;i ++){
		if (state[i] == 1) cout << i << " ";
	}
	return 0;
}
```

