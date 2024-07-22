```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int mcf(int x,int y){ //最大公因数 
	int maxn,a[10001],k=0,big=(x>y?x:y);
	for(int i=1;i<=big;i++){
		if(x%i==0&&y%i==0) a[k++]=i;
	}
	maxn=a[0]; 
	for(int i=0;i<k;i++){
		if(maxn<a[i]) maxn=a[i];
	}
	return maxn;
}
bool coprime(int x,int y){ // 是否互质
	int n=mcf(x,y);
	if(n==1) return true;
	else return false;
}
int lcm(int x,int y,int z){ // 最小公倍数
	int sum=1,n=0,minn,b[10001],k=0,big=(x>y?x:y);
	if(coprime(x,y)) return x*y;
	int c=x,d=y;
	n=mcf(c,d);
	while(coprime(c,d)==false&&n!=1){
		n=mcf(c,d);
		c/=n;
		d/=n;
		b[k++]=n;
	}
	sum=c*d;
	for(int i=0;i<k;i++){
		sum*=b[i];
	}
	return sum;
}

int main(){
	int a,b;
	cin>>a>>b;
	int x=mcf(a,b);
	int y=lcm(a,b,x);
	cout<<"最大公因数："<<x<<endl<<"最小公倍数："<<y<<endl;
	return 0;
}
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e9c9f83c214148978cac0934600beda7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3fef514474e04d98b196672ceeb464f4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

