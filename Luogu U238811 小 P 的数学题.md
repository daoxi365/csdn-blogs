# [戳我直接看题解](#tijie)
---

# 小 P 的数学题

## 题目背景

小 $P$ 马上就要升入初中了。在此之前，他已经对初一的数学科目有了足够的了解……

## 题目描述

小 $P$ 有一些问题，想请你解答，内容主要是初一的数学题目，~~可能有些题有点儿超纲~~。

本题目分为 $12$ 个子问题，程序运行后首先输入一个整数 $n$ （ $1\le n\le 12$ ，分别对应冀教版的一至十一章，有一个是样例），程序需要输出第 $n$ 个问题的结果。

下面是每一道题的题干，请仔细阅读。

### 问题 1
$有理数a, b,c\ 满足a+b+c>0，且abc<0，求\frac{\lvert a \rvert}{a}+\frac{\lvert b \rvert}{b}+\frac{\lvert c \rvert}{c}+\frac{\lvert abc \rvert}{abc} 的值。$

输出一个整数，表示此题的答案。

### 问题 2
![luogu-t2](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/dc92ca6f15c50d6194809ba4c68b7537.jpeg)
输出一个**整数**，表示 $\angle EOC$ 的度数。

### 问题 3
$当a取下列值时，求代数式\frac{a^{2}-3a+1}{5}的值：
\\(1)a=4;(2)a=-\frac{1}{3}.$

输出两个整数，用换行符隔开。
除不尽的保留2位小数。

### 问题 4
$先化简，再求值：2(a^{2}-2ab-b^{2})+(-a^{2}+3ab+3b^{2})。其中a是绝对值最小的数，b是最大的负整数。$

### 问题 5
$规定“\heartsuit”是一种运算法则：a\heartsuit b=a^{2}-b.
\\(1)求5\heartsuit (-1)的值；(2)若(-4)\heartsuit x=2+x，求x的值。$

输出两个整数，用换行符隔开。

