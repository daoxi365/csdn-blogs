![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5037dd6241eb40f895d82b7dc4800f55.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream> 
#include <algorithm>
using namespace std;
bool cmp(int n){
	int m=n,x,y=0,a[11],b[11];
	while(m!=0){
		x=m%10;
		m/=10;
		a[y++]=x;
	}
	for(int i=0;i<y;i++){
		b[i]=a[y-i-1];
	}
	sort(a,a+y);
	for(int i=0;i<y;i++){
		if(a[i]!=b[i]) return false;
	}
	return true;
}
int main(){
	int n,sum=0;
	cin>>n;
	for(int i=10;i<=n;i++){
		if(cmp(i)) sum++;
	}
	cout<<sum<<endl;
	return 0;
}
```

