![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9a4eff34afcf4f908e7d10d67ac662cb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int a[10001]={};
int main(){
	int n,m,s,t,max=0;
	cin>>n;
	for(int j=0;j<n;j++){
		cin>>t;
		a[t]++;
	}
	for(int i=1;i<10001;i++){
		if(a[i]>max) max=a[i];
	}
	for(int i=0;i<10001;i++){
		if(a[i]==max) cout<<i<<" "<<max<<endl;
	}
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e080cef47c074399a783a77b4423a335.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

