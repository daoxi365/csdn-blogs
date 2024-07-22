今天刷题闲得慌，写了个程序去运算“干支纪年法”。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/710d729cdcf346a893b3b1e7d6260a6d.png)
这有一种比较好的写法，我们可以直接将内容按顺序储存到字符串数组中，直接按下标访问即可，没有必要再写那么多`switch`，多麻烦呐？

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	// 天干，按顺序取余结果0~10排序
	string tg[11]={"庚","辛","壬","癸","甲",
	//               0    1    2    3    4
	"乙","丙","丁","戊","己"},
	//5   6    7    8    9
	// 地支，同样
	dz[13]={"申","酉","戌","亥","子",
	//       0     1    2    3    4
	"丑","寅","卯","辰","祀",
	//5   6    7    8    9
	"午","未"};
	//10   11
	// 输入年份
	int n;
	cin>>n;
	// 输出天干、地支
	cout<<tg[n%10]<<dz[n%12];
	return 0;
}
```
（话说，曾经我也犯过这个错误，后面慢慢就发现用的步骤太复杂了，跑着也慢）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1f618ccdbaf34b0a9fc6d753220afd4f.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/c2c174ef19414956a4fd1a3a07ecd741.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/053c827a57a647669b30df768f65437d.png)

