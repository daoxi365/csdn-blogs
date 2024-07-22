![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d03fffd0858e481a93cf025045c194cd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/465d61a8aedc42a3b5cb286eaf613850.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int g[1001][1001];
int main(){
	int n,e,a,b,c; //c权值 
	cin>>n>>e; //顶点和边数
	//接收边的状态
	for(int i=1;i<=e;i++){
		cin>>a>>b>>c;
		g[a][b]=c;
		g[b][a]=c;
	} 
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<g[i][j];
		}
		cout<<endl; 
	}
	return 0;
} 
```

