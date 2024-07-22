![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5fd4e0180e7f4789930432ab475143ad.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cb8e612d2cca433ea9d4b0471c31441f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20c7b03fd373486a95bc155490e41ba1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4f72569fe09c4b728afcaf5655c1ed53.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int g[1001][1001],vis[1001],n,e,sum=0;
//深搜函数
void dfs(int cur){
	cout<<cur<<" "; //搜索到 
	sum++;
	if(sum==n) return; //结束 
	for(int i=1;i<=n;i++){
		//判断当前点是否可用 
		if(g[cur][i]==1&&vis[i]!=1){
			vis[i]=1;
			dfs(i);
		}
	}
} 
int main(){
	int a,b;
	cin>>n>>e;
	for(int i=1;i<=e;i++){
		cin>>a>>b;
		g[a][b]=1;
		g[b][a]=1; //无向图 
	}
	//搜索
	vis[1]=1;
	dfs(1); 
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/451f5a6b3c6c407388bad39947b34892.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

