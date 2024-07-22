前两天课本上才学了身份证的组成，我来搞搞事情
说实话，这个根本没什么技术含量。课间瞎搞搞罢了
输入前17位，计算最后一位。

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	char b[18],c;
	int a[18],s=0,ans;
	cin>>b;
	for(int i=0;i<18;i++){
		switch(b[i]){
			case '1':
				a[i]=1;
				break;
			case '2':
				a[i]=2;
				break;
			case '3':
				a[i]=3;
				break;
			case '4':
				a[i]=4;
				break;
			case '5':
				a[i]=5;
				break;
			case '6':
				a[i]=6;
				break;
			case '7':
				a[i]=7;
				break;
			case '8':
				a[i]=8;
				break;
			case '9':
				a[i]=9;
				break;
			case '0':
				a[i]=0;
				break;
		}
	}
	a[0]*=7,
	a[1]*=9,
	a[2]*=10,
	a[3]*=5,
	a[4]*=8,
	a[5]*=4,
	a[6]*=2,
	a[7]*=1,
	a[8]*=6,
	a[9]*=3,
	a[10]*=7,
	a[11]*=9,
	a[12]*=10,
	a[13]*=5,
	a[14]*=8,
	a[15]*=4,
	a[16]*=2;
	for(int i=0;i<17;i++){
		s+=a[i];
	}
	ans=s%11;
	switch(ans){
		case 0:
			c='1';
			break;
		case 1:
			c='0';
			break;
		case 2:
			c='X';
			break;
		case 3:
			c='9';
			break;
		case 4:
			c='8';
			break;
		case 5:
			c='7';
			break;
		case 6:
			c='6';
			break;
		case 7:
			c='5';
			break;
		case 8:
			c='4';
			break;
		case 9:
			c='3';
			break;
		case 10:
			c='2';
			break;
	}
	cout<<b<<c;
	return 0;
}
```
我直接超级switch！！
