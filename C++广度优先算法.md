![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/be44c33f6b5848afae05c5a73b27e88b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9c88ff54925a449ba19f59e065faec7e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4e9505b2d59c438d977e1fba6c7c6dfe.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d72f5dc31685465f957a1b946879fa8c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/19ec6fbf0b1c4acfacb5043731394129.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5c33c26daa804cdb872e6e676aa8938c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d5ef0dedca9349cea2cb786d851c6fef.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4e04f41b8d31409fbf5b3b4b9fcbb171.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/be7a06a493db4dd9853d23adf49a926d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/75120934e5364840b16c0faefbceaea8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_19,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/93da5159e265420dbd1cd8fce2e46932.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0bf8c530e8f94f1887401ac7824e14da.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
测试数据：

```cpp
5 4
0 1 0 0
0 0 0 0
0 0 1 0
0 1 0 1
0 0 0 1
1 1 4 3
```

程序如下：
```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
//定义结构体 
struct node{
	int x,y,step;
};
//map=地图 book=标记走过的点
int map[51][51],book[51][51];
//给结构体开长度 
struct node que[2501];
//移动的方向
int nt[4][2]={{-1,0},{0,1},{1,0},{0,-1}};
//m,n=地图大小 sx,sy=当前自己的位置
//p,q=目标位置 tx,ty=中间过程点的坐标 
int m,n,sx,sy,p,q,tx,ty;
//设置队首、队尾指针
int head=1,tail=1;
//标记是否有解
bool flag=false;
//广搜函数
void bfs(){
	//起点入队
	que[tail].x=sx;
	que[tail].y=sy;
	que[tail].step=0;
	tail++;
	//标记当前入队点
	book[sx][sy]=1;
	//循环：后序子节点入队 
	while(head<tail){
		//向四个方向搜索
		for(int i=0;i<4;i++){
			//获得子节点坐标
			tx=que[head].x+nt[i][0];
			ty=que[head].y+nt[i][1];
			//出界的情况跳过
			if(tx<1||tx>m||ty<1||ty>n) continue;
			//判断可以用的点
			if(map[tx][ty]==0&&book[tx][ty]==0){
				book[tx][ty]=1;
				//入队
				que[tail].x=tx;
				que[tail].y=ty;
				que[tail].step=que[head].step+1;
				tail++; 
			} 
			//是否找到目标
			if(tx==p&&ty==q){
				flag=true;
				break;
			} 
		} 
		//判断是否找到目标
		if(flag) break;
		//出队
		head++; 
	}
} 
int main(){
	//输入
	cin>>m>>n;
	//初始化地图
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n;j++){
			cin>>map[i][j];
		}
	} 
	//输入自己和目标的坐标
	cin>>sx>>sy>>p>>q;
	//广搜
	bfs();
	//输出解
	cout<<que[tail-1].step; 
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/eb285c5f716f44a38be7df3962861787.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)


<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b134943e25804704b11322a5a692b2c1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/bc0aa303194541b680cedad45ee0ce71.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/502c2c1d82a84cd29c973ec1d527e185.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/687ecedd8d5d4bda926e7c92a4ffbd38.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c532039e09c54b67a5426062ed27e00b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2c1ff999cf834718a06250ab0c6ec397.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/643d06fbeefc4699b8a5371f96cd6ea9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct node{
	int x,y,step;
}; 
struct node que[10001];
int book[101][101];
int next[12][2]={{-2,-2},{-2,2},
				{2,-2},{2,2},
				{-2,-1},{-2,1},
				{-1,2},{1,2},
				{2,1},{2,-1},
				{1,-2},{-1,-2}
				};
int head=1,tail=1;
int p1,q1,p2,q2,tx,ty,flag1=0,flag2=0;
int s1,s2;
void bfs(){
	que[tail].x=1;
	que[tail].y=1;
	que[tail].step=0;
	tail++;
	book[1][1]=1;
	while(head<tail){
		for(int i=0;i<12;i++){
			tx=que[head].x+next[i][0];
			ty=que[head].y+next[i][1];
			if(tx<1||tx>100||ty<1||ty>100) continue;
			if(book[tx][ty]==0){
				book[tx][ty]=1;
				que[tail].x=tx;
				que[tail].y=ty;
				que[tail].step=que[head].step+1;
				tail++;
			}
			if(flag1==0&&tx==p1&&ty==q1){
				flag1=1;
				s1=que[tail-1].step;
			}
			if(flag2==0&&tx==p2&&ty==p2){
				flag2=1;
				s2=que[tail-1].step;
			}
		}
		if(flag1==1&&flag2==1) break;
		head++;
	}
}
int main(){
	cin>>p1>>q1>>p2>>q2;
	bfs();
	cout<<s1<<endl<<s2<<endl;
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ab472260edeb4a2ba2ac7eee0dda117c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/bd5b2c8879244dedbb0fc797fe7cd1e3.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/126dc706a28a43bfbfd875852e728ef8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/55ba1a718e2245e3a078f9ca12af72f3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4a1cfd8138c84a35a410be7d335cc91f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct node{
	int x,y,step;
};
int book[101][101];
struct node map[10001];
int next[8][2]={
	{-2,-1},{-2,1},
	{-1,2},{1,2},
	{2,1},{2,-1},
	{1,-2},{-1,-2}
};
int n,m,sx,sy,tx,ty;
int head=1,tail=1;
void bfs(){
	map[tail].x=sx;
	map[tail].y=sy;
	map[tail].step=0;
	tail++;
	book[map[head].x][map[head].y]=0;
	while(head<tail){
		for(int i=0;i<8;i++){
			tx=map[head].x+next[i][0];
			ty=map[head].y+next[i][1];
			if(tx<1||tx>n||ty<1||ty>m) continue;
			if(book[tx][ty]==-1){
				map[tail].x=tx;
				map[tail].y=ty;
				map[tail].step=map[head].step+1;
				book[tx][ty]=map[tail].step;
				tail++;
			}
		}
		head++;
	}
}
int main(){
	cin>>n>>m>>sx>>sy;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			book[i][j]=-1;
		}
	}
	bfs();
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cout<<book[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1ad7241a37534a11898bd51c4b0fe464.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

