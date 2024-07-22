![C++](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/21afcd02863341c8843acc971e191e67.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1d1220a0a0ad4ddb83bcb26ac37a7a67.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0d0766623f7448e9af2f11fb0fef1ebc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/58516178718c4b0c9d6ccbace9f338d3.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ec54b771eb0a42f08eeb6cfab53185c4.png)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int dp[101][101];
void lcs(string & s1,string & s2){
	int m=s1.size();
	int n=s2.size();
	s1="#"+s1;
	s2="#"+s2;
	//动规核心
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n;j++){
			//第一种情况：末尾字母相等
			if(s1[i]==s2[j]) dp[i][j]=dp[i-1][j-1]+1; 
			//第二种情况
			else dp[i][j]=max(dp[i-1][j],dp[i][j-1]);	 
		}
	} 
	cout<<dp[m][n]<<endl;
} 
int main(){
	string s1,s2;
	cin>>s1>>s2;
	//求出最长公共子序列
	lcs(s1,s2); 
	return 0;
}
 
```

