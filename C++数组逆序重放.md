![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/070ecd4f51bf40e7b0e912720f9d5a23.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
忒简单了！
```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	int a[101],n;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	for(int i=n-1;i>=0;i--){
		cout<<a[i]<<" ";
	}
	return 0;
} 
```

