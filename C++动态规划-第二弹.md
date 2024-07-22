![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e719167979184b0c9aad7ddbe18f9698.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a20200d89b5e4d3c87da1c4a95b17b79.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
嚯，这是什么奇怪的题目![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0b27e9369c7d4999b075b98ffb4cfb9c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d792879c75aa4af68a9a9dd52c8f74d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3b3c39b1722244d5a51c689f5c1bb567.png)
这样可以递归：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int f(int i,int j){
	if(i==1||j==1) return 1;
	else return f(i-1,j)+f(i,j-1);
}
int main(){
	int n,m;
	cin>>n>>m;
	cout<<f(n,m);
	return 0;
} 
```
也可以使用动规：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
//动态规划 
int pathSum_DP(int i,int j){
	if(i==1||j==1) return 1;
	const int x=i,y=j;
	int dp[x+1][y+1]={};
	for(int k=1;k<=i;k++){
		dp[k][1]=1;
	}
	for(int l=1;l<=j;l++){
		dp[1][l]=1;
	}
	//核心
	for(int k=2;k<=i;k++){
		for(int l=2;l<=j;l++){
			dp[k][l]=dp[k-1][l]+dp[k][l-1];
		}
	} 
	return dp[i][j];
}
int main(){
	int n,m;
	cin>>n>>m;
	cout<<pathSum_DP(n,m);
	return 0;
} 
```
再次优化为一维数组：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int pathSum_DP(int m,int n){
	if(m==1||n==1) return 1;
	const int x=n;
	//再次优化
	int dp[x+1]={};
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n;j++){
			if(i==1||j==1) dp[j]=1;
			else dp[j]=dp[j]+dp[j-1]; 
		}
	} 
	return dp[n];
}
int main(){
	int m,n;
	cin>>m>>n;
	cout<<pathSum_DP(m,n);
	return 0;
}
```

