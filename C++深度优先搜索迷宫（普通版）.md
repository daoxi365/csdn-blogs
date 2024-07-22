![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0872d5347bb7427e921b52d0344e5b80.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int dx[5]={-1,0,1,0},dy[5]={0,1,0,-1};
int G[51][51],vis[51][51],n,sx,sy,ex,ey;
bool f=false;
void dfs(int x,int y){
	if(x==ex&&y==ey){
		cout<<"yes";
		f=true;
		return;
	}
	for(int i=0;i<4;i++){
		int x2=x+dx[i],y2=y+dy[i];
		if(x2>=1&&x2<=n&&y2>=1&&y2<=n&&G[x2][y2]&&!vis[x2][y2]){
			vis[x2][y2]=1;
			dfs(x2,y2);
		}
	}
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>G[i][j];
		}
	} 
	cin>>sx>>sy>>ex>>ey;
	if(sx==ex&&sy==ey){
		cout<<"yes";
		return 0;
	}
	vis[sx][sy]=1;
	dfs(sx,sy);
	if(!f){
		cout<<"no";
	}
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3972056104bf43879b5b8a420301a9ed.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

