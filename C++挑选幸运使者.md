![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/49f3557f0a1e4c1c92535f3d48fc94e6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std; 
int main(){
	int q[1001],n,front=0,rear=0,x,ans;
	cin>>n;
	for(int i=0;i<n;i++) q[i]=i+1;
	rear=n;
	while(rear!=front){
		for(int i=1;i<=2;i++){
			x=q[front];
			front=(front+1)%n;
			q[rear]=x;
			rear=(rear+1)%n;
		}
		ans=q[front];
		front=(front+1)%n;
	}
	cout<<ans<<endl;
	return 0;
}
```

