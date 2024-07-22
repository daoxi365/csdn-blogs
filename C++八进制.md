![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2200d2b0ad224359b6a9800dc9698ff0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;
const int n=100;
int stack[n+1],top=0;
int main(){
	int n;
	cin>>n;
	while(n){
		stack[++top]=n%8;
		n/=8;
	}
	while(top!=0){
		cout<<stack[top--];
	}
	cout<<endl;
	return 0;
}
```


