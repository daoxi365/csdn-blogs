![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e2fb4a86dff49109ab7565c497854eb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5e610db42c3041fd841fb6d143c391c8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
有很多种方法：

选择排序：
```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[501],b[501],k,x=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	// 获取到这个范围内所有奇数储存在数组b中 
	for(int i=0;i<n;i++){
		if(a[i]%2){
			b[k++]=a[i];
			x++;
		}
	}
	k=0; // 将k归零
	// 选择排序 
	for(int i=0;i<x;i++){
		k=i;  
		for(int j=i+1;j<x;j++){ 
			if(b[j]<b[k]){
				k=j; 
			}
		}
		if(k!=i){
			swap(b[i],b[k]);
		} 
	}
	for(int i=0;i<x;i++){
		cout<<b[i]<<",";
	}
	return 0;
} 
```

冒泡排序：
```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[501],b[501],k,x=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	// 获取到这个范围内所有奇数储存在数组b中 
	for(int i=0;i<n;i++){
		if(a[i]%2){
			b[k++]=a[i];
			x++;
		}
	}
	k=0; // 将k归零
	// 冒泡排序 
	for(int i=x-1;i>=1;i--){
		for(int j=0;j<i;j++){
			if(b[j]>b[j+1]){ 
				swap(b[j],b[j+1]);
			}
		}
	}
	for(int i=0;i<x;i++){
		cout<<b[i]<<",";
	}
	return 0;
} 
```

插入排序：

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[501],b[501],k,x=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	// 获取到这个范围内所有奇数储存在数组b中 
	for(int i=0;i<n;i++){
		if(a[i]%2){
			b[k++]=a[i];
			x++;
		}
	}
	k=0; // 将k归零
	// 插入排序 
	for(int i=1;i<x;i++){
		int key=b[i],j=i-1; 
		while(j>=0&&key<b[j]){
			b[j+1]=b[j];
			j--;
		}
		b[j+1]=key;
	}
	for(int i=0;i<x;i++){
		cout<<b[i]<<",";
	}
	return 0;
} 
```

