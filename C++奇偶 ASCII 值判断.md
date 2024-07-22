```cpp
1. 奇偶 ASCII 值判断（ascii.cpp ） 
【问题描述】
任意输入一个字符，判断其 ASCII 是否是奇数，若是，输出 YES，否则输出
NO。
【输入文件】 文件名： ascii.in 
一行，包括一个字符。
【输出文件】文件名： ascii.out 
一行，判断结果。
【样例输入 1】
A 
【样例输出 1】
YES 
【样例输入 2】
B 
【样例输出 2】
NO
```
这是我翻到的一道题，太简单了，顺便解了一下。
```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	char text;
	cin>>text;
	int number=int(text);
	if(number%2==0) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
} 
```

