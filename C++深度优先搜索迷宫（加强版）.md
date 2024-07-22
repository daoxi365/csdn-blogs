![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/843f7e28f31b4d8b981498b70d2337a4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d45fb906bb9e4d9c86e3e6f46cc3fc6b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
普通版代码：
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
加强版代码：
```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int dx[5]={-1,0,1,0},dy[5]={0,1,0,-1};
int G[31][31],vis[31][31],n,sx,sy,ex,ey,A[1000][3];
bool f=false;
void dfs(int x,int y,int d){
	if(x==ex&&y==ey){
		for(int i=0;i<d-1;i++){
			cout<<"("<<A[i][0]<<","<<A[i][1]<<")"<<"-->"; 
		} 
		cout<<"("<<ex<<","<<ey<<")";
		f=true;
		return;
	}
	for(int i=0;i<4;i++){
		int xx=x+dx[i],yy=y+dy[i];
		if(xx>=1&&xx<=n&&yy>=1&&yy<=n&&G[xx][yy]&!vis[xx][yy]){
			vis[xx][yy]=1;
			A[d][0]=xx,A[d][1]=yy;
			dfs(xx,yy,d+1);
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
		cout<<"yes"<<endl;
		return 0;
	}
	A[0][0]=sx,A[0][1]=sy;
	vis[sx][sy]=1;
	dfs(sx,sy,1);
	if(!f){
		cout<<"no"<<endl;
	} 
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4da5d3ff301745c093134698791255e1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
