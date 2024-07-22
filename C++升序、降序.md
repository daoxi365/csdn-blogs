升序：

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int a[100],n;
	cin >> n;
	for (int i = 0;i < n;i ++){
		cin >> a[i];
	}
	sort(a + 0,a + n);
	for (int i = 0;i < n;i ++){
		cout << a[i] << " ";
	}
	return 0;
}
 ```
降序：

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int a[100],n;
	cin >> n;
	for (int i = 0;i < n;i ++){
		cin >> a[i];
	}
	sort(a + 0,a + n);
	for (int i = n - 1;i >= 0;i --){
		cout << a[i] << " ";
	}
	return 0;
} 
```

