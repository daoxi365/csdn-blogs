![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/01913e182bb749668a95eae44b56e9c4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;
int add(int x){
	if(not x>=1) return 0;
	x--;
	return (x+1)+add(x);
}
int main(){
	int n;
	cin>>n;	
	cout<<add(n)<<endl;
	return 0;
} 
```

