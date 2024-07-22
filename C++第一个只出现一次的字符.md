![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720151609939.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[100001];
	cin.getline(a,100001);
	int b[26];
	for(int i=0;i<strlen(a);i++) b[a[i]-97]++;
	for(int i=0;i<strlen(a);i++){
		if(b[a[i]-97]==1) {
			cout<<a[i];
			return 0;
		}
	}
	cout<<"no";
	return 0;
}
```

