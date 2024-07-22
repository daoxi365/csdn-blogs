> 输入n，输出1~n（包含1和n）之间所有的回文数，并统计回文数的个数。个数之前要加星号。 
> 输入： 100 
> 输出：（下面是需要换行的）
>  1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99
> *18

这道题我挖掘了两种做法，一种好理解但是运行内存和时间可能要差点；另一种稍微费点劲，但是可以放到比赛里用。

方法一：

```cpp
// Author:PanDaoxi 
#include <iostream>
using namespace std;
bool hw(int n){
	int a[11],b[11],m=n,i=0;
	while(m){
		a[i++]=m%10;  // 获取到每一位的数字，储存在数组
		m/=10;  
	}
	for(int j=0;j<i;j++){ // 数组b将数组a的元素倒置
		b[j]=a[i-j-1];
	}
	for(int k=0;k<i;k++){
		if(a[k]!=b[k]) return false; // 如果有一位上的数字不同，就不是回文数
	}
	return true;
}
int main(){
	int n,s=0;
	cin>>n;
	for(int i=1;i<=n;i++){
		if(hw(i)){
			s++;
			cout<<i<<endl;
		}
	}
	cout<<"*"<<s;
	return 0;
}

```
第二种：

```cpp
// Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	int n,s=0,t,k=10,m;
	cin>>n;
	for(int i=1;i<=n;i++){
		t=i,m=0;
		while(t!=0){
			m=m*k+t%10;
			t/=10;  // 重新组合
		}
		if(m==i){ // 判断组合前后的数是否一样
			cout<<m<<endl;
			s++;
		}
	}
	cout<<"*"<<s;
	return 0;
}

```

