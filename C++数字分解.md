1.   数字分解
【问题描述】
任何一个大于1的自然数n,总可以拆分成若干个小于n的自然数之和，当n等于5时有6种拆分方法：

```cpp
5=1+1+1+1+1
5=1+1+1+2
5=1+1+3
5=1+2+2
5=1+4
5=2+3
```

输入：一行包含一个正整数n（1<n<10）。
输出：先将拆分方案输出，然后再输出拆分的方案数。
【输入样例】

```cpp
5
```

【输出样例】

```cpp
5=1+1+1+1+1
5=1+1+1+2
5=1+1+3
5=1+2+2
5=1+4
5=2+3
total=6
```

<hr>

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int a[10001]={1},n,sum=0;
void output(int y){
	cout<<n<<"=";
	for(int i=1;i<=y-1;i++) cout<<a[i]<<"+";
	cout<<a[y]<<endl;
	sum++;
}
void find(int m,int x){
	for(int i=a[x-1];i<=m;i++){
		if(i<n){
			a[x]=i;
			m-=i;
			if(m==0) output(x);
			else find(m,x+1);
			m+=i; 
		}
	}
}
int main(){
	cin>>n;
	find(n,1);
	cout<<"total="<<sum<<endl;
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/eb6c44029d8a4b1e87ca7097c26ab04f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

