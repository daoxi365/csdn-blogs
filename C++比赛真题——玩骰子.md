骰（tóu）子，是中国传统民间娱乐用来投掷的博具。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/277ad12c0b5845e697a41a3ad63d8100.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/16063e8a7b314364b32552cbf3014c8a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int tong[3]={4,6,5},mei[3]={1,2,3}; 
void put(char x,int t[]){
	int u,f,r;
	switch(x){
		case 'R':
			u=7-t[2];
			f=t[1];
			r=t[0];
			break;
		case 'D':
			u=7-t[1];
			f=t[0];
			r=t[2];
			break;
		case 'L':
			u=t[2];
			f=t[1];
			r=7-t[0];
			break;
	}
	t[0]=u,t[1]=f,t[2]=r;
}
int main(){
	int n,sum1=0,sum2=0;
	cin>>n;
	int i=1;
	while(i<=n){
		int a=(2*1-1)%4,b=(2*1)%4;
		switch(i%3){
			case 1:
				while(a--) put('R',tong);
				sum1+=tong[0];
				while(b--) put('R',mei);
				sum2+=mei[0];
				break;
			case 2:
				while(a--) put('D',tong);
				sum1+=tong[0];
				while(b--) put('D',mei);
				sum2+=mei[0];
				break;
			case 0:
				while(a--) put('L',tong);
				sum1+=tong[0];
				while(b--) put('L',mei);
				sum2+=mei[0]; 
				break;
		}
		i++; 
	}
	char last=sum1>sum2?'A':(sum1==sum2)?'P':'B';
	cout<<last<<endl;
	return 0;
} 
```

