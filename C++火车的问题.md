![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/150e0d3fc68c4f3d816655ea7f094470.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int a[20]={0,1,1},b,n,m,x,k;
	cin>>b>>n>>m>>x;
	if(x==1){
		cout<<a;
		return 0;
	}
	for(int i=3;i<20;i++) a[i]=a[i-1]+a[i-2];
	if(n>4) k=(m-(a[n-3]+1)*b)/(a[n-2]-1);
	int num=(a[x-1]-1)*k+(a[x-2]+1)*b;
	cout<<num<<endl;
	return 0;
}
```

