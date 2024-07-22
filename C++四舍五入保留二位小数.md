方法一：

```cpp
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
	double x;
	cin>>x;
	cout<<fixed<<setprecision(2)<<x<<endl;
	return 0;
} 
```
方法二：

```cpp
#include <cstdio>
using namespace std;

int main(){
	double x;
	scanf("%lf",&x);
	printf("%.2lf",x);
	return 0;
}
```

