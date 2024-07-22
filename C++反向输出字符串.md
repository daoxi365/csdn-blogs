![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719151752529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[101];
	cin.getline(a,101);
	for(int i=strlen(a)-1;i>=0;i--) cout<<a[i]<<a[i];
	return 0;
} 
```

