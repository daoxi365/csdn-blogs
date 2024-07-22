![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e7101ce6c45d44718c5cfa9d70436f54.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct node{
	int left,right;
	char value;
}data[101];
int root=0,cnt=0;
char ch;
int buildTree(int bt){
	cin>>ch;
	if(ch=='#'){
		bt=0;
		return bt;
	}
	else{
		bt=++cnt;
		data[bt].value=ch;
		data[bt].left=data[bt].right=0;
		data[bt].left=buildTree(bt);
		data[bt].right=buildTree(bt);
	}
	return bt;
}
int func(int bt){
	if(bt){
		if(data[bt].left==0&&data[bt].right==0){
			return 1;
		}
		else {
			return func(data[bt].left)+func(data[bt].right);
		}
	}
	else return 0;
}
int main(){
	root=0;
	cnt=0;
	root=buildTree(0);
	cout<<func(root)<<endl;
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/df6dcd73f30a43dc9e2db5654dfc61cb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

