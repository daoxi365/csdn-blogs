![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/70ecd967ef3744058de00111d220dcbf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int N=500001; 
int n,a[N];
int find(int x){
	for(int i=1;i<=n;i++){
		if(a[i]==x) return i;
	}
	return 0;
} 
void left(int x,int y){
	int t=a[x-1];
	for(int i=x;i<=y;i++){
		a[i-1]=a[i];
	}
	a[y]=t;
}
void right(int x,int y){
	int t=a[x];
	for(int i=x;i>=y;i--){
		a[i+1]=a[i];
	}
	a[y]=t;
}
int main(){
	int m,x,y,p,q;
	char type;
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		a[i]=i;
	}
	for(int i=1;i<=m;i++){
		cin>>type>>x>>y;
		p=find(x);
		q=find(y);
		if(type=='A'){
			if(q>p) left(p+1,q-1);
			else right(p-1,q);
		}
		else{
			if(q>p) left(p+1,q);
			else right(p-1,q+1);
		}
	}
	for(int i=1;i<=n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
} 
```

