![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/77051e21d14a45ac84cda4d17800d556.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4ecf7128625f4b31afb85cb230f1acea.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e5408bae6d5f470a8b18cc84d86133c4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
测试数据如下：


6 6 3 4
0 1 0 1 1 0
0 0 0 1 1 1
1 0 1 1 0 1
0 0 0 1 0 0
0 1 1 1 1 0
0 0 0 0 0 0

```

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
//定义结构体
struct node{
	int x,y;
}que[1001];
int head=1,tail=1; 
//头指针、尾指针分别对应当前搜索对象的下标和下个元素的位置
int m,n,x,y,map[101][101]; //m,n地图行、列 x,y小童位置的坐标
int sum=0; //计数器：岛屿的面积 
//搜索方向
int next[4][2]={{-1,0},{0,1},{1,0},{0,-1}}; 
void bfs(){
	//第一个搜索的点 
	que[tail].x=x;
	que[tail].y=y;
	map[x][y]=0;
	tail++;
	//更新岛屿面积
	sum++;
	//广搜核心代码
	while(head<tail){
		for(int i=0;i<=3;i++){
			int tx=que[head].x+next[i][0],
			ty=que[head].y+next[i][1];
			//判断是否可以通过
			if(tx<1||tx>m||ty<1||ty>n) continue;
			//判断是否为陆地
			if(map[tx][ty]==1){
				que[tail].x=tx;
				que[tail].y=ty;	
				tail++;
				map[tx][ty]=0;
				sum++;
			} 
		}
		//搜索完以后
		head++; 
	} 
}
int main(){
	//输入地图行列、小童的坐标 
	cin>>m>>n>>x>>y;
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n;j++){
			cin>>map[i][j];
		}
	}
	//广度优先搜索
	bfs();
	//输出信息
	cout<<sum<<endl; 
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2a25224d326748cf93cf98c6b2d0d327.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

