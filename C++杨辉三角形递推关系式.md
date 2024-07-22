![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c47fd34713504558a46f0f096a5e7263.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;

int main(){
	int a[101][101],n;
	cin>>n;
	cout<<endl<<endl;
	for(int i=0;i<n;i++){
		for(int j=0;j<=i;j++){
			if(j==0||j==i) a[i][j]=1;
			else a[i][j]=a[i-1][j-1]+a[i-1][j];
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
} 
```
杨辉三角的递推关系式是什么？大家找一找规律。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a1f7bb6009aa4ada8c367c45416137e3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_12,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fa96907481944fb4869d3e5803d5b555.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
发现了吗？同色的框里有什么规律？
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f3d7a2fb6bc641f2b94abe396ab670fc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

