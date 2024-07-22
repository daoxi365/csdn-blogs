![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/bbf87d1df6824921acb47c0f0762d5f5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b849c563a1e74fd5a1efb0068a58ffec.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
//map=地图 
char map[30][30];
//vis=标记字母是否使用过
//r,s=矩阵的长和宽
//maxs=最大值
//cnt=每次搜索的值 
int vis[30]={},r,s,maxs=0,cnt=1; 
//搜索方向：上右下左 
int f[4][2]={{-1,0},{0,1},{1,0},{0,-1}};
//深搜函数 
void dfs(int x,int y){
	if(cnt>maxs) maxs=cnt;
	for(int i=0;i<4;i++){
		int x1=x+f[i][0],y1=y+f[i][1];
		//不超过边界且字母不能重复 
		//map[x1][y1]=储存的字母 
		if(x1>=1&&x1<=r&&y1>=1&&y1<=s&&vis[map[x1][y1]-'A']==0){
			cnt++;
			vis[map[x1][y1]-'A']=1; //标记已经使用
			dfs(x1,y1);
			//回溯
			vis[map[x1][y1]-'A']=0;
			cnt--; 
		}
	}
} 
int main(){
	cin>>r>>s;
	for(int i=1;i<=r;i++){
		for(int j=1;j<=s;j++){
			cin>>map[i][j];
		}
	} 
	vis[map[1][1]-'A']=1;
	dfs(1,1);
	cout<<maxs<<endl;
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f321c01bcdec4b0782a84b493af4e22b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

