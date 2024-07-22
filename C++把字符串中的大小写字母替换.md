![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210716155531801.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	string str;
	cin>>str;
	for(int i=0;i<str.length();i++){
		if(str[i]>='A'&&str[i]<='Z') str[i]+=32;
		else str[i]-=32;
	}
	cout<<str<<endl;
	return 0;
} 
```

