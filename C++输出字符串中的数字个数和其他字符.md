【问题描述】统计用户输入的字符（长度1≤n≤100）中数字的个数和其他字符。
输入共一行，包含用户输入要检测的字符串。
输出共两行，第一行包含其他字符，第二行包含字符串中数字的个数。
【样例输入】
abcde12345
【样例输出】
abcde
5

```cpp
#include <iostream>
using namespace std;

int main(){
	char k[101];
	cin.getline(k,101);
	int i=0,x=0;
	while(k[i]!='\0'){
		if(k[i]>='0'&&k[i]<='9') x++;
		else cout<<k[i];
		i++;
	}
	cout<<endl<<x<<endl;
	return 0;
} 
```

