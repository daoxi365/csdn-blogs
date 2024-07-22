①以空格分割输入内容：

```cpp
#include <iostream>
using namespace std;

int main(){
	int x,y;
	cin>>x>>y;
	cout<<"你刚才输入了："<<x<<" "<<y<<endl;
	return 0;
}
```
②带空格输入（即将空格也理解为一个字符）：

```cpp
#include <iostream>
using namespace std;

int main(){
	char a[10];
	cin.getline(a,10);
	cout<<"你刚才输入了：";
	for (int i=0;i<10;i++){
		cout<<a[i];
	}
	return 0;
}
```

