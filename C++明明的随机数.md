![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/418e8bf6d7d54abb95d4c6b1e8ddcea9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
建议使用桶排序。

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int main(){
	int n,k,a[10001]={};
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>k;
		a[k]++;
	}
	for(int i=0;i<10000;i++){
		if(a[i]!=0) cout<<i<<" "; 
	}
	return 0;
} 
```

