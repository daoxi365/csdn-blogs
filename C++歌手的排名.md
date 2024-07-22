![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7a7ddebec9ca4680b6ad702425e0bd08.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,b,a[1001]={};
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>b;
		a[b]++;
	}
	for(int i=1;i<=10;i++){
		cout<<i<<" ";
	}
	cout<<endl;
	for(int i=1;i<=10;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}
 
```
（简简单单，有手就行）
