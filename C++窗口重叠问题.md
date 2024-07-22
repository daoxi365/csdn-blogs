![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9cd2276dd4c34783a88fcd610888ded9.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct window{
	int left=0,right=0,top=0,bottom=0;
}w[2];
int main(){
	int l=0,r=0,t=0,b=0,n=0;
	cin>>w[0].left>>w[0].right>>w[0].top>>w[0].bottom;
	cin>>w[1].left>>w[1].right>>w[1].top>>w[1].bottom;
	l=w[0].left>w[1].left?w[0].left:w[1].left;
	r=w[0].right<w[1].right?w[0].right:w[0].right;
	t=w[0].top>w[1].top?w[0].top:w[1].top;
	b=w[0].bottom<w[1].bottom?w[0].bottom:w[1].bottom;
	n=(r-l)*(b-t);
	if(r<=l||b<=t) n=0;
	cout<<n<<endl;
	return 0;
}
```

