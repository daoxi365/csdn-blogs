![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8cc67b8f82134d89a94e68f60cd7e685.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[100]={0},m=2;
	cin>>n;
	a[1]=1;
	for(int i=2;i<=n;i++){
		a[i]=a[i-1]+m;
		m*=2;
	}
	cout<<a[n]<<endl;
	return 0;
} 
```

