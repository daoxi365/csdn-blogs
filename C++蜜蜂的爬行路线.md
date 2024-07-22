![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e6e54db464cc4ca5925581c8bb2519df.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int start,end,a[1001]={0,1,2};
	cin>>start>>end;
	for(int i=3;i<=end-start;i++){
		a[i]=a[i-1]+a[i-2];
	}
	cout<<a[end-start]<<endl;
	return 0;
}
```

