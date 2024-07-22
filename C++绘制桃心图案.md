我制作成了老师的教师节礼物，比较简单：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	for(double y=1.5;y>-1.5;y-=0.1){
		for(double x=-1.5;x<1.5;x+=0.05){
			double a=x*x+y*y-1;
			char b=(a*a*a-x*x*y*y*y<=0.0?'*':'\0');
			cout<<b;
		}
		cout<<endl;
	}
	
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/43ba3fe1f19a40f7aa956d5f4acfe3b5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

