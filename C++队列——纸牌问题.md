![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/981fd19c967d47f19c6dff06714be969.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
// 创建队列 
const int MaxSize=101;
int q[MaxSize],front=0,rear=0;
void push(int value){ // 入队操作 
	if(rear<MaxSize) q[rear++]=value; 
} 
int pop(){ // 出队操作 
	if(front!=rear) return q[front++];
}
int main(){
	int n,temp;
	cin>>n;	
	for(int i=1;i<=n;i++){
		push(i);
	}
	for(int i=1;i<=n;i++){
		cout<<pop()<<" ";
		push(pop());
	}
	return 0;
} 
```
或是这样：
```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[10000],front=0,rear=0;
	cin>>n;
	for(int i=0;i<n;i++){
		a[i]=i+1;
	}
	rear=n;
	while(front<rear){
		cout<<a[front++]<<" ";
		a[rear++]=a[front++];
	} 
	return 0;
}
```

