![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1cbef34d4d7e44919b8ccad9b5d22681.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int N=1000000;
int a,n,q[N];
void blash(int a,int n){
	q[1]=a;
	int rear=1,front1=1,front2=1;
	while(rear<=n){
		long long x=2*q[front1]+1;
		long long y=3*q[front2]+1;
		if(x<y){
			q[++rear]=x;
			front1++;
		}
		else{
			if(x>y){
				q[++rear]=y;
				front2++;
			}
			else{
				q[++rear]=x;
				front1++;
				front2++;
			}
		}
	}
	cout<<q[n]<<endl;
} 
int main(){
	while(cin>>a>>n){
		blash(a,n);
	}
	return 0;
} 
```

