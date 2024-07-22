[今天我们在数学课上学习了用天平找次品。](http://www.kebenku.com/jiaocai/shuxue/jijiao/6s/79937.html)
（以下几张图片来自课本库网）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/61f31690701f48e1838240cace9a4a43.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/540f2ffe0d66454f99011f27ed67bdab.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
哈哈，根据道理我又能写程序了。

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int x,y,z; 
int find(int n){
	if(x==2||y==2){
		cout<<1<<" "<<1<<endl;
		return 0;
	}
	if(x==1&&y==1) return 0;
	z=n%3,x=n/3,y=n/3;
	y=x; 
	if(z==2){
		x++;
	}
	else if(z==1) y++;
	else x=y;
	cout<<x<<" "<<x<<" "<<y<<endl;
	find(x>y?x:y);
}
int main(){
	int n;
	cin>>n;
	if(n==1){
		cout<<-1<<endl;
		return 0;
	}
	find(n);
	return 0;
} 
```
这个程序可以输出具体的称重过程：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/35771eca648549c6a4db2f8069babb29.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
也可以根据范围，求出需要的次数，在这里不写了。
例如有100个零件，100在3^4^~3^5^之间，则需要5次即可。
