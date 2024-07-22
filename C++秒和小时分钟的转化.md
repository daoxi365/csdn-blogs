![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210712145941557.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	int all = 8000,s,m,h;
	s = all % 60;;
	m = all / 60 % 60;
	h = all / 60 / 60;
	cout << "8000秒=" << h << "小时" << m << "分钟" << s << "秒" << endl;
	return 0;
} 
```

