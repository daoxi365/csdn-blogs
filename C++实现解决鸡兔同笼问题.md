今天我第一次使用 C++ 语言，新手入门，请大家多多关照，博客有什么写错的地方请随时留言，我将随时改正，谢谢！

> 今天需要的材料：浏览器和网络 或 Dev-Cpp。

我先给大家推荐一个网站：[编程中国](https://bccn.net/)，这个网站可以在线编程。
如果有编程软件那么创建一个新的C++程序文件，命名为`01.cpp`即可，双击打开，输入以下代码：

> 例题：
> 鸡兔同笼，已知头共30个，脚共90只，问笼子中的鸡和兔各有多少只？

代码如下：

```cpp
# include <iostream>
# include <cstdio>
using namespace std;
//最开始的导入库代码

//main函数
int main()
{
	//创建变量
	int head,foot,chick,rabbit;
	//设置初始值
	head = 30;
	foot = 90;
	//计算
	chick = (4 * head - foot) / 2;  // chick = (foot - 2 * head) / 2; 
	rabbit = head - chick;
	cout << "鸡的数量：" << chick << "    兔的数量：" << rabbit << endl;
	getchar();
}
```
代码完成了！效果大家自己尝试！
