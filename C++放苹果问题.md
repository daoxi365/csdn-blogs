近期由于课业繁忙，无法发布文章，只能利用周末的时间抓紧学习C++语言。今天下午突然有事，所以下午没办法发布有关算法学习的文章了。望谅解。

周内尽可能发布广度优先搜索的学习、使用。
<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/de75da15b495440eb1cb71e0dcf5a297.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int apple(int m,int n){
	if(m<0||n<1) return 0;
	else if(m==0||n==1) return 1;
	else if(m<n) return apple(m,m);
	else return apple(m-n,n)+apple(m,n-1);
}
int main(){
	int n;
	cin>>n;
	while(n){
		int a,b;
		cin>>a>>b;
		cout<<apple(a,b)<<endl;
		n--;
	}
	return 0;
} 
```
这里分为几种情况：

 - 如果没有苹果，那么有多少个盘子也没用，返回`0`，**没有放法**；
 - 只有一个盘子的话，那么无论有没有苹果，**都只有`1`种放法**；
 - 如果`n`大于`m`，则和`m`个苹果放在`m`个盘子里，**所以递归传入两个`m`值**；
 - 如果`m`大于等于`n`，则有两种情况：一是都有苹果（`n`个苹果放在`n`个盘子中，**剩下的`m-n`个苹果放在`n`个盘子中**），二是有的没有苹果（与至少有`1`个盘子归为一类，**递归传入`m`和`n-1`**），**程序设计为`apple(m-n,n)+apple(m,n-1)`即可**。
