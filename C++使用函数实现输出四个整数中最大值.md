![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720153946227.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int bigest(){
	int a[4],max = 0;
	for(int i=0;i<4;i++){
		cin>>a[i];
		if(a[i]>max) max=a[i];
	}
	return max;
}

int main(){
	cout<<bigest()<<endl;
	return 0;
}
```

