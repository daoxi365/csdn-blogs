```cpp
#include <iostream>
using namespace std;

int main(){
	int n,num,first = 0,second = 0;
	cin >> n;
	for (int i = 1;i <= n;i ++){
		cin >> num;
		if (first < num){
			second = first;
			first = num;
		}
		else if (second < num){
			second = num;
		}
		
	}
	cout << second << endl;
	return 0;
}
```

