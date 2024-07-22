@[toc]


所谓高精度，就是大数的运算，这个大数可能是要远远超过现有数据类型的最大范围。如果我们想进行这样的运算，就要掌握计算的原理——竖式运算。

# 加法
我们这里先简单考虑非负数的加法，竖式这么列对吧：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/100188c0797942e796f075922ab5eeb2.png)
可能比较简陋但是就是这个意思。
我们如何储存过长的数呢？可以用数组存储。怎么才能将各个数位上的数放到数组里面呢？这里，我们可以使用字符串。
我们使用逆序储存，这样会比较方便，后面可以在`result`数组中反向输出。

```cpp
	// 高精度加法 240位内
	int a[241]={},b[241]={},result[242]={},x=0,y=0;
	string c,d;
	cin>>c>>d;
	// 第一步读取整数
	for(int i=c.size()-1;i>=0;i--){
		a[x++]=c[i]-'0';
	}
	for(int i=d.size()-1;i>=0;i--){
		b[y++]=d[i]-'0';
	}
```

接着，模拟运算：

```cpp
	// 第二步加法计算
	for(int i=0;i<(x>y?x:y);i++){
		result[i]+=(a[i]+b[i])%10;
		result[i+1]+=(a[i]+b[i])/10;
	}
```
反向输出：

```cpp
	for(int i=(x>y?x:y);i>=0;i--){
		cout<<result[i];
	}
```
完整的代码：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	// 高精度加法 240位内
	int a[241]={},b[241]={},result[242]={},x=0,y=0;
	string c,d;
	cin>>c>>d;
	// 第一步读取整数
	for(int i=c.size()-1;i>=0;i--){
		a[x++]=c[i]-'0';
	}
	for(int i=d.size()-1;i>=0;i--){
		b[y++]=d[i]-'0';
	}
	// 第二步加法计算
	for(int i=0;i<(x>y?x:y);i++){
		result[i]+=(a[i]+b[i])%10;
		result[i+1]+=(a[i]+b[i])/10;
	}
	for(int i=(x>y?x:y);i>=0;i--){
		cout<<result[i];
	}
	return 0;
}
```
---
# 减法
不说什么了，您能看懂我写的翔一样的代码嘛？

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	string s1,s2;
	int a[241]={},b[241]={},result[241]={},k=0,t;
	cin>>s1>>s2;
	// 考虑几种特殊情况
	if(s1==s2){
		cout<<0;
		return 0;
	}
	if(s1.size()<s2.size()||s1.size()==s2.size()&&s1<s2){
		cout<<"-";
		swap(s1,s2);
	}
	// 存储数据
	for(int i=0;i<s1.size();i++){
		a[s1.size()-i-1]=s1[i]-'0';
	}
	for(int i=0;i<s2.size();i++){
		b[s2.size()-i-1]=s2[i]-'0';
	}
	// 模拟竖式的算法
	for(int i=0;i<(s1.size()>s2.size()?s1.size():s2.size());i++){
	    t=10-b[i]+a[i]+result[k++];
		if(t<10) result[k]--; // 退位，在后面一位减去1
		result[k-1]=t%10;
	}
	// 前面可能有0，从第一个不是0的数开始输出
	for(int i=k-1;i>=0;i--){
		if(result[i]>0){
			t=i; // 记录第一个不是0的数
			break;
		}
	}
	// 输出
	for(int i=t;i>=0;i--){
		cout<<result[i];
	}
	return 0;
}
```
放到草稿纸上，想想就明白了。

---
# 乘法
## 高精度乘单精度
我们用单精度去乘高精度的每一位，然后累加。

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	// 高精度乘单精度（不超过10000）
    int a[251]={};
    string s1;
	int b;
    cin>>s1>>b;
    for(int i=0;i<s1.size();i++){
		a[i]=s1[s1.size()-i-1]-'0';
	}
	// 按位相乘
	for(int i=0;i<s1.size();i++){
		a[i]=a[i]*b;
	}
	// 处理进位
	for(int i=0;i<s1.size()+4;i++){
		if(a[i]>=10){
			a[i+1]+=a[i]/10;
			a[i]%=10;
		}
	}
	// 获取第一个不是0的数
	int point=0;
	for(int i=s1.size()+4;i>=0;i--){
		if(a[i]!=0){
			point=i;
			break;
		}
	}
	for(int i=point;i>=0;i--){
		cout<<a[i];
	}
	return 0;
}

```
## 高精度乘高精度
最难的地方，需要找找规律！

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	// 高精度乘高精度
    string s1,s2;
    int a[251],b[251],c[503]={};
    cin>>s1>>s2;
    for(int i=0;i<s1.size();i++) a[i]=s1[s1.size()-i-1]-'0';
    for(int i=0;i<s2.size();i++) b[i]=s2[s2.size()-i-1]-'0';
    for(int i=0;i<s1.size();i++){
    	for(int j=0;j<s2.size();j++){
			//     ↓ 这里是 +=
    		c[i+j]+=a[i]*b[j];
    		// 进位
    		if(c[i+j]>=10){
    			c[i+j+1]+=c[i+j]/10;
    			c[i+j]%=10;
			}
		}
	}
	int p=0;
	// 找到不是0的数
	for(int i=s1.size()+s2.size()-1;i>=0;i--){
		if(c[i]!=0){
			p=i;
			break;
		}
	}
	// 从p开始输出
	for(int i=p;i>=0;i--){
		cout<<c[i];
	}
	return 0;
}

```
---
# 除法

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int a,b,n,t=0,c[1001];
	cin>>a>>b>>n;
	cout<<a/b<<".";
	a=(a%b)*10;
	for(int i=0;i<n;i++){
		c[t++]=a/b;
		a=(a%b)*10;
	}
	for(int i=0;i<t;i++){
		cout<<c[i];
	}
	return 0;
}
```

---
# 乘方（2的n次方）
思路是高精度乘单精度，单精度的永远是2，然后循环。

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	/*
    高精度2的乘方
    思路：高精度*单精度2，循环n次
	*/
	int a[251]={1},n,len=1;
	cin>>n;
	for(int i=1;i<=n;i++){
		// 按位相乘
		for(int j=0;j<len;j++){
			a[j]*=2;
		}
		// 处理进位
		for(int j=0;j<len;j++){
			if(a[j]>=10){
				a[j+1]+=a[j]/10;
				a[j]%=10;
			}
		}
		if(a[len]>0) len++;
	}
	for(int i=len-1;i>=0;i--){
		cout<<a[i];
	}
	return 0;
}
```

