![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d7bef00736e645b2bc895d519b767f49.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c0388828b25e42e389da4d5d6a84a0d6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5fbc0bcae1e5435d9fc11512e931d0a4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/09520ec9650148009a4fdd867809b4e4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_18,color_FFFFFF,t_70,g_se,x_16)

```cpp
测试数据：


4 4 1
1 2 3 4
#*##
**##
###*
****
```

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
char map[201][201]; //map=字符型地图 *=道路 #=机关 
bool vis[201][201]; //记录是否走过 0=未走过 1=走过 
int n,m,t; //n,m=地图大小 t=装备数量
int sx,sy,ex,ey; //sx,sy=起始坐标 ex,ey=终点坐标
int minTime=100001;
int next[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
void dfs(int i,int j,int life,int time){
	//走到终点就结束搜索
	if(i==ex&&j==ey){
		if(time<minTime) minTime=time;
		return;
	} 
	//搜索周围四个方向
	for(int k=0;k<=3;k++){
		int tx=i+next[k][0],
		ty=j+next[k][1];
		//没有越界且没有走过
		if(tx>=1&&tx<=n&&ty>=1&&ty<=m&&!vis[tx][ty]){
			//优化深搜
			if(time+1>=minTime){
				continue; 
			} 
			vis[tx][ty]=1;
			//顺利通过
			if(map[tx][ty]=='*'&&life>=0){
				dfs(tx,ty,life,time+1);   //递归 
			} 
			if(map[tx][ty]=='#'&&life>0){
				dfs(tx,ty,life-1,time+1); //递归 
			}
			vis[tx][ty]=0; //回溯 
		} 
	} 
} 
int main(){
	//输入 
	cin>>n>>m>>t;
	cin>>sx>>sy>>ex>>ey;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cin>>map[i][j];
		}
	}
	//深搜
	vis[sx][sy]=1;
	dfs(sx,sy,t,0); //t=装备 0=所用时间
	//输出 
	if(minTime==100001){
		cout<<"-1";
	} 
	else{
		cout<<minTime;
	}
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1eeafdbf9a2f45a5b8192c0c54a54fa5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

