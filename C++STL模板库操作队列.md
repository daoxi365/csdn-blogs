```cpp
//Author:PanDaoxi
#include <iostream>
#include <queue> 
using namespace std;
int main(){
	// 创建队列q
	queue<int> q;
	int sum=0;
	for(int i=1;i<=10;i++){
		q.push(i); // 入队 
	} 
	cout<<"队头元素："<<q.front()<<endl;
	cout<<"队尾元素："<<q.back()<<endl;
	cout<<"队列中元素的个数："<<q.size()<<endl;
	cout<<"队列中元素：";
	while(!q.empty()){
		sum+=q.front();
		cout<<q.front()<<" ";
		q.pop();
	} 
	cout<<endl<<"元素之和："<<sum<<endl;

	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/eef929ffa8c64809b5f9ab16a37a81d3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