### 问题 6
$解方程组：
\left\{\begin{matrix}
    x+y=70,
   \\2x+3y=180
\end{matrix}\right.$

输出整数解 $x$ 、 $y$，用换行符隔开。

### 问题 7

![luogu-t7](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/180336494bc6ca159bf8e31a1790e0e6.jpeg)

> 既然这是个大题，我帮你回答一半，第一题的证明题我帮你证明，下面这个你自己来。
> 
> $\\证明：\\\because BE平分\angle ABF，FC平分\angle BFG\\
又\because \angle 1=\angle 2，\angle 1=\angle ABG，\angle 2=\angle BFG\\
\therefore \angle EBF=\angle BFC\\
\therefore EB//CF$

输出 $\angle BED$ 的度数，输出一个**整数**。

### 问题 8
$求值：y(x+y)+(x-y)^2-x^2-2y^2，其中x=-\frac{1}{3}，y=3.$

输出问题的答案（整数）。

### 问题 9 
![luogu-t9](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/00351394c991b2cd7b6b4c4f3aad7045.jpeg)

输出 $2$ 个整数，一行一个，表示第一问和第二问的答案。

### 问题 10
$解不等式组\left\{\begin{matrix}
   2x-5\ge 3(x-1), & ① 
\\ \frac{x}{3}-\frac{x-1}{2}<1,& ②
\end{matrix}\right. 并写出它的所有整数解。$

输出不等式组的整数解，按从小到大排列，一行一个。

### 问题 11
$因式分解：x^2-5xy+6y^2.\\
答案：(x+ay)(x+by).（a<b）$

输出两个整数表示 $a、b$，表示答案。

### 问题 12
$若x+y=7，xy=11，求 \frac{1}{2}x^2+\frac{1}{2}y^2的值。$

输出一个小数，表示答案。

## 输入格式

一个正整数 $n$ ，表示第 $n$ 号问题的答案。

## 输出格式

详见【题目描述】，根据题目要求给出对应答案。

## 样例 #1

### 样例输入 #1

```
12
```

### 样例输出 #1

```
13.5
```

## 提示

### 数据范围
保证 $1\le n\le 12$。
本题共 $12$ 个测试点，每个测试点的分数如下：

|测试点编号|分数|题目类型/知识点|
|:-:|:-:|:-:|
|$1$|$9$|绝对值的综合应用|
|$2$|$9$|几何初步|
|$3$|$8$|整式化简、代入求值|
|$4$|$9$|整式的加减|
|$5$|$9$|一元一次方程、定义新运算|
|$6$|$8$|二元一次方程组|
|$7$|$10$|平行线的性质|
|$8$|$8$|整式的乘法、化简求值|
|$9$|$10$|三角形初步|
|$10$|$10$|一元一次不等式组|
|$11$|$10$|因式分解|
|$12$|$0$|因式分解、配方法|

### 样例（问题 12）说明
> 此题指向第 $12$ 号测试点，通过不会增加分数。

$解：\\
\because x+y=7,xy=11\\
\therefore x^2+y^2=(x+y)^2-2xy=7^2-22=27 \\
\therefore \frac{1}{2}(x^2+y^2)=\frac{27}{2}=13.5$

### 提示
- 回答问题思考全面；
- 提交之前记得检查；
- 可以直接使用判断，也可以提交答案生成程序。

# <a id="tijie">题解</a>
> 这是我出的第二道题，欢迎观看我的[原创题单](https://www.luogu.com.cn/training/219530)。

呵呵，我今年新初一，但我喜欢内卷，就出了这个题目。

## 问题 1
> 难点：绝对值的性质。
> $\mathbf{若a\ge 0，|a|=a；\\若a<0，|a|=-a。}$

$解：\\\because abc<0 \\\therefore a,b,c中含有奇数个负因数 \\ \because a+b+c>0 \\\therefore a,b,c中至少有一个正数 \\ \therefore a,b,c一负二正 \\\therefore 原式=1+1-1-1=0.$

## <a id="q2">问题 2</a>
> 其实不难，是个方程题。
> 主要就是加减消元。

$解：\\设\angle AOD=\angle DOB=x°,\ \angle BOE=y°\\
则有\left\{\begin{matrix}
  & 2x+3y=180\ \ ①,\\
  & x+y=70\ \ ②
\end{matrix}\right.，\\①-2\times ②消元，得y=40，代回②式，解得x=30.
\\故\angle AOD=30°.$

## 问题 3
$解：\\原式=\frac{(a-1)^2-a}{5}=\frac{(a-1)^2}{5}-\frac{a}{5}.\\
当a=4时，原式=\frac{9}{5}-\frac{4}{5}=1.\\
当a=-\frac{1}{3}时，原式=\frac{\frac{19}{9}}{5}=\frac{19}{45}\approx 0.42.$

## 问题 4
> 绝对值最小的数是 $0$，最大的负整数是$-1$。

$解：原式\\=2(0-0-1)+(0+0+3)\\=1$

## 问题 5
$(1)原式=25+1=26.\\
(2)16-x=2+x，解得x=7.$

## 问题 6
解方程的内容，见[问题 4](#q2) 。

## 问题 7
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4495b69ae694430e85303a6a8118eeed.png)
$解：\\
\because \angle 2=\angle ABF=\angle 1 \\
\therefore AC//DG （同位角相等，两直线平行）\\
\therefore \angle C=\angle CFG =35°\\
\because BE//CF \\
\therefore \angle CFG=\angle BEF=35°\\
\therefore \angle BED=180°-\angle BEF=145°$

## 问题 8
> 直接代入求值即可。

$解：原式 \\
=xy+y^2+x^2+y^2-2xy-x^2-2y^2\\
=-xy \\
=1$

## 问题 9
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/91747c3fc3b8f511f1b732d905733355.jpeg#pic_center)
$解：\\
（1）\\\because BE平分\angle CBD，\angle ABC=90°-40°=50° \\
\therefore \angle CBE=\frac{180°-\angle ABC}{2}=65°\\
（2）\\\because EB//FD \\
\therefore \angle AEB=\angle EFD=180°-\angle A-(\angle ABC+\angle CBE)=180°-40°-115°=25°$

## 问题 10
$解不等式组\left\{\begin{matrix}
   2x-5\ge 3(x-1), & ① 
\\ \frac{x}{3}-\frac{x-1}{2}<1, &②
\end{matrix}\right. \\
得-3<x\le2，故不等式的整数解为-2.$

## 问题 11
$化简：\\
\ \ \ \ \ x^2-5xy+6y^2\\
=[x^2-6xy+(3y)^2]+xy-3y^2\\
=(x-3y)^2+y(x-3y)\\
=(x-3y)(x-2y)\\
故输出-3，-2.$

## 问题 12
$解：\\
\because x+y=7,xy=11\\
\therefore x^2+y^2=(x+y)^2-2xy=7^2-22=27 \\
\therefore \frac{1}{2}(x^2+y^2)=\frac{27}{2}=13.5$
