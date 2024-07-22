# 一、认识递归
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/4abe2f7a2f75ca56a1336d8b5f48e6b2.png)
如果对其不加限制，程序会一直进行下去。
```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;

void story(){
	cout<<"从前有座山，山里有个庙，庙里有老和尚和小和尚，老和尚给小和尚讲故事，讲了什么呢？";
	getchar();
	story();
	return;
}

int main(){
	story();
	return 0;
}
```
如果这样不加节制的运行下去，就形成了死循环，程序会运行到系统崩溃为止。所以要实现以下效果，我们需要对它进行条件判断。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/8e7f51f0892272c4614b5d84b2fe2110.png)

```cpp
//Author:PanDaoxi
#include <iostream> 
using namespace std;
int n=0;
void story(){
	n++;
	cout<<"(第"<<n<<"遍)从前有座山，山里有个庙，庙里有老和尚和小和尚，老和尚给小和尚讲故事，讲了什么呢？";
	getchar();
	if(n<10) story();  //边界条件
	else cout<<"故事讲完了！"<<endl;
	return;
}

int main(){
	story();
	return 0;
}
```
这就是简单的递归算法。

<hr>

# 二、递归算法的运用
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/83b34ca514009df3ab85386e378f0fc6.png)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/21955f21fc8ed849bf400bc6f411aa5b.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/05c5d91e280242d4c7f22e7c99eae343.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/a6386a319505350023d733fc4bcbaa06.png)
做递归算法，我们需要找到以下几点：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/3e9ce8926568c3fb57e5a3bd99ca1d74.png)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;

int age(int n){
	int c;
	if(n==1) c=10;
	else c=age(n-1)+2;
	return c;
}

int main(){
	cout<<age(5);
	return 0;
} 
```

