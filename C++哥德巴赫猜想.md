![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/7a04c8b1d5e6f09386ae573e65404c73.png)

```cpp
#include <iostream>
using namespace std;

bool prime(int x){
	for(int i=2;i*i<=x;i++) if(x%i==0) return 0;
	return 1;
}
int main(){
	int m,n;
	cin>>m>>n;
	for(int i=m;i<=n;i++){
		if(i%2==0){
			for(int j=2;j<i;j++){
				if(prime(j)&&prime(i-j)){
					cout<<i<<"="<<j<<"+"<<i-j<<endl;
					break;
				}
			}
		}
	}
	return 0;
}
```

