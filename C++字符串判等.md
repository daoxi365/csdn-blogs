![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719153106262.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[101],b[101],c[101],d[101];
	cin.getline(a,101);
	cin.getline(b,101);
	int k=0;
	for(int i=0;i<strlen(a);i++){
		if(a[i]!=' '){
			if(a[i]>='a'&&a[i]<='z') c[k++]=a[i]-32;
			else c[k++]=a[i];
		}
	}
	int h=0;
	for(int i=0;i<strlen(b);i++){
		if(b[i]!=' '){
			if(b[i]>='a'&&b[i]<='z') d[h++]=b[i]-32;
			else d[h++]=b[i];
		}
	}
	if(strcmp(c,d)) cout<<"NO"<<endl;
	else cout<<"YES"<<endl;
	
	return 0;
}
```

