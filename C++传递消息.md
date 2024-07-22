![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5e897969de0c47db950040c6ef4ea8d7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e625ea1b9afc4f11835a8f6cc5216e18.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int dx[5]={-1,0,1,0},dy[5]={0,1,0,-1};
int G[51][51],n,m;
void dfs(int x,int y){
	for(int i=0;i<4;i++){
		int xx=x+dx[i],yy=y+dy[i];
		if(xx>=0&&xx<n&&yy>0&&yy<n&&G[xx][yy]==0){
			G[xx][yy]=1;
			dfs(xx,yy);
		}
	}
} 
int main(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>G[i][j];
		}
	}
	int res=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(G[i][j]==0){
				G[i][j]=1;
				dfs(i,j);
				res++;
			}
		}
	}
	cout<<res<<endl;
}
```

