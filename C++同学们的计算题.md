![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/df9f9f4165444ccabb0f204a52ed8645.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c9c7ecc7aed44cf9a2ad0861b1d86525.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,f[101]={};
	cin>>n;
	f[n]=n; //第n名同学做了n道题
	while(n>=0){
		f[n-1]=(f[n]+n-1)*2;
		n--;
	} 
	cout<<f[1]<<endl;
	return 0;
}
```

