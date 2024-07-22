![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/055786187c524c29b3ed8f09a0b0bcb5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <cstring> 
using namespace std;
int main(){
	char a[101];
	int front=0,rear=0;
	cin>>a;
	rear=strlen(a);
	while(front<rear){
		cout<<a[front++];
		a[rear++]=a[front++];
	}
	return 0;
}

```

