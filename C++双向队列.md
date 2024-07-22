![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a41462c1454d46eaa907431669f9b7cd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/91ee211dc37c4736bc0e96b66d8b2e87.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/789f8d5b518647239d2228426c5995ae.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <deque>
using namespace std;
int main(){
	// 创建双向队列
	deque<int>dq;
	int sum=0;
	cout<<"最大容量："<<dq.max_size()<<endl;
	for(int i=1;i<=5;i++){
		dq.push_front(i); // 在对首插入元素 
	}
	cout<<"元素个数："<<dq.size()<<endl;
	for(int i=6;i<=10;i++){
		dq.push_back(i); // 向队尾插入元素 
	} 
	cout<<"元素个数："<<dq.size()<<endl;
	cout<<"队首至队尾的元素依次为：";
	while(!dq.empty()){
		sum+=dq.front();
		cout<<dq.front()<<" ";
		dq.pop_front();
	} 
	cout<<endl<<"元素和为："<<sum<<endl;
	cout<<"容纳的最大元素个数为："<<dq.max_size()<<endl;
	return 0;
} 
```

