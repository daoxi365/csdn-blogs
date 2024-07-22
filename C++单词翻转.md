![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719155000619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	const int n=501;
	char a[n];
	int len,s=0,c=0,k=0;
	cin.getline(a,n);
	len=strlen(a);
	for(int i=0;i<len;i++){
		if(a[i]==' '||i==len-1){
			c++;
			if(i==len-1) k=i;
			else k=i-1;
			for(int j=k;j>=s;j--) cout<<a[j];
			if(c==1){
				cout<<" ";
				c=0;
			} 
			s=i+1;
		}
	}
	cout<<endl;
	return 0;
} 
```

