![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/cd892ca2b55d4cbe8568dc209e7a5f75.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int a[10001];
int output(int n){
	for(int i=1;i<=n;i++){
		if(i!=1) cout<<"+";
		cout<<a[i];
	}
	cout<<endl;
}
int calc(int n,int ans){
	for(int i=1;i<=n/2;i++){
		if(i>=a[ans-1]){
			a[ans]=i;
			a[ans+1]=n-i;
			output(ans+1);
			calc(n-i,ans+1);
		}
	}
}
int main(){
	int n;
	cin>>n;
	a[0]=0;
	calc(n,1);
}
```

