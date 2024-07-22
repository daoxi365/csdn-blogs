![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/dfaa4f42154e47909db690ee666d99aa.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,m;
	cin>>n>>m;
	int total=m*2;
	for(int i=m+1;i<=n;i++) total+=i;
	cout<<total<<endl;
	return 0;
} 
```

