![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/82f021cd28284a0387830530dc97bef9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
//Author:PanDaoxi
#include <iostream>
#include <cstring>
using namespace std;
int main(){
	char name[101];
	cin>>name;
	//a记录 'a'的ASCII为97
	int a[101]={},minx=100001,len=strlen(name);
	for(int i=0;i<len;i++) a[name[i]-97]++;	//在a中记录使用过 
	for(int i=0;i<26;i++) if(a[i]!=0&&a[i]<minx) minx=a[i]; //纪录最小值 
	for(int i=0;i<len;i++) if(a[name[i]-97]!=minx) cout<<name[i]; //输出除了最小值以外其他的字母 
	return 0;
} 
```

