@[toc]

# 1.回文数判定

```cpp
//Author:PanDaoxi 
#include <iostream>
#include <cmath>
using namespace std;
bool text(int n){ //判定回文数 
	int a[11],m=n,k=0;
	while(m){
		a[k++]=m%10;
		m/=10;
	}
	m=0;
	for(int i=0;i<k;i++){
		m+=pow(10,i)*a[k-i-1];
	}
	if(m==n) return true;
	else return false;
}
int main(){
	int n;
	cin>>n;
	if(text(n)) cout<<"YES";
	else cout<<"NO";
	return 0;
} 
```

# 2.质数的判定

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
bool prime(int n){
	if(n==1) return false;
	for(int i=2;i<n;i++) if(n%i==0) return false;
	return true;
}
int main(){
	int n;
	cin>>n;
	if(prime(n)) cout<<"YES";
	else cout<<"NO";
	return 0;
} 
```
# 3.最大公因数和最小公倍数

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int zdgys(int a,int b){
	for(int i=a>b?a:b;i>=1;i--){
		if(a%i==0&&b%i==0) return i;
	}
}
int zxgbs(int a,int b){
	return a*b/zdgys(a,b);
}
int main(){
	int n,m;
	cin>>n>>m;
	cout<<zdgys(n,m)<<" "<<zxgbs(n,m);
	return 0;
} 
```

# 4.阶乘

```cpp
// Author:pandaoxi 
#include <iostream>
using namespace std;
int main(){
	int n,s=1;
	cin>>n;
	for(int i=1;i<=n;i++){
		s*=i;
	}
	cout<<s;
	return 0;
} 
```

# 5.超大数（200位以内）判断是否为3的整数倍

```cpp
// Author:pandaoxi 
#include <iostream>
#include <cstring>
using namespace std;
int main(){
	int a[201],l=1,s=0;
	char b[201];
	cin>>b;
	for(int i=0;i<strlen(b);i++){
		if(b[i]=='0') a[l++]=0;
		else if(b[i]=='1') a[l++]=1;
		else if(b[i]=='2') a[l++]=2;
		else if(b[i]=='3') a[l++]=3;
		else if(b[i]=='4') a[l++]=4;
		else if(b[i]=='5') a[l++]=5;
		else if(b[i]=='6') a[l++]=6;
		else if(b[i]=='7') a[l++]=7;
		else if(b[i]=='8') a[l++]=8;
		else if(b[i]=='9') a[l++]=9;
		else return 0;
	}
	for(int i=0;i<l;i++){
		s+=a[i];
	}
	if(s%3) cout<<"No";
	else cout<<"Yes";
	return 0;
} 
```
# 6.保留m位小数
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/87b23995025e46ad932f49da9456dbf0.png)

```cpp
// Author:PanDaoxi
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
	double n;
	int m;
	cin>>n>>m;
	cout<<fixed<<setprecision(m)<<n;
	return 0;
}

```
# 7.分解质因数

```cpp
// Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n,a[1001],k=0;
    cin>>n;
    if(n<2){
		cout<<"Impossible";
		return 0;
	}
	for(int i=2;i<=n;i++){
		while(n%i==0){
			a[k++]=i;
			n/=i;
		}
	}
	sort(a,a+k);
	for(int i=0;i<k;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}

```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/550e30d93f0944729db03224809650a6.png)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/57a9af7793294f7395e1de082fa2d851.png)
# 8.十进制与二进制的互相转换
## （1）十进制转二进制
```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int a[10001],k=0,s=2; // s进制（s<=10）
void f(int n){
	if(n==0) return;
	a[k++]=n%s;
	f(n/s); 
}
int main(){
	int n;
	cin>>n;
	f(n);
	for(int i=k-1;i>=0;i--){
		cout<<a[i];
	}
	return 0;
} 
```
## （2）二进制转十进制

```cpp
// Author:PanDaoxi
#include <iostream>
#include <cmath>
using namespace std;
int main(){
	string s;
	int a[10001],sum=0,k=0;
	cin>>s;
	for(int i=0;i<s.length();i++){
		if(s[i]-'0') a[k++]=1;
		else a[k++]=0;
	}
	for(int i=0;i<k;i++){
		sum+=pow(2,i)*a[k-i-1];
	}
	cout<<sum;
	return 0;
} 
```

