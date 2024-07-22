具体如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/64a667c042e940508e92fdc6aa31c4cd.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/26f9fc7447424037bb81cb114a15c081.png)

```cpp
// Author:PanDaoxi 
#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int n=0;
	char c[101][101]={};
	cin>>n;
	memset(c,32,sizeof(c));
	for(int i=1;i<=n;i++){
		c[1][i]='*';
		c[n][i]='*';
	} 
	for(int i=2,j=n-1;i<n;i++,j--){
		c[i][j]='*';
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<c[i][j];
		}
		cout<<endl;
	}
	return 0;
} 
```

