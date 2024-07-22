![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210712141409196.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main()
{
    int n,i = 1;
    cin >> n;
    do{
    	if (i % 2 == 1){
    		cout << i << " ";
		}
		i ++;
	} while (i <= n);
    return 0;
}
```

```cpp
#include <iostream>
using namespace std;

int main()
{
	int n,i = 1;
	cin >> n;
	
	while (i <= n){
		if (i % 2 == 1) {
			cout << i << " ";
		}
		i ++;
	}
    return 0;
}
```

