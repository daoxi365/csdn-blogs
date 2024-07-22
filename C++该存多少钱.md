![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/af41534d494b4d0d85a0d246ca1e210f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	double a[51]={0.0};
	int n;
	cin>>n;
	for(int i=n;i>0;i--) a[i-1]=(a[i]+1000)/(1+0.0031*12);
	cout<<a[0]<<endl;
	return 0;
} 
```

