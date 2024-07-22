![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/478ddd32d2fe40699df26d2e16346ebc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9caf315a0276419ebdc177cbe40430a0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
图中`x`表示无法移动。不可以走走过的路程，所以为`x`。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3b6d0bcf85a7461686dad8a5f2827c0a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（个人喜欢“上→右→下→左”的顺序）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/328413d0445f4d4589543da0f16e61cf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
//创建模拟地图、记录点否用过的变量 
int G[105][105],vis[105][105],n; 
//位置变化：上右下左 
int dx[5]={-1,0,1,0},  //x坐标的位置变化 
    dy[5]={0,1,0,-1};  //y坐标的位置变化 
//标记是否有解
bool f=false;
//深搜函数
void dfs(int x,int y){
	//如果(x,y)存在目标，则有解 
	if(G[x][y]==2){
		f=true;
		return;
	}
	//向四个方向搜索 
	for(int i=0;i<4;i++){
		//更新坐标位置 
		int x2=x+dx[i],y2=y+dy[i]; 
		//判断是否在地图中
		//如果G[x2][y2]!=1，则可以搜索
		//vis[x2][y2]==0，没走过，可以搜索 
		if(x2>=0&&x2<n&&y2>=0&&y2<n&&G[x2][y2]!=1&&vis[x2][y2]==0){
			//标记这个点已经使用 
			vis[x2][y2]=1;
			//从当前的点递归搜索 
			dfs(x2,y2);
			//还原状态
			vis[x2][y2]=0; 
		}
	} 
} 
int main(){
	cin>>n;
	//初始化地图 
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>G[i][j];
		} 
	}
	//搜索：先处理两种简单情况，如果没有则搜索
	if(G[0][0]==1){ //如果当前位置就是障碍，则无法搜索
		cout<<"NO";
		return 0;
	} 
	else if(G[0][0]==2){ //如果当前位置就是目标，则不用搜索，直接成功 
		cout<<"YES";
		return 0;
	}
	else{ //如果都没有出现则进行深度优先搜索
		vis[0][0]=1;
		dfs(0,0);
		if(f){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
	return 0;
} 
```

