![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/5beb3f0fc6f3d2b7661e36b8a27e206e.png)
这个题我们需要一点小技巧，请看：

```cpp
#include <iostream>
#include <cstring>
using namespace std;

bool check(char n[10001],char d){
	for(int i=0;i<strlen(n);i++){
		if(n[i]==d) return true;
	}
	return false;
}

int main(){
	char b,a[10001];
	string c="";
	cin>>a>>b;
	if(check(a,b)) c="true";
	else c="false";
	cout<<c<<endl;
	return 0;
} 
```

