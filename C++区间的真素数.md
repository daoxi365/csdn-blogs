![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/6886c362db52a1f682ad889cf27b0157.png)

```cpp
#include <iostream>
using namespace std;

int prime(int x){
	for(int i=2;i*i<=x;i++) if(x%i==0) return 0;
	return 1;
}
int back(int x){
	int sum=0,n;
	while(x>0){
		n=x%10;
		sum*=10;
		sum+=n;
		x/=10;
	}
	return sum;
}
int main(){
	int m,n,k=0,a[10001];
	cin>>m>>n;
	for(int i=m;i<=n;i++) if(prime(i)) if(prime(back(i))) a[k++]=i;
	for(int i=0;i<k;i++) cout<<a[i]<<","; 
	return 0;
} 
```

