![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/a16f9fa874d540e4b20c05adeee7125c.png)


## 提示

对于 $100\%$ 的数据，$1 \le R,C \le 1000$。

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/94bb11ac51bf4a16b8639c22f9e6edf7.png)

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int inf = 1e3+1;
int n, m, ans, cnt, mini, minj, maxi, maxj,
	fx[5] = {0, -1, 1, 0, 0},
	fy[5] = {0, 0, 0, -1, 1};
bool a[inf][inf];
void dfs(int x, int y){
	// 更新位置信息
	maxi = max(maxi, x),
	maxj = max(maxj, y),
	mini = min(mini, x),
	minj = min(minj, y),
	cnt++, a[x][y] = false;
	
	// 搜索
	for(int i=1; i<=4; i++){
		int xx = x + fx[i], yy = y + fy[i];
		if(
			a[xx][yy] &&
			x >= 1 && x <= n &&
			y >= 1 && y <= m
		) dfs(xx, yy);
	}
}
int main(){
	ios :: sync_with_stdio(false);
	cin >> n >> m;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			char c;
			cin >> c;
			a[i][j] = c == '#';
		}
	}
	
	/*
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++) printf("%d ", a[i][j]);
		printf("\n");
	}
	*/
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			if(a[i][j]){
				// 初始化位置信息
				maxi = mini = i,
				maxj = minj = j,
				cnt = 0;
				
				// 搜索
				dfs(i, j);
				int tot = (maxi-mini+1) * (maxj-minj+1);
				if(tot == cnt) ans++; // 一艘船
				else{
					printf("Bad placement.");
					return 0;
				}
			}
		}
	}
	printf("There are %d ships.", ans);
	return 0;
}
```


可以从我的微信名片上找到视频题解。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3ed64a1ea0734150ac8454c1a0a067b6.png)

