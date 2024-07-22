![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/537f8ef894df4c57a349aabe9952b363.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int a[11],book[11],n;
void dfs(int step){ //深搜函数 
	if(step==n+1){
		for(int i=1;i<=n;i++){ //注意从1~n
			cout<<a[i];
		}
		cout<<endl;
		return;
	}
	for(int i=1;i<=n;i++){
		if(book[i]==0){
			a[step]=i;
			book[i]=1; //使用过了 
			dfs(step+1); 
			book[i]=0; //回溯 
		}
	}
	return; 
}
int main(){
	cin>>n;
	dfs(1);
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/112bae4d4d504d3ca9ddad1cf1906be4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

