![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9630588c30eb41f89285f028a08e0a29.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
（这是一道真题）

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	int n,a,b,c;
	cin>>n;
	while(n!=0){
		a=n%10; //获取末位
		b=c*10+a;
		c=b; 
		n/=10; //递除 
	} 
	cout<<c;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/278e606011a3471a8c05188e35f991c3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

