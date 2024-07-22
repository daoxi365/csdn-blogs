![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e5b96415c6ee46859362c65cdf2027c3.png)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;

int eat(int n){
	if(n!=10) return 2*(eat(n+1)+1);
	else return 1;
} 
int main(){
	cout<<eat(1)<<endl;
	return 0;
}
```

