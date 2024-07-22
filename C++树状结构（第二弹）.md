![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ca87f8172bf84feeba257ee978f1588e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/070d12c61d574e2a87a359b8ef403369.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2f6ab6470a3a42f98b3d86f082dca930.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/162aeb7b2b5d48039f5edfda559c05f8.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d9cc76105bf14b838c4788873010b8c6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/33b277a39e14485bb4585d253cb39133.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0b9a705d8a404fa3b7126002684b4b3a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/75683de76f1a47af8c4c584cde8e44a6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/59eb899a80f748c3963600d07bd7cd75.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/be6b3f79cfc644caaa4aa7c1ec8efc8d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a3c0fc92849949a7a901cc78869a78fd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/401266bcb39f4ee6a2ed754e6c2702e6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e89dc0ca1974ef3aa8ca7769b9d8baa.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
#include <iostream> 
#include <algorithm>
#include <cstring>
using namespace std;
struct use{
	int st,en; //两端连线点 
}b[10001];
int son[10001],ans[10001],minn,n;
//son 子树个数
int next[10001],point[10001],t;
//next 上条边 point 最后的边 t 记录边的编号
bool f[10001]; //标记当前边是否已经使用 
void add(int x,int y){ //建立联系 
	t++; //边编号
	next[t]=point[x]; //把当前变放入next
	point[x]=t; // 当前边
	b[t].st=x; //开始
	b[t].en=y; //结束
	return; 
}
void dfs(int x){ //x=从6个节点开始搜索位置
	int i,u,balance=0; //i=边的编号 u=边的子节点端 balance=最大子树节点数
	son[x]=0; //子节点个数 
	f[x]=false; //跳过的点 
	//搜索所有分支节点
	for(i=point[x];i;i=next[i]){
		u=b[i].en; //当前节点的子节点
		if(!f[u]) continue; //如果搜索过则跳过
		dfs(u); //根据新的根继续向下搜索
		son[x]+=son[u]+1; //x的子节点是u的子节点+1
		balance=max(balance,son[u]+1); //记录搜索最大子节点的个数
	} 
	balance=max(balance,n-son[x]-1); //最大子树 
	//过滤重心
	if(balance<minn){
	    minn=balance;
	    ans[0]=1; //重心数量
	    ans[1]=x; 
	}
	else if(balance==minn){
		ans[0]+=1;
		ans[ans[0]]=x;
	}
	return;	
}
int main(){
	int x,y;
	cin>>n;
	minn=100001;
	memset(f,1,sizeof(f)); //给整数数组赋值
	for(int i=1;i<n;i++){ //输入数据 并建立连接 
		cin>>x>>y;
		//调用函数连线
		add(x,y); //x连y 
		add(y,x); //y连x 
	}	
	dfs(1);
	sort(ans+1,ans+ans[0]+1);  //排序并保留重心 (ans[0])
	for(int i=1;i<=ans[0];i++){
		cout<<ans[i]<<" ";
	}
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/19aa6b0983b240be83e3552f05419e5c.gif#pic_center)


<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/95c10b9e89a04d98a5d375a4703d0f18.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d490aa811635489aa35061707b8f3df8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4e591025ef4140cb831fa472e39f7723.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi 
#include <iostream>
#include <cstring>
using namespace std;
struct node{
	int to,next; //to=端点 next=边的编号 
}edge[10001];
int cnt=0; //边的编号
int vis[10001],head[10001],dis[10001]; //vis=标记 head=新边的编号 dis=路径中节点
void add(int u,int v){
	cnt++; //边的编号
	edge[cnt].to=v;
	edge[cnt].next=head[u];
	head[u]=cnt;
	return; 
} 
void dfs(int x){
	vis[x]=1; //搜索过的当前点
	for(int i=head[x];i;i=edge[i].next){
		if(!vis[edge[i].to]){
			dis[edge[i].to]=dis[x]+1;
			dfs(edge[i].to); //递归 
		}
	}
}
int main(){
	int n;
	cin>>n;
	memset(head,-1,sizeof(head));
	memset(vis,0,sizeof(vis));
	memset(dis,0,sizeof(dis));
	//建立树、连接
	for(int i=1;i<n;i++){
		int u,v;
		cin>>u>>v;
		add(u,v);
		add(v,u);
	} 
	dfs(1); //深搜
	int pos=1; //最远端端点的位置
	for(int i=1;i<=n;i++){
		if(dis[i]>dis[pos]){
			pos=i;
		}
	} 
	memset(vis,0,sizeof(vis)); //重新覆盖、二次深搜 
	dis[pos]=1;
	dfs(pos);
	int ans=0; //路径最大值
	for(int i=1;i<=n;i++){
		if(dis[i]>ans){
			ans=dis[i];
		}
	} 
	cout<<ans<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/947eb5ce97714cdda6cf756c00b36308.gif#pic_center)

