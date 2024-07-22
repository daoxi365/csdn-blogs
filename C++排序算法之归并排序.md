![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e1b9c71f36d4029b6d3b16d7ef678e7.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/071c52c9e8004535b39956f3e1e51f82.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1d851b5e238d4ad99f164cdf375d3e0b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cfa0db5953074af981a9229682644362.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int maxn=101;
int a[maxn],r[maxn];
// 归并排序
void merge(int left,int right){
	{
		// 1.分解
		if(left==right) return; // 分解完成
		int mid=(left+right)/2;
		merge(left,mid);
		merge(mid+1,right);
		// 2.归并
		int i=left,j=mid+1,k=left;
		while(i<=mid&&j<=right){ // 两侧都有数值 
			if(a[i]<a[j]) r[k++]=a[i++];
			else r[k++]=a[j++];
		}
		while(i<=mid){   // 右侧无元素 
			r[k++]=a[i++]; 
		}
		while(j<=right){ // 左侧无元素 
			r[k++]=a[j++];
		}
	}
	// a数组更新为归并好的数组 
	for(int i=left;i<=right;i++){
		a[i]=r[i];
	}
	return;
} 
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	// 归并排序
	merge(1,n);
	for(int i=1;i<=n;i++){
		cout<<a[i]<<" ";
	} 
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/ebf4d1f4aeb349fd92278b3041a23593.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e4bf53751e84187a733fa6274058995.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

