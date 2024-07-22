![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/30140e6b6edd45319ab74c42be31b8d6.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b71f9ea3325a4a869d369e57ea38f17c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
还是这一道题：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b04d5275e8df4b87a7f09a1459ad3b61.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
可以用这样的方法：
```cpp
//Author:PanDaoxi
#include <iostream>
#include <cstring>
using namespace std;
const int n=100;
char a[n+1],s[100];
int top=0;
int main(){
	cin>>a;
	int len=strlen(a);
	for(int i=0;i<len;i++){
		if(a[i]=='('||a[i]=='['){
			top++;
			s[top]=a[i];
		}
		else if(a[i]==')'&&top>0&&s[top]=='(') top--;
		else if(a[i]==']'&&top>0&&s[top]=='[') top--;
		else {
			cout<<"NO"<<endl;
			return 0;
		}
	}
	if(top==0) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
	return 0;
}
```
亦或者这样：

```cpp
//Author:PanDaoxi
#include <stack>
#include <iostream>
#include <cstring>
using namespace std;
char a[100];
stack<char> s; // 创建char类型的栈s
int main(){
	cin>>a;
	int len=strlen(a);
	for(int i=0;i<len;i++){
		if(a[i]=='('||a[i]=='[') s.push(a[i]); // 对左括号进行入栈操作
		else if(a[i]==')'&&!s.empty()&&s.top()=='(') s.pop();
		else if(a[i]==']'&&!s.empty()&&s.top()=='[') s.pop();
		else {
			cout<<"NO"<<endl;
			return 0;
		}
	}
	// 判断栈是否为空
	if(s.empty()) cout<<"YES"<<endl;
	else cout<<"NO"<<endl;
	return 0;
} 
```
代码瞬间简单得多了。

