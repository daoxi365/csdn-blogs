![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7ff1908494c143aeba41ead8852dd478.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
const int N=1010;
int stack[N],a[N],top=0,n; //栈和指针 
int main(){
	for(int i=1;i<=5;++i){
		cin>>a[i]; //输入骑士编号 
	}
	for(int i=1,cur=1;i<=5;i++){ // cur是编号 
		while(cur<=a[i]){
			stack[++top]=cur; //骑士编号入栈 
			cur+=2; //从1开始每次增加5 
		}
		if(stack[top]==a[i]) --top;
		else {
			cout<<"NO"<<endl;
			return 0;
		}	
	}
	cout<<"YES"<<endl;
	return 0;
} 
```

