![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/257171e6c8b64157b9c85d7d1998a0a1.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int n;
long long a,b,res[50000],cnt;
// 判断是否为素数 
bool prime(int x){
	for(int i=2;i*i<=x;i++) if(x%i==0) return false;
	return true;
}
// 求10的x次方 
long long mypow(int x){
	long long ans=1;
	for(int i=1;i<=x;i++){
		ans*=10;
	}
	return ans;
}
// 回文数
long long text(long long x){
	long long ans=x;
	x/=10;
	while(x>0){
		ans=ans*10+x%10;
		x/=10; 
	}
	return ans;
}
int main(){
	cin>>n;
	// 简单的直接输出
	if(n==1) cout<<4<<endl<<"2 3 5 7"<<endl;
	else if(n==2) cout<<1<<endl<<11<<endl;
	else if(n%2==0)  cout<<0<<endl;
	else{
		// 不含有规律的进行计算
		cnt=0;
		n=(n+1)/2;
		a=mypow(n-1);
		b=mypow(n);
		for(long long i=a;i<b;i++){
			long long t=text(i);
			if(prime(t)){
				res[cnt++]=t;
			}
		}
		cout<<cnt<<endl;
		for(int i=0;i<cnt;i++){
			cout<<res[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e676203cd414ba58b7b146e5961928e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

