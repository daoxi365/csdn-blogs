

hello，大家好，我是你们的新朋友，你们可以叫我小潘~

或许大家是第一次见到我，也有可能是其他平台过来的，我都要给大家作个自我介绍：我是来自河北石家庄的一名新初一学生。我热爱编程技术，擅长Python、C++和命令行（Windows批处理），目标是信息学竞赛。
我的同学们都说我很幽默，甚至有人说我“不正经”😑 。

你现在看到的文章是一个特别、特别厉害的失败者写下的，希望大家可以吸取我的惨痛教训，创造出你们的海阔天空。

> 咳咳，别的好成绩别说，我直到现在的模拟赛成绩都在100以内。

OK，我们介绍完了，来说说这个专辑**C++信息学竞赛从入门到出门**😎 ，大家可以在这里从学C++，入门信息学竞赛，~~然后再出门~~！

---
那我们废话不多说，现在我们来开始今天的内容————
# HELLO,C++
首先吧，你得知道C++是啥，不然学了半天都白学。

> C++ 是一种静态类型的、编译式的、通用的、大小写敏感的、不规则的编程语言，支持过程化编程、面向对象编程和泛型编程。
C++ 被认为是一种中级语言，它综合了高级语言和低级语言的特点。
C++ 是由 Bjarne Stroustrup 于 1979 年在新泽西州美利山贝尔实验室开始设计开发的。C++ 进一步扩充和完善了 C 语言，最初命名为带类的C，后来在 1983 年更名为 C++。
C++ 是 C 的一个超集，事实上，任何合法的 C 程序都是合法的 C++ 程序。
注意：使用静态类型的编程语言是在编译时执行类型检查，而不是在运行时执行类型检查。
> C++ 完全支持面向对象的程序设计，包括面向对象开发的四大特性：封装、抽象、继承、多态

我嘞个去，这都是啥跟啥啊？！
没关系，看不懂也没事儿，就记住一点：C++是**面向对象编程语言**！
C++、Python、Java等等等，现在主流的编程语言，<font color="red">除了C语言</font>，都是**面向对象编程语言**。

OK，看到这儿，你就能做题了：

>[CSP-J 2021]以下不属于面向对象程序设计语言的是（ ）。
 A. C++
 B. Python
 C. Java
 D. C

显而易见~答案是？D！
现在，你的C++漫漫长路，已经迈出了第一步。我们继续看：
> Luogu B2002 Hello,World!
【题目背景】
强烈推荐[新用户必读贴](https://www.luogu.com.cn/discuss/241461)
【题目描述】
编写一个能够输出 `Hello,World!` 的程序，这个程序常常作为一个初学者接触一门新的编程语言所写的第一个程序，也经常用来测试开发、编译环境是否能够正常工作。
【样例 #1】
【样例输入 #1】
>```
>无
>```
>【样例输出 #1】
>```
>Hello,World!
>```
>【提示】
>- 使用英文标点符号；
>- `Hello,World!` 逗号后面**没有**空格。

大家都有devcpp吧？如果没有就下一个安装，有的话就继续搞~
现在，让我们开始**熟悉语法**。
在我们学**函数**和**递归算法**以前，你完全可以把下面的内容当做模板：
```cpp
#include <bits/stdc++.h> // 导入所有函数，万能头文件
using namespace std; // 使用命名空间
int main(){
    // 在这里写程序
	
    return 0; // 退出程序
}
```

我们这时候要输出`Hello,world!`，需要先认识两个重要功能：`cout`和`printf`。它们是标准的输出流。用法：
```cpp
cout<<"这里是cout输出的内容"<<endl; // endl为换行
printf("这里是printf输出的内容\n"); // \n为换行
```
在devcpp里面写好，编译运行：
![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/1c50cd02be8b334b8bbec006ad83f525.png)


你可以看到，程序正常地输出了文字。

![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/290b42c48647d4a721333aac5f8dda8c.png)

那么还有个问题，怎么输入呢？

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	// 在此声明变量
	cin>>变量1>>变量2>>...>>变量n;
	return 0;
}
```
这样，就给每个变量输入并赋值啦~

## C++的运算
运算是很简单的啊，和别的语言一样。相信大家对别的编程语言有所了解，其实都一样，一通百通~
![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/fdca5326075a50c7790c516302bb0ce8.jpeg)
就是这么神奇~来试试看：
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	// 建议加上括号，不加也对
	cout<<(1+2)<<endl;
	cout<<(1-2)<<endl;
	cout<<(1*2)<<endl;
	cout<<(1%2)<<endl; // 取余运算
	// 数据范围小的话可以使用pow函数计算幂，该句的意思是1的平方。
	cout<<pow(1,2)<<endl; 
	// 计算2的算术平方根
	cout<<sqrt(2)<<endl;
	return 0;
}
```
但是，有一个易错点，你知道下面这个程序输出的结果嘛？
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	cout<<(1/2);
	return 0;
}
```
![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/2053d6ecab1e519a900edec23ed3e158.png)
哈哈哈，惊讶吗？？这是为什么？！
> 因为C++语言是个静态类型语言，它不转换的话整数始终是整数，小数始终是小数。所以在C++的眼里1/2=0.5，但是1和2是整数，所以要**向下取整**，结果就是0！这一点一定要记住，特别重要！！

但是怎么才能让它变成小数类型呢？首先我们要认识一个概念：
> `float` 为 **“单精度浮点数”**；
> `double` 为 **“双精度浮点数”**。

在信息学竞赛中，我们使用`double`类型比较多，那么如何强制类型转换呢？
```cpp
(要转换的数据类型)(要转换的内容)
```
例如，我们需要转换1/2的值，可以这样写：
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	cout<<(double)(1)/(double)(2);
	return 0;
}
```
这里有个小坑儿，需要先转换然后再做除法。因为转换前会先运算表达式，所以整型的结果转换为浮点型，和原来一样。

> 这里还有个点儿，比较低级的类型转换类型时会自动转换。所以想要实现刚才的效果还可以这样写：
> ```cpp
> // Author:PanDaoxi
> #include <bits/stdc++.h>
> using namespace std;
> int main(){
> 	cout<<(double)(1)/2<<endl;
> 	cout<<1/(double)(2)<<endl;
> 	return 0;
> }
> ```
> C++语言有好多坑，一不留神就踩进去了！
> ![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/a0b646419940dc377d3646cca9c05296.jpeg)

现在我们来看一个题儿：
> Luogu B2022 输出保留 12 位小数的浮点数
> ![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/9eb1d46dff0d9bebdff151375974e672.png)

啊这，怎么保留呢？
记住一个写法：
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	cout<<fixed<<setprecision(保留小数的位数)<<保留的小数;
	return 0;
}
```

结合以前的写法，你自己写一写叭！

---

参考答案：
```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int main(){
	double n;
	cin>>n;
	cout<<fixed<<setprecision(12)<<n;
	return 0;
}
```
![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/96ff11c942a4dd98cc4638d8e02a15ad.png)

今天，就先说到这儿叭，明天见！
![image](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/75ce6f8c22df247c3c0b56bb9cc01066.gif)

