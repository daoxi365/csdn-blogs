给出题的人点个赞，好有思想！！！
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ea31c9f76ef14ddd89dd2dfed24141bc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1994801d95d949debea14c291a218b96.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3fd4bd00e09d4c718ddd26de7309f233.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/25e1268975d946fdac85abf6d46e0997.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c6fb23e9ef3b4045a0e70ea9b9db3ea6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cff0dc43de524028991cd52e532f0eea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/275ccdc2859d435a8f707ad063f8a77b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a34d6c9f3b3c43d5b4bb9b5696ad8ddf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/00d3e09080504dc6beb33c11ceec1f85.png)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int a[101],n;
void lis(int a[],int n){
	int dp[101]={};
	fill(dp+1,dp+1+n,1); //从1填充到最后，填充值为1
	//动规核心：完全背包
	for(int i=2;i<=n;i++){
		//因为dp[1]=1，所以从2开始判断
		for(int j=1;j<i;j++){
			if(a[i]>a[j]&&dp[j]+1>dp[i]) dp[i]=dp[j]+1;
		} 
	} 
	//获取最优解
	int l=1;
	for(int i=1;i<=n;i++){
		l=max(l,dp[i]);
	} 
	cout<<l;
}
int main(){ 
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	lis(a,n);
	return 0;
}
 
```

