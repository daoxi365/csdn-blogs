![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/33b01c813ebb48b8bc27d526ef7d3c0e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:Pan Daoxi
#include <iostream>
using namespace std;
struct student{
	int number;
	double score;
} stu[101];
int main(){
	int n,k,a[101];
	cin>>n>>k;
	for(int i=0;i<n;i++){
		cin>>stu[i].number>>stu[i].score;
	}
	for(int i=n-1;i>=1;i--){
		for(int j=0;j<i;j++){
			if(a[j]>a[j+1]){ 
				swap(a[j],a[j+1]);
			}
		}
	}
	cout<<stu[k].number<<" "<<stu[k].score;
	return 0;
} 
```

