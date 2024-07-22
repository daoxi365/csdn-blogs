# [戳我直接看题解](#pandaoxi-yyds)

# [USACO1.5]回文质数 Prime Palindromes

## 题目描述

因为 $151$ 既是一个质数又是一个回文数（从左到右和从右到左是看一样的），所以 $151$ 是回文质数。

写一个程序来找出范围 $[a,b] (5 \le a < b \le 100,000,000)$（一亿）间的所有回文质数。

## 输入格式

第一行输入两个正整数 $a$ 和 $b$。

## 输出格式

输出一个回文质数的列表，一行一个。

## 样例 #1

### 样例输入 #1

```
5 500
```

### 样例输出 #1

```
5
7
11
101
131
151
181
191
313
353
373
383
```

## 提示

Hint 1: Generate the palindromes and see if they are prime.

提示 1: 找出所有的回文数再判断它们是不是质数（素数）.


Hint 2: Generate palindromes by combining digits properly. You might need more than one of the loops like below.

提示 2: 要产生正确的回文数，你可能需要几个像下面这样的循环。


题目翻译来自NOCOW。

USACO Training Section 1.5


产生长度为 $5$ 的回文数：

```cpp
for (d1 = 1; d1 <= 9; d1+=2) {    // 只有奇数才会是素数
     for (d2 = 0; d2 <= 9; d2++) {
         for (d3 = 0; d3 <= 9; d3++) {
           palindrome = 10000*d1 + 1000*d2 +100*d3 + 10*d2 + d1;//(处理回文数...)
         }
     }
 }

```

# <a id="pandaoxi-yyds">题解</a>
这个题暴力解是肯定解不了的，明摆着超时，要4秒多。
我们如何优化呢？

## 打表！
想不到吧？！
> 打表，是一个信息学专用术语，意指对一些题目，通过打表技巧获得**一个有序表或常量表**，来执行程序某一部分，优化时间复杂度。这种算法也可用于在对某种题目没有最优解法时，用来得到分数的一种策略。 —— **百度百科**

既然我们得不到，我们就毁了它！

生成表的程序：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e8; // 数据规模是1e8的
bool judge(int n){
	// 判断回文
	int t=0, m=n;
	while(m) t = t*10 + m%10, m /= 10;
	if(t == n){
		// 如果回文接着判断质数
		if(n <= 1) return false;
	 	for(int i=2; i*i<=n; i++) if(n%i == 0) return false;
		return true;
	}
	else return false;
}
int main(){
	// 把表储存到文本文档里
	freopen("PANDAOXI_YYDS.txt", "w", stdout);
	// 要开的数组的长度（即有多少个这样的回文质数）
	int len = 0;
	// 暴力枚举
	for(int i=2; i<=INF; i++){
		if(judge(i)){
			// 找到了这样的数，就输出它
			printf("%d, ", i);
			len++;
		}
	}
	// 换回来控制台输出
	freopen("con", "w", stdout);
	// 输出长度
	printf("%d", len);
	// 养成好习惯~
	fclose(stdout);
	return 0;
}
```

哈哈，你看懂了吗？
运行一下，控制台输出的是：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c9a9e5f7a3af4065acde29df495c40c9.png)
我的小电脑运行了 $3.265$ 秒，放到竞赛里绝对是过不了的，但是我们打成了这个表：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9b91722dd6564aa9b93740e03bbda8b3.png)
$PanDaoxi\ \_YYDS$，~~名副其实~~，一身傲气。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a00248dab06e417c93305853a06f622c.png)


接下来我放出来 AC 的模板：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int INF = 782; // 数组长度
int PANDAOXI_YYDS[INF] = {/* 看你自己咯，把 PANDAOXI_YYDS.txt 的内容直接复制过来 */}; // 打的表
int main(){
    int a, b;
    scanf("%d%d", &a, &b);
    // 疯狂枚举
    for(int i=0; i<INF; i++){
        if(PANDAOXI_YYDS[i] < a) continue; // 还没找到头，跳过
        if(PANDAOXI_YYDS[i] > b) break;    // 已经超过尾，结束
        if(PANDAOXI_YYDS[i]>=a && PANDAOXI_YYDS[i]<=b) printf("%d\n", PANDAOXI_YYDS[i]); // 刚刚好，输出
    }
    return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/fcbf4a54bd4e49d9a1b138b758fe4a1c.png)
29ms，轻松水过！

**祝大家2021CSP取得好成绩，$AC++$ ！**

> ![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0c940cb758a8433f80c3ac47f0be1ab2.png)



