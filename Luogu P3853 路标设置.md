这大概是我第一次发![<p style="color: rgb(82, 196, 26);">普及+/提高</font>](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/84d094ea3f424229bd155bb3d8b782ac.png)难题的题解吧……

这道题我整了好几天，才过。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4bcd20053e614580971629598b41be36.png)

# 题面 $\&$ 题解
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d2c9f67209b043bdad5ba07139285077.png)


如果单纯地思考怎么拿部分分，那这个题并不难，暴力模拟一遍就行了，小样例能过。
如果你要拿![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a361cbcf74914de7a47acb1e8348d347.png)，那你就不能枚举了，需要**二分**降低时间复杂度。

> 我的老师说过：求最小值的最大值（最大值的最小值），跑不了**二分答案**。

因为起点和终点都有路标，所以我们可以确定出“空旷值”的范围啦（即下限为 $0$， 上限为 $L$）。我们在这期间开始二分答案每一个“空旷值”。

思考一下，二分答案的判断函数怎么写呢？
我们可以**从第一个路标枚举到最后一个路标，取两个路标的距离差**。如果这个距离差大于$mid$，那么我们就可以增加一个路标了。
为了进一步降低时间复杂度，我们可以使用~~小学~~数学来解决一下。我们可以知道：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/52783020f9f94a129dbf3f95bebae093.png)
（图画的很丑，拿鼠标画的我尽力了）
考虑一种特殊情况，如果距离差刚好整除$mid$，那么需要减去一。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7d53b274ff754e488f927197ca3d3f43.png)
我们用一个计数器$cnt$记录每一个距离差之间放的路标数量。我们可以根据$cnt$和最多放的路标数量$K$作比较，如果$cnt<=K$返回真，反之返回假。

再说二分模板，我们可以根据$check$函数的返回值来对应$l$和$r$的变化。如果返回值为真，说明空旷值还可以进一步缩小；反之表示空旷值过小。
**因此如果$check$返回真，我们需要往左看；返回假，我们需要向右看。**

由于最后是求最小值，所以需要输出左边界。

完整程序如下：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e5 + 1;
int k, n, m, l, r, mid, a[INF];

bool check(int t){
	int cnt = 0,
		now = 0;
	for(int i=1; i<=n; i++){
		/*
            取两个路标之差x，cnt+=x/t
            特判如果x%t为0，那么cnt--
		*/
  		now = a[i] - now;
		if(now > t) cnt += now/t - (now%t == 0);
		now = a[i];
	}
	if(cnt <= m) return true;
	else return false;
}

int main(){
	ios :: sync_with_stdio(false);

	cin >> k >> n >> m;
	for(int i=1; i<=n; i++){
		cin >> a[i];
	}
	l = 0, r = k;

	while(l <= r){
		mid = (l+r) / 2;
		if(check(mid)){
			r = mid - 1;
		}
		else{
			l = mid + 1;
		}
	}
	cout << l;

	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d7ac5e14707a41db89b2bf5d61f1dbf9.png)

# 拓展
Luogu P2678 跳石头
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8b697e6797ff40ed84359ad01bb6d5b2.png)
类比于《路标设置》的思想，刚才的那道题是**枚举空旷指数**，这个题是**枚举跳跃距离**。思考一下，得到以下程序：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
#define int long long
using namespace std;

const int INF = 5e4 + 1;
int k, m, n, l, r, mid, a[INF];

bool check(int t){
	int cnt = 0,
		now = 0;
	for(int i=1; i<=n; i++){
		if(a[i] - now >= t) now = a[i];
		else cnt++;
	}
	if(k - now < t){
		cnt++;
	}
	if(cnt <= m) return true;
	else return false;
}

signed main(){
	ios :: sync_with_stdio(false);
	
	cin >> k >> n >> m;
	l = 1, r = k;
	for(int i=1; i<=n; i++){
		cin >> a[i];
	}

	while(l <= r){
		mid = (l+r) / 2;
		if(check(mid)){
			l = mid + 1;
		}
		else{
   			r = mid - 1;
		}
	}
	cout << r;
	
	return 0;
}
```

# 题外话
预祝全天下$OIer$们程序员节快乐！

我去年$1024$来的洛谷，到今天快一年了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/aee468dca4724b35b4dc74216ef34ffd.png)
一年前我还啥也不是，现在已经可以开始挑战难题了（部分是跟着老师做的）
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/436174b3b09947e085be1881105bcd68.png)

---

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/114fba857233428fb2a16616e379dc44.png#pic_center)


由于今年的形势（学校那边的七天小长假不好请），我决定不参加$CSP2022$，再努力一年，明年再战。
$OIer$们加油啊！**祝全天下$OIer$能取得好成绩！**

