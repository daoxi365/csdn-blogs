![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/804f44d71c494702bfe86e82ba3cb0f8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

<hr>


![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/efca99660a334ec8850240a4b8667f18.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/76c92c33e08b4c2b829b9d33e8e400d8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7b73cb9159fb4c06a465d931e1b4b4de.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e2efc3a25d05402da32533dcec67f16c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2267a3b69c6a489696468b52cca8f354.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
测试数据：

8 12
1 2
1 3
1 4
1 6
2 6
3 4
3 5
4 7
5 7
5 8
6 8

```

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
struct node{
	int city,pre;
}que[1001];
int map[11][11],book[11],head=1,tail=1,n,m;
void print(int n){
	if(n==1) cout<<que[n].city;
	else {
		print(que[n].pre);
		cout<<"->"<<que[n].city;
	}
}
void bfs(){
	que[tail].city=1;
	que[tail].pre=0;
	tail++;
	book[1]=1;
	while(head<tail){
		for(int i=1;i<=n;i++){
			if(map[que[head].city][i]==1&&book[i]==0){
				que[tail].city=i;
				que[tail].pre=head;
				tail++;
				book[i]=1;
			}
			if(que[tail-1].city==n){
				print(tail-1);
				return;
			}
		}
		head++;
	}
}
int main(){
	cin>>n>>m;
	int a,b;
	for(int i=1;i<m;i++){
		cin>>a>>b;
		map[a][b]=1;
		map[b][a]=1;
	}
	bfs();
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f09bbbd424e34034b0b1fc72c809dd36.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

