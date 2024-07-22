![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210714155102368.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main() {
    int i,n,k,sum,a[1001];
    cin >> n;
    if (n == 1) {
        cout << 1 << endl << 1;
    }
    if (n == 2) {
        cout << 2 << endl << 3;
    }
    if (n>=3) {
        a[1] = 1;
        a[2] = 2;
        sum = 3;
        for(i = 3; i <= n; i ++) {
            a[i] = (a[i - 1] + a[i - 2]) * 3;
            sum += a[i];
        }
    }
    
    cout << a[n] << endl;
	cout << sum << endl; 
    return 0;
}
```

