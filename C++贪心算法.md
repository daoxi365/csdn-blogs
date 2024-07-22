![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e3b86d40c1be466fa618b63be52e0bbb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/df2774fadf8d4098a71d43a6c21c207c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/067b339130a74b5ebfd6d69c4b06d66a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/695105584388406686de889fd3525c77.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9d76ddccac664ad3aee9b80d28f3afe9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fc6a84d84f354eefb110ee51f86b2888.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e55af5f691474730a296a34a840fb72c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
int w[1001];
int main(){
	int c,n; //c=袋子最大承重量 n=苹果数量
	cin>>c>>n;
	for(int i=0;i<n;i++) cin>>w[i];
	sort(w,w+n);
	int temp=0,ans=0;
	for(int i=0;i<n;i++){
		temp+=w[i];
		if(temp<=c) ans++;
		else break;
	} 
	cout<<ans<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d59f67f360114cc798c062f8bc16f431.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/15ad47468b264980a005b21db129214d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a2936df315f74b05b8e38a4851ccca85.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/088b0342f7ce43b8bad6526e8f7c19b1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
struct gudong{
	string name;
	double weight;
}; 
bool cmp(gudong a,gudong b){ //排序用的比较函数 
	return a.weight<b.weight;
} 
int main(){
	gudong w1[10001];
	int c,n;
	cin>>c>>n;
	for(int i=0;i<n;i++){
		cin>>w1[i].name>>w1[i].weight;
	}
	sort(w1+0,w1+n,cmp);
	int sum=0,count=0;
	for(int i=0;i<n;i++){
		sum+=w1[i].weight;
		if(sum<c) count++;
		else break;
	}
	for(int i=0;i<count;i++) cout<<w1[i].name<<" ";
	return 0;
}
```
（插个话，今天的百度网盘格外地块）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/123fdfb8c0c44fc3ba667347cc6fad62.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/acaf6c42d1cb4152b5d566a4f2962d30.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ca79fd578ad541888e60cfbad6a680ba.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[101],s=0; //n=堆数 a=储存苹果重量 s记录苹果总重量 
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
		s+=a[i];
	}
	//求出平均每堆的重量
	s/=n;
	int t=0; //移动次数
	for(int i=1;i<n;i++){
		if(a[i]!=s){
			t++; //需要移动一次 
			//a[i]需要(s-a[i])个苹果 
			a[i+1]=a[i+1]-s+a[i];
		}
	} 
	cout<<t<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/05a8ad0e29aa4e66a60de466b0802030.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;
int main(){
	//n=苹果数量 m=袋子最大承重 ans=袋子数量 s=每袋所装数量 
	int n,m,x,s=0,ans=0;
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		cin>>x;
		if(s+x<=m) s+=x; //可以装入
		else{
			ans++;
			s=x;
		} 
	}
	cout<<ans+1<<endl;
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/618a7c119c17411c8753e1eca8e081ed.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/678fd922270f4e6b9d9d1d068c950a5c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_13,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
struct meeting{
	int st,en;
} a[10001];
bool cmp(meeting a,meeting b){
	return a.en<b.en;
} 
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i].st>>a[i].en;
	//按结束时间排序
	sort(a+1,a+n+1,cmp);
	int sum=1;
	int last=a[1].en;
	for(int i=1;i<=n;i++){
		if(a[i].st>last){
			sum++;
			last=a[i].en; //更新 
		}
	} 
	cout<<sum<<endl;
	return 0; 
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ea3fe46cadb746bdb422d7e0877d2c04.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,m,sum=0;
	cin>>n;
	m=n;
	while(m>0){
		if(m>=20){
			m-=20;
			sum++;
		}
		else if(m>=10){
			m-=10;
			sum++;
		}
		else if(m>=5){
			m-=5;
			sum++;
		}
		else{
			sum+=m;
			m=0;
		}
	}
	cout<<sum<<endl;
	return 0;
} 
```

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int m[5]={20,10,5,1},n,count=0;
	cin>>n;
	for(int i=0;i<4;i++){
		while(n>=m[i]){
			n-=m[i];
			count++;
		}
	}
	cout<<count<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6ec11bebf3794071a4a220e01781ef16.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,m,a[21],sum=0;
	cin>>n>>m;
	for(int i=0;i<m;i++) cin>>a[i];
	for(int i=0;i<m;i++){
		while(n>=a[i]){
			n-=a[i];
			sum++;
		}
	}
	cout<<sum<<endl;
	return 0;
} 
```

