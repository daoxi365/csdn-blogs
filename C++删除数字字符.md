![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720141242170.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	int n=0;
	char a[31],b[31];
	cin.getline(a,31);

	for(int i=0; i<strlen(a); i++) {
		if(a[i]>='0'&&a[i]<='9') n++;
		else cout<<a[i];
	}
	cout<<endl<<n<<endl;
	return 0;
}
```

