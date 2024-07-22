![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a8b407bc04534bb597b1f76680eff027.png)
```
有理数的加法运算法则：
(1) 同号两数相加，取相同的符号，再计算两数绝对值之和；
(2) 异号两数相加，取绝对值较大数的符号，再用较大的绝对值减去较小的绝对值。
```
依题意，高精度如下（无注释，可拿走使用）：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
#define int long long
#define endl "\n"

using namespace std;
const int INF = 101;

struct bn{
	string s, absn;
	int num[INF], len, absLen;
	bool neg;

	void inp(){
		cin >> s;
		len = s.size();

		neg = (s[0] == '-');
		absn = neg ? s.substr(neg) : s;
		absLen = absn.size();

		for(int i=0; i<absLen; i++){
			num[i] = absn[absLen-i-1] - '0';
		}
  		return;
	}
} a, b;
int c[INF+1];

char cABS(){
	if(a.absLen > b.absLen || (a.absLen >= b.absLen && a.absn > b.absn)){
		return 'a';
	}
	else if(a.absn == b.absn){
		return '=';
	}
	else{
		return 'b';
	}
}

void add(){
	for(int i=0; i<max(a.len, b.len)+1; i++){
		c[i] += a.num[i] + b.num[i];
		c[i+1] += c[i] / 10;
		c[i] %= 10;
	}
	return;
}

void sub(){
	for(int i=0; i<max(a.len, b.len)+1; i++){
		if(a.num[i] < b.num[i]) c[i+1]--;
		c[i] += 10 - b.num[i] + a.num[i];
		c[i] %= 10;
	}
	return;
}

void work(){
	if(!a.neg && !b.neg){
		add();
	}
	else if(a.neg && b.neg){
		cout << "-";
		add();
	}
	else{
		char c = cABS();
		if(c == '='){
			cout << 0;
			return;
		}
		
		if(a.neg && !b.neg){
			if(c == 'a'){
				cout << "-";
                sub();
			}
			else{
				swap(a, b);
				sub();
			}
		}
		else{
			if(c == 'a'){
				sub();
			}
			else{
				cout << "-";
				swap(a, b);
				sub();
			}
		}
	}

	int point = 0;
	for(int i=max(a.len, b.len) + 1; i>=0; i--){
		if(c[i]){
			point = i;
			break;
		}
	}
	for(int i=point; i>=0; i--){
		cout << c[i];
	}
	return;
}

signed main(){
	ios :: sync_with_stdio(false);

	a.inp();
	b.inp();
	work();

	return 0;
}
```
上面的程序可计算 $100$ 位内的两有理数加法。
具体的，有注释版本如下：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
#define int long long
#define endl "\n"

using namespace std;
const int INF = 101; 						// 支持 (INF-1) 位的运算

struct bn{ 									// 大数结构体
	string s, absn; 						// s: 输入的数  		absn: 绝对值
	int num[INF], len, absLen;				// num: 逆序存储        len: 输入的数的长度     absLen: 绝对值的长度
	bool neg;                       		// neg: 负数标记

	void inp(){
		cin >> s;
		len = s.size();

		neg = (s[0] == '-');            	// 获取负数标记
		absn = neg ? s.substr(neg) : s; 	// 截取绝对值
		absLen = absn.size();               // 获取绝对值长度

		for(int i=0; i<absLen; i++){        // 只记录绝对值的逆序，和符号无关
			num[i] = absn[absLen-i-1] - '0';
		}
  		return;
	}
} a, b;                                     // 输入的两个数
int c[INF+1];                               // 结果

char cABS(){                                // 字符串长度比较（字典序）
	if(a.absLen > b.absLen || (a.absLen >= b.absLen && a.absn > b.absn)){
		return 'a';
	}
	else if(a.absn == b.absn){
		return '=';
	}
	else{
		return 'b';
	}
}

void add(){                                 // 加法函数 (a+b)
	for(int i=0; i<max(a.len, b.len)+1; i++){
		c[i] += a.num[i] + b.num[i];
		c[i+1] += c[i] / 10;
		c[i] %= 10;
	}
	return;
}

void sub(){                                 // 减法函数 (a-b)
	for(int i=0; i<max(a.len, b.len)+1; i++){
		if(a.num[i] < b.num[i]) c[i+1]--;
		c[i] += 10 - b.num[i] + a.num[i];
		c[i] %= 10;
	}
	return;
}

void work(){
	if(!a.neg && !b.neg){                   // 同号（正）
		add();
	}
	else if(a.neg && b.neg){                // 同号（负）
		cout << "-";
		add();
	}
	else{                                   // 异号
		char c = cABS();
		if(c == '='){                       // a=b，a-b=0
			cout << 0;
			return;
		}

		if(a.neg && !b.neg){                // a负b正
			if(c == 'a'){                   // a的绝对值大于b的绝对值
				cout << "-";
                sub();
			}
			else{                           // a的绝对值小于b的绝对值
				swap(a, b);
				sub();
			}
		}
		else{                               // a正b负
			if(c == 'a'){                   // a的绝对值大于b的绝对值
				sub();
			}
			else{                           // a的绝对值小于b的绝对值
				cout << "-";
				swap(a, b);
				sub();
			}
		}
	}

	int point = 0;                          // 高精度的输出
	for(int i=max(a.len, b.len) + 1; i>=0; i--){
		if(c[i]){
			point = i;
			break;
		}
	}
	for(int i=point; i>=0; i--){
		cout << c[i];
	}
	return;
}

signed main(){
	ios :: sync_with_stdio(false);

	a.inp();
	b.inp();
	work();

	return 0;
}

```

