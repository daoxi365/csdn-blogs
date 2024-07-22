![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5ac3dad4be234bb38cee7f39aa15ac76.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6f0cd7c75ef34a1e8af1ff28157921f2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;
struct p{
	char id[15];
	int age;
} a[110],b[110],c;
void qsort(int left,int right){
	if(left>=right) return;
	int i=left,j=right;
	p x=a[left];
	while(i<j){
		while(i<j&&a[j].age<x.age) j--;
		a[i]=a[j];
		while(i<j&&a[i].age>x.age) i++;
	}
	a[i]=x;
	qsort(left,i-1);
	qsort(i+1,right);
	return;
}
int main(){
	int m;
	int f=0,s=0;
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>c.id>>c.age;
		if(c.age>=60) a[f++]=c;
		else b[s++]=c;
	}
	qsort(0,f-1);
	for(int i=0;i<f;i++){
		cout<<a[i].id<<endl;
	}
	for(int i=0;i<s;i++){
		cout<<b[i].id<<endl;
	}
	return 0; 
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/30dbf3b2abdd4c5fa0c1752220206b36.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

