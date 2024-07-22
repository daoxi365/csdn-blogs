![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/873921ae2b384fbe94f39858835d243a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
很好使的。

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int x,y,big,n=1;
int fractionReduction(int a,int b){
	x=a,y=b,big=(a>b?a:b);
	for(int i=big;i>=1;i--){
		if(x%i==0&&y%i==0){
			x/=i; //分子（前项）
			y/=i; //分母（后项）
			n*=i; //公约数
		}
	} 
}
int main(){
	int a,b;
	cin>>a>>b;
	fractionReduction(a,b);
	cout<<x<<" "<<y<<endl<<"公约数为"<<n<<endl; 
	return 0;
} 
```

