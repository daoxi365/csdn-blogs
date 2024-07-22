![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6abe2f5751594dc8b649b9f91f9a617f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
那个医生，带辰辰到山上采药，每株草药都有自己的价值，如何在一定时间内最快得到最高价值。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f078040e8bd045acb4dec12b30643a45.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
这个题好坑啊，和上道题一模一样。
离离原上谱，一岁一枯荣。

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int w[101],c[101],f[101][101];
int m,n;
int main(){
	cin>>m>>n;
	for(int i=1;i<=n;i++) cin>>w[i]>>c[i]; 
	//动态规划
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
		if(j>=w[i]) f[i][j]=max(f[i-1][j],f[i-1][j-w[i]]+c[i]);
		else f[i][j]=f[i-1][j];		
		}
	} 
	cout<<f[n][m];
	return 0;
}
```

