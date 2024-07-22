题目中输入的`4*4`的数组表示走过这个点所用的时间，求最短时间。
![](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/769529c0e3c7487c9acf733ebe9625a2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1e9e0698849544ccba6c61756fd61272.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
//a=地图
//n,m=地图的宽和高
//mins,maxs=最短时间
int a[101][101],book[101][101],n,m,mins=100000,maxs=0;
//sx,sy=起点坐标
//ex,ey=终点坐标
int sx,sy,ex,ey;
//搜索：上右下左
int f[4][2]={{-1,0},{0,1},{1,0},{0,-1}};
//深搜函数
void dfs(int x,int y){
	//假如到终点
	if(x==ex&&y==ey){
		mins=(maxs<mins?maxs:mins);
		return;
	}
	//搜索 
	for(int i=0;i<4;i++){
		int nx=x+f[i][0],ny=y+f[i][1];
		//在地图中且没被搜索过 
		if(nx>=1&&nx<=n&&ny>=1&&ny<=m&&book[nx][ny]==0){
			book[nx][ny]=1;
			maxs+=a[nx][ny]; //累加时间 
			dfs(nx,ny); //递归 
			//回溯
			book[nx][ny]=0;
			maxs-=a[nx][ny]; 
		} 
	}	
} 
int main(){
	cin>>n>>m;
	cin>>sx>>sy>>ex>>ey;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cin>>a[i][j];
		}
	}
	book[sx][sy]=1;
	maxs=a[sx][sy];
	dfs(sx,sy);
	cout<<mins<<endl;
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/639ebf9387d74b70891b8b1c9d9b6ca9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

