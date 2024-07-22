写得着急，做得简陋，敬请谅解。
注：输入内容中必须有`.`。

```cpp
// Author:PanDaoxi
#include <iostream>
#include <cmath>
using namespace std;
int zdgys(int a,int b){
	for(int i=a>b?a:b;i>=1;i--){
		if(a%i==0&&b%i==0) return i;
	}
}
int main(){
	string x;
	cin>>x;
	int len=x.length(),y,z,
	zs=0,xs=0;
	for(int i=0;i<len;i++){
		if(x[i]=='.'){
			z=i-1;
			y=i+1;
			break;
		}
	}
	// 实现整、小分离
	// 整数 x[0~z]  小数 x[y~(len-1)] 
	for(int i=0;i<=z;i++){
		zs+=pow(10,z-i)*(x[i]-'0');
	}
	// cout<<zs;
	for(int i=y;i<len;i++){
		xs+=pow(10,len-i-1)*(x[i]-'0');
	}
	// 小数部分位数为 len-y
	int b=pow(10,len-y),a=xs+zs*b,gys=zdgys(a,b);
	cout<<a/gys<<"/"<<b/gys;
	return 0;
}


```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7372d959b79a4e69b630bd0eb4016d64.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c3eb974865154a499d1fa750b9ee6968.png)

更新：
我在学校机房整活，修改、优化了一下这个程序。

```cpp
// Author:PanDaoxi
#include <iostream>
#include <cmath>
using namespace std;
int zdgys(int a,int b){
	for(int i=a>b?a:b;i>=1;i--){
		if(a%i==0&&b%i==0) return i;
	}
}
int main(){
	string x;
	bool jie=false;
	cin>>x;
	int len=x.length(),y,z,
	zs=0,xs=0;
	for(int i=0;i<len;i++){
		if(x[i]=='.'){
			z=i-1;
			y=i+1;
			jie=true;
			break;
		}
	}
	if(jie){
		// 实现整、小分离
		// 整数 x[0~z]  小数 x[y~(len-1)] 
		for(int i=0;i<=z;i++){
			zs+=pow(10,z-i)*(x[i]-'0');
		}
		// cout<<zs;
		for(int i=y;i<len;i++){
			xs+=pow(10,len-i-1)*(x[i]-'0');
		}
		// 小数部分位数为 len-y
		int b=pow(10,len-y),a=xs+zs*b,gys=zdgys(a,b);
		cout<<a/gys<<"/"<<b/gys;
	}
	else{
		cout<<"impossible!";
	}
	return 0;
}

```

