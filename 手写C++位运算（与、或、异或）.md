大概是太闲得慌，练练手写了个这玩意儿。
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
