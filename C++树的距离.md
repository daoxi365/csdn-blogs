![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/557b41a0896d4f90a634a1d4fc99b3a2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/dc57cf49d0f54d808d539f75bc27fa23.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
又是一道递推算法题：
```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int m,a[21]={0};
	cin>>m;
	a[2]=2;
	for(int i=2;i<=m;i++) a[i]=a[i-1]+i;
	cout<<a[m]<<endl;
	return 0;
}
```

