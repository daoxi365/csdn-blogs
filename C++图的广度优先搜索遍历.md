**预告：下周很大概率更新贪心算法。**
广度优先算法遍历有序图。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/342a5e5d51ee4f67a5ec8df8ea37e39b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c4ea9a94f3de4559a0a515d4b7a7d6f1.png)

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
void bfs(int cur){
	int head=0,tail=1;
	q[0]=cur; //q数组储存经过的点
	cout<<cur<<" "; //已经遍历的点
	vis[cur]=1;
	while(head<tail){
		for(int i=1;i<=n;i++){
			if(g[q[head]][i]==1&&vis){
				cout<<i<<" ";
				vis[i]=1;
				q[tail]=i;
				tail++; 
			}
		}
		head++;
	} 
}
int main(){
	int a,b;
	cin>>n>>e;
	for(int i=1;i<=e;i++){
		cin>>a>>b;
		g[a][b]=1; //有向图 
	}
	cin>>temp; //起点
	bfs(temp); 
	return 0;
} 
```

