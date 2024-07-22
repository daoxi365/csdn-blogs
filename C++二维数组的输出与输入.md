```cpp
#include <iostream>
using namespace std;

int main(){
	int a[3][4]; // 定义一个3 * 4的整数类型二维数组
	// 输入
	for (int i = 0;i < 3;i ++){
		for (int j = 0;j < 4;j ++) cin >> a[i][j];
	}

	// 输出
	for (int i = 0;i < 3;i ++){
		for (int j = 0;j < 4;j ++) cout << a[i][j] << " ";
	}
	return 0;
} 
```

