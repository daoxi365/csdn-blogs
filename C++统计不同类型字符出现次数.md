![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720140527528.png)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[1001];
	int b=0,s=0,n=0,o=0;
	cin.getline(a,1001);
	
	for(int i=0;i<strlen(a);i++){
		if(a[i]>='a'&&a[i]<='z') s++;
		else if(a[i]>='A'&&a[i]<='Z') b++;
		else if(a[i]>='0'&&a[i]<='9') n++;
		else o++;
	}
	cout<<b<<" "<<s<<" "<<n<<" "<<o<<endl;
	return 0;
} 
```

