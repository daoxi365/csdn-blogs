![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/470090d91aba443e80a44ecb9c9488bb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
这题简单的要命，别看那么长，原理简单得很！
```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		if(i%6) cout<<i<<" ";
		else cout<<i<<endl;
	}
	return 0;
} 
```

