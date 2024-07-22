```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int a[10001]={},x,y;
int main(){
	int n,m,small=1,big=1;
	cin>>n>>m;
	for(int i=0;i<n;i++){
		cin>>x;
		a[x]++;
	}
	for(int i=0;i<m;i++){
		cin>>y;
		a[y]++;
	} 
	for(int i=0;i<10001;i++){
		if(a[i]>=2) big*=i; 
	}
	small=big; 
	for(int i=0;i<10001;i++){
		if(a[i]==1){
			small*=i;
		}
		if(a[i]>=3){
			small*=((a[i]-1)*i);
		}
	}
	cout<<big<<" "<<small<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/427cafff571c4d3d943544c5e7ee69c8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

已知
10=2* 5
20=2* 2* 5
那么
(10,20)=2* 5=10
[10,20]=2* 5* 2=20

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/58eae41ff0ef4df1ac5572c77df92657.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

