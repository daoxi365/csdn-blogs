![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/202107141538166.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double s = 0,arr[10] = {28.9,32.7,45.6,78,35,86.2,27.8,43,56,65};
	int n = 0;
	for (int i = 0;i < 10;i ++) {
		cin >> n;
		arr[i] *= n; 
	}
	for (int i = 0;i < 10;i ++) {
		s += arr[i];
	}
    cout << fixed << setprecision(1) << s << endl; 

    return 0;
}
```

