![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6311d6beb66b4195a14824bbd9a1bbb9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/578a04c9a4104d77a93e6ca72751426f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6fa5e383ada54fc193ae2661950292c2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9337134fefd54c7bacc0f944cace7ce2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9e6b439c01cf4b99b91fd3933023ae3c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int g[101][101],du[101],c[101];
//g=邻接数组 du=顶点读书 c存储路径
int n,e,ci; //n=顶点数 e=边数 ci=搜索的点数 
//搜索函数
void find(int i){
	for(int j=1;j<=n;j++){
		if(g[i][j]==1){
			g[j][i]=g[i][j]=0; //擦除i-j的连线 
			find(j); 
		}
	}
	c[++ci]=i;
} 
int main(){  
	int x,y,k=0,start=1;
	cin>>n>>e;
	//创建邻接数组
	for(int i=1;i<=e;i++){
		cin>>x>>y;
		g[y][x]=g[x][y]=1; //无向图
		du[x]++;
		du[y]++; 
	} 
	//奇点个数
	for(int i=1;i<=n;i++){
		if(du[i]%2){
			start=i;
			k++;
		}
	} 
	//判断奇点个数
	if(k==0||k==2){
		ci=0;
		find(start);
		for(int i=1;i<=ci;i++){
			cout<<c[i]<<" ";
		}
	} 
	else{
		cout<<"-1"<<endl; 
	}
	return 0;	
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/31d3c7c68edd402fa89de5ebc588d466.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

