![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8a766800fb6246d692dad87f6a27abf5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
上面的题和下面的基本一样，直接参考这道题：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7c936f1c1cca43f3bb1d79d8879ea8d6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/320dff654b064acdb93df7055be39dd8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int main(){
	int a[10001],n,k;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	// 作比较 
	for(int i=1;i<n;i++){
		int key=a[i],j=i-1; // 记录a[i]的值和第一个元素 
		while(j>=0&&key<a[j]){
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=key;
	}
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
} 
```

