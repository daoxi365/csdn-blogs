![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/173ba00b14774f908005c3fa83c58b6d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;
int main(){
	int a[101],n,m,t,s=0,count;
	cin>>n;
	count=n;
	for(int i=0;i<n;i++){
		cin>>t;
		if(t==1) a[i]=1;
		else a[i]=2;
	}
	cin>>m;
	int i=0;
	while(count>1){
		if(a[i]>0) s++;
		if(s==m){
			a[i]--;
			if(a[i]==0) count--;
			s=0;
		}
		i++;
		i%=n;
	}
	for(int i=0;i<n;i++) if(a[i]) cout<<(i+1)<<endl;
	return 0;
}
```