# 9.十进制与十六进制的互相转换
## （1）十进制转十六进制

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int a[10001];
int k=0;
void f(int n){
	if(n==0) return;
	int x=n%16;
	if(x<10) a[k++]=x+'0';
	else a[k++]=x+('A'-10);
	f(n/16);
}
int main(){
	int n;
	cin>>n;
	f(n);
	for(int i=k-1;i>=0;i--){
		cout<<char(a[i]);
	}
	return 0;
} 
```
## （2）十六进制转十进制

```cpp
// Author:PanDaoxi
#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;
int main(){
	char s[1001];
	cin>>s;
	int sum=0,len=strlen(s);
	for(int i=0;i<len;i++){
		int x;
		if('A'<=s[i]&&s[i]<='F') x=s[i]-('A'-10);
		if('0'<=s[i]&&s[i]<='9') x=s[i]-'0';
		sum+=pow(16,len-i-1)*x; 
	}
	cout<<sum;
	return 0;
} 
```
# 10.中位数、众数
## （1）中位数

```cpp
// Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int n,a[1001];
	double s;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	sort(a,a+n);
	if(n%2){
		s=a[n/2];
	}
	else{
		s=(a[n/2-1]+a[n/2])/2.0;
	}
	cout<<s;
	return 0;
} 
```
## （2）众数

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int n,a[10001]={},x,y;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>x;
		a[x]++;
	}
	x=0;
	for(int i=0;i<10001;i++){
		if(a[i]>x){
			x=a[i];
			y=i;
		}
	}
	cout<<y;
	return 0;
} 
```
# 11.小数化分数

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
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/88178b3e722242288d835a323122c03c.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e9723fe5e06e43acad663d646e7bdbf9.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/78638a0dc34c4490a9c5890010b06fe1.png)
# 12. 与、或、异或 的模拟
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
// 十进制转二进制
int a[10001],l;
void f(int n){
	if(n==0) return;
	a[l++]=n%2;
	f(n/2);
}
string tentotwo(int n){
	f(n);
	string s="";
	for(int i=l-1;i>=0;i--){
		s+=a[i]+'0';
	}
	memset(a,0,sizeof(a));
	l=0;
	return s;
}
// 二进制转十进制
int twototen(string s){
	int b[11]={},sum=0,k=0;
	for(int i=0;i<s.size();i++){
		if(s[i]-'0') b[k++]=1;
		else b[k++]=0;
	}
	for(int i=0;i<k;i++){
		sum+=pow(2,i)*b[k-i-1];
	}
	return sum;
}
int main(){
	int a,b;
	char c;
	// 输入表达式
	cin>>a>>c>>b;
	// 转换为二进制
	string s1,s2,result="";
	s1=tentotwo(a),s2=tentotwo(b);
	// 补齐前导0
	int l1=s1.size(),l2=s2.size();
	while(min(l1,l2)<max(l1,l2)){
		if(l1<l2) s1='0'+s1;
		else s2='0'+s2;
		l1=s1.size(),l2=s2.size();
	}
	// 按位与
	if(c=='&'){
		// 这时 l1=l2 所以都一样
		for(int i=l1-1;i>=0;i--){
			// 同真则真
			result=((s1[i]=='1'&&s2[i]=='1')?"1":"0")+result;
		}
	}
	// 按位或
	else if(c=='|'){
		for(int i=l1-1;i>=0;i--){
			// 一真则真
			result=((s1[i]=='1'||s2[i]=='1')?"1":"0")+result;
		}
	}
	// 按位异或
	else if(c=='^'){
		for(int i=l1-1;i>=0;i--){
			// 不同为真
			result=((s1[i]!=s2[i])?"1":"0")+result;
		}
	}
	else cout<<0;
	// 再转换为10进制
	cout<<twototen(result);
	return 0;
}
```
直接输入表达式即可，但是切记不要太大，程序会爆掉。
仅为了方便大家理解，考试时位运算也是很有用的。
输入整数 $a$ 字符 $c$ 和整数 $b$ ，别输负数，中间不用空格。

# 13.后缀表达式转换
[P1149 后缀表达式](https://www.luogu.com.cn/problem/P1449)
诶嘿还挺神奇，我就蒙出来了……😅

```cpp
// Author:PanDaoxi
#include <iostream>
#include <stack>
using namespace std;
stack<int> st;
int sti(string s){
	int n=0;
	for(int i=0;i<s.size();i++){
		n=10*n+(s[i]-'0');
	}
	return n;
}
int main(){
	string s,temp="";
	cin>>s;
	for(int i=0;i<s.size();i++){
		// 如果遇到@
		if(s[i]=='@') break;
		// 累计数字
		if('0'<=s[i]&&s[i]<='9'){
			temp+=s[i];
		}
		// 记录数字
		if(s[i]=='.'){
			st.push(sti(temp));
			temp="";
		}
		// 遇到符号就计算
		if(s[i]=='+'){
			// 取出2个数
			int x=st.top();st.pop();
			int y=st.top();st.pop();
			st.push(x+y);
		}
		else if(s[i]=='-'){
	        int x=st.top();st.pop();
			int y=st.top();st.pop();
			// 前面的减后面的
			st.push(y-x);
		}
		else if(s[i]=='*'){
		    int x=st.top();st.pop();
			int y=st.top();st.pop();
			st.push(x*y);
		}
		else if(s[i]=='/'){
		    int x=st.top();st.pop();
			int y=st.top();st.pop();
			st.push(y/x);
		}
	}
	cout<<st.top();
	return 0;
}
```

