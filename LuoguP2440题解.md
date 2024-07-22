# 木材加工

## 题目背景

要保护环境

## 题目描述

木材厂有 $n$ 根原木，现在想把这些木头切割成 $k$ 段长度**均**为 $l$ 的小段木头（木头有可能有剩余）。

当然，我们希望得到的小段木头越长越好，请求出 $l$ 的最大值。

木头长度的单位是 $\text{cm}$，原木的长度都是正整数，我们要求切割得到的小段木头的长度也是正整数。

例如有两根原木长度分别为 $11$ 和 $21$，要求切割成等长的 $6$ 段，很明显能切割出来的小段木头长度最长为 $5$。

## 输入格式

第一行是两个正整数 $n,k$，分别表示原木的数量，需要得到的小段的数量。

接下来 $n$ 行，每行一个正整数 $L_i$，表示一根原木的长度。

## 输出格式

仅一行，即 $l$ 的最大值。

如果连 $\text{1cm}$ 长的小段都切不出来，输出 `0`。

## 样例 #1

### 样例输入 #1

```
3 7
232
124
456
```

### 样例输出 #1

```
114
```

## 提示

#### 数据规模与约定

对于 $100\%$ 的数据，有 $1\le n\le 10^5$，$1\le k\le 10^8$，$1\le L_i\le 10^8(i\in[1,n])$。


```cpp
// Author: PanDaoxi
#include <bits/stdc++.h>
#define int long long
using namespace std;

const int INF = 1e5 + 1;
int n, k, l, r, mid, a[INF];

bool check(int t){
	/*
        我们要求出每根棍按t截出来的数量
        然后和k作比较
        如果q >= k ===> true
        否则       ===> false
	*/
	int q = 0;
	for(int i=1; i<=n; i++){
		q += a[i] / t;
	}
	return q >= k;
}

signed main(){
	ios :: sync_with_stdio(false);
	
	cin >> n >> k;
	l = 0, r = INT_MIN;
	for(int i=1; i<=n; i++){
		cin >> a[i];
		r = max(r, a[i]);
	}
	
	while(l <= r){
		mid = (l+r) / 2;
		if(mid != 0){
			if(check(mid)){
				l = mid + 1;
			}
			else{
				r = mid - 1;
			}
		}
		else{
			cout << 0;
			return 0;
		}
	}
	cout << r;
	
	return 0;
}
```


[video(video-MkJdtLY6-1666702389191)(type-csdn)(url-https://live.csdn.net/v/embed/248023)(image-https://live-file.csdnimg.cn/release/live/file/1666620168028.png?x-oss-process=image/resize,l_300)(title-P2440题解)]

