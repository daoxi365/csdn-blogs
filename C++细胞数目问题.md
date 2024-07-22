![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/906318fceaff4d2ab883cd5c871c4f84.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
看到这道题时我手头这台电脑没有编辑器，听说微软出了一个`vscode.dev`，在线编辑器，正好试试。但是我以前没有用过VSCode系列产品，试一试看吧，主要看代码就行：
测试数据：

```cpp
4 10
0 2 3 4 5 0 0 0 6 7
1 0 3 4 5 6 0 5 0 0
2 0 4 5 6 0 0 6 7 1
0 0 0 0 0 0 0 0 8 9
```

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct node{
	int x,y;
} que[2501];
int map[51][
1],head=1,tail=1,book[51][51],sum=0;
int next[4][2]={{0,1},{1,0},{0,-1},{-1,0}},m,n,x,y,tx,ty;
//广搜函数
void bfs(int x,int y){
	sum++;
	map[x][y]=0;
	que[tail].x=x;
	que[tail].y=y;
	book[x][y]=1;
	tail++;
	while(head<tail){
		for(int k=0;k<=3;k++){
			tx=que[head].x+next[k][0];
			ty=que[head].y+next[k][1];
			if(tx<0||tx>=m||ty<0||ty>=n){
				continue;
			}
			if(map[tx][ty]>0&&book[tx][ty]==0){
				map[tx][ty]=0;
				book[tx][ty]=1;
				que[tail].x=tx;
				que[tail].y=ty;
				tail++;
			}
		}
		head++;
	}
} 
int main(){
	cin>>m>>n;
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			cin>>map[i][j];
		}
	}
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			if(map[i][j]){
				bfs(i,j);
			}
		}
	}
	cout<<sum<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f1f735884bcd4d25b80d444ee1766312.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4275cce9c85f40008e06dde3598669c6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
终究还是运行不了，回家再说……

<hr>

我回家了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/47081b6fb5d94c46ae93c2e45d2cc589.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
还是本地的`dev-cpp`好用点，
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2eb40412421d44d29ae12316401cf94a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

