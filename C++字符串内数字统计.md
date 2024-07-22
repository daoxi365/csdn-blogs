

> 【问题描述】 输入一串内容（长度不超过100），统计出数字字符的个数，并输出其他字符。 输入：包含空格、字母和数字的一串内容。
> 输出：两行，第一行是删掉数字之后的字符串（保留空格），第二行是数字字符的个 数。 
> 【样例输入】  
> Ab c12 fds 34
>  【样例输出】 
> Ab c fds  4

```cpp
//Author:PanDaoxi 
#include <iostream>
#include <cstring> 
using namespace std;
int main(){
	char a[101],b[101];
	cin.getline(a,101);
	int len=strlen(a),sum=0,j=0;
	for(int i=0;i<len;i++){
		if(a[i]>='0'&&a[i]<='9') sum++;
		else b[j++]=a[i];
	}
	for(int i=0;i<j;i++){
		cout<<b[i];
	}
	cout<<endl<<sum;
	return 0;
} 
```

