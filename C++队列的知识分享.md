![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9f53d63a9f8b45458078b968fab05703.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b048a4160b1a4fd19c5f0323de1668ac.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/09f10ae07c0b4c53b9425ab0a20de27e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int MaxSize=100; // 最大值常量 
int q[MaxSize],front=0,rear=0; // 创建队列和两个指针（front=队首，rear=队尾）
// 1.入队函数 
void push(int value){
	// 如果队不满则添加值 
	if(rear<MaxSize) q[rear++]=value; 
} 
// 2.出队函数 
int pop(){
	// 如果队首不为队尾（即不为空），则返回出队元素 
	if(front!=rear) return q[front++];
}
int main(){
	// 输入并入队 
	cout<<"请输入五个数：";
	for(int i=0;i<5;i++){
		int n;
		cin>>n;
		push(n);
	}	
	// 输出队中元素
	cout<<endl<<"队中元素：";
	for(int i=front;i<rear;i++){
		cout<<q[i]<<" ";
	} 
	// 出队
	cout<<endl<<"出队元素："<<pop()<<endl;
	cout<<"出队后队中元素：";
	for(int i=front;i<rear;i++){
		cout<<q[i]<<" ";
	}
	cout<<endl;
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/253352550abd4182bc5a750b316cf5e3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

