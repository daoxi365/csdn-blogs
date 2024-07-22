![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720162700189.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
以下两种方法都可以，推荐第一种：

```cpp
#include <iostream>
using namespace std;

int prime(int x){
	for(int i=2;i*i<=x;i++) if(x%i==0) return 0;
	return 1;
}
int main(){
	int n,m;
	cin>>n>>m;
	for(int i=n;i<=m;i++) if(prime(i)) cout<<i<<" ";
	return 0;
} 
```
（可省略为

```cpp
#include <iostream>
using namespace std;int prime(int x){for(int i=2;i*i<=x;i++) if(x%i==0) return 0;return 1;}int main(){int n,m;cin>>n>>m;for(int i=n;i<=m;i++) if(prime(i)) cout<<i<<" ";return 0;}
```

）
```cpp
#include <iostream>
using namespace std;

int prime(int x){
	if(x<2) return 0;
	for(int i=2;i<x;i++) if(x%i==0) return 0;
	return 1;
}  
int main(){
	int n,m;
	cin>>n>>m;
	for(int i=0;i<=m;i++)if(prime(i)) cout<<i<<" ";
	return 0;
} 
```
可省略为（

```cpp
#include <iostream>
using namespace std;int prime(int x){if(x<2) return 0;for(int i=2;i<x;i++) if(x%i==0) return 0;return 1;}  int main(){int n,m;cin>>n>>m;for(int i=0;i<=m;i++)if(prime(i)) cout<<i<<" ";return 0;} 
```

）
