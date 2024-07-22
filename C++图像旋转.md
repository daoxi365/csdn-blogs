![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/a8101d7309fc3511b2b4ca4d3f3c576f.png)

```cpp
#include <iostream>
using namespace std;

int main(){
	int m,n,a[101][101];
	cin>>m>>n;
	for(int i=1;i<=m;i++) for(int j=1;j<=n;j++) cin>>a[i][j];
	for(int j=1;j<=n;j++){
        for(int i=m;i>=1;i--) cout<<a[i][j]<<" ";
        cout<<endl;
    }
	return 0;
}
```

