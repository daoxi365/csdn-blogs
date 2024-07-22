![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/90213be82adb4e5cbfb1f2fc9c62211d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
上次文章中的位置：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8408cc1517e24882a50103355dcb4e1e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
原来的代码：

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
const int N=101;
int main(){
	int n,a[N];
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	for(int i=n-1;i>=1;i--){
		for(int j=0;j<i;j++){
			if(a[j]>a[j+1]){ // 如果大，就放到后面去，和小的交换位置 
				swap(a[j],a[j+1]);
			}
		}
	}
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
} 
```
优化后代码：

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
const int N=101;
int main(){
	int n,a[N];
	bool flag; // 优化：判断交换的开关 
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	for(int i=n-1;i>=1;i--){
		flag=true; // 判断是否交换 
		for(int j=0;j<i;j++){
			if(a[j]>a[j+1]){ 
				swap(a[j],a[j+1]);
			}
			flag=false; // 已经交换 
		}
		if(flag){
			break;
		} 
	}
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7f49bee2007e4ed8a7b404f59206d520.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

