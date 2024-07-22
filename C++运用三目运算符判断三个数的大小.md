```cpp
#include <iostream>
using namespace std;

int main(){
	int a,b,c,d;
	cin >> a >> b >> c;

	d = (a > b ? a : b) > c ? (a > b ? a : b) : c;
	cout << d << endl; 
	return 0;
}
```

