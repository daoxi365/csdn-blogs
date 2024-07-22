![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/87a8a7367d4e4f3484cc70c4e05b7464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int calc(int n,int k){
	if(k==0||n<k) return 0;
	if(k==1||k==n) return 1;
	return calc(n-1,k-1)+calc(n-1,k)*k;
}
int main(){
	int n,k;
	cin>>n>>k;
	cout<<calc(n,k)<<endl;
	return 0;
} 
```

