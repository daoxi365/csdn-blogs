![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/76bc34f490584234b4aef3a1f909ca66.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/da7d30b7c63f4331add2197d9d988599.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
//book=标记岛屿是否被搜索过
//e=地图
//n=岛屿数量
//m=桥的数量 
int book[101],e[101][101],n,m;
//计数器：搜索过的岛屿
int sum=0; 
//深搜函数
void dfs(int j){
	cout<<j<<" "; //输出当前所在岛屿 
	sum++;
	if(sum==n) return; //搜索完成 
	//搜索j是否可以去其他岛屿
	for(int i=1;i<=n;i++){
		//1.岛屿：j和i是否相通
		//2.判断岛屿i是否被搜索过
		if(e[i][j]==1&&book[i]==0){
			book[i]=1;
			dfs(i);
		} 
	} 
} 
int main(){
	cin>>n>>m;
	int a,b;
	for(int i=1;i<=m;i++){
		cin>>a>>b;
		e[a][b]=e[b][a]=1;
	}
	book[1]=1; //从1开始搜索
	dfs(1); //开始深搜 
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c1eaf1c13e0a482691d8ab9896c97ac4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

