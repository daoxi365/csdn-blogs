![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5e27dcf35dd24770bc856db95df9ef39.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int l,m,x,y,sum=0;
	bool a[10001];
	cin>>l>>m;
	for(int i=0;i<=l;i++){
		a[i]=true; //有树 
	}
	for(int i=0;i<m;i++){
		cin>>x>>y;
		for(int j=x;j<=y;j++){
			if(a[j]) a[j]=false; //无树 
		}
	} 
	for(int i=0;i<=l;i++){
		if(a[i]) sum++;
	}
	cout<<sum;
	return 0;
}

```

