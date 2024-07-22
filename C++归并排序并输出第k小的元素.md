![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e9807b0865fd414b9f0283e933eb3067.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int maxn=101;
int a[maxn],r[maxn];
void merge(int left,int right){
	{
		if(left==right) return;
		int mid=(left+right)/2;
		merge(left,mid);
		merge(mid+1,right);
		int i=left,j=mid+1,k=left;
		while(i<=mid&&j<=right){ 
			if(a[i]<a[j]) r[k++]=a[i++];
			else r[k++]=a[j++];
		}
		while(i<=mid){
			r[k++]=a[i++]; 
		}
		while(j<=right){ 
			r[k++]=a[j++];
		}
	}
	for(int i=left;i<=right;i++){
		a[i]=r[i];
	}
	return;
} 
int main(){
	int n,k;
	cin>>n>>k;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	merge(1,n);
	cout<<a[k]<<" ";
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6c64b7fe44a14f38a8cb6482fa8b14a8.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)


