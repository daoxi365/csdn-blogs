# 数池塘（四方向）
## 题目描述
农夫约翰的农场可以表示成$N \times M$（$1\le N\le 100\le M\le100$）个方格组成的矩形。由于近日的降雨，在约翰农场上的不同地方形成了池塘。每一个方格或者有积水（`'W'`）或者没有积水（`'.'`）。农夫约翰打算数出他的农场上共形成了多少池塘。一个池塘是一系列相连的有积水的方格，每一个方格周围的四个方格都被认为是与这个方格相连的。现给出约翰农场的图样，要求输出农场上的池塘数。

## 输入
第 $1$ 行：由空格隔开的两个整数：$N$ 和 $M$ 。
第 $2..N+1$ 行：每行M个字符代表约翰农场的一排方格的状态。每个字符或者是'W'或者是`'.'`，字符之间没有空格。

## 输出
输出只有 $1$ 行，输出约翰农场上的池塘数。

## 样例输入

```cpp
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
```

## 样例输出

```cpp
13
```
## 代码

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int inf = 101;
bool a[inf][inf];
int n, m, ans;
int fx[6] = {inf, 0, 1, 0, -1},
	fy[6] = {inf, 1, 0, -1, 0};
void dfs(int x, int y){
	if(!a[x][y]) return; // 没水了，结束
	a[x][y] = false;     // 抽当前位置的水
	for(int i=1; i<=4; i++){
		int xx = x + fx[i], yy = y + fy[i]; // 记录方向
		if(xx >= 1 && xx <= n && yy >= 1 && yy <= m && a[xx][yy]){
			dfs(xx, yy); // 搜
		}
	}
}
int main(){
	cin >> n >> m;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			char ch;
			cin >> ch;
			a[i][j] = ch == 'W'; // 读入
		}
	}
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			if(a[i][j]){
				dfs(i, j);
				ans++; // 水池数++
			}
		}
	}
	cout << ans;
	return 0;
}
```

走出迷宫的最少步数
题目描述
一个迷宫由$R$行$C$列格子组成，有的格子里有障碍物，不能走；有的格子是空地，可以走。
给定一个迷宫，求从左上角走到右下角最少需要走多少步(数据保证一定能走到)。只能在水平方向或垂直方向走，不能斜着走。

输入
第一行是两个整数，R和C，代表迷宫的行数和列数。（ $1\le  R，C \le 40$)
接下来是R行，每行C个字符，代表整个迷宫。空地格子用'.'表示，有障碍物的格子用`'#'`表示。迷宫左上角和右下角都是`'.'`。

输出
输出从左上角走到右下角至少要经过多少步（即至少要经过多少个空地格子）。计算步数要包括起点和终点。

## 样例输入

```cpp
5 5
..###
#....
#.#.#
#.#.#
#.#..
```

## 样例输出

```cpp
9
```

## 代码

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int inf = 41;
bool a[inf][inf];
int fx[6] = {inf, 0, 1, 0, -1},
	fy[6] = {inf, 1, 0, -1, 0},
	p[inf][inf], n, m;
void dfs(int x, int y, int k=1){
	p[x][y] = k;
	for(int i=1; i<=4; i++){
		int xx = x + fx[i], yy = y + fy[i];
		// a[i][j] 为 true 有路
		if(xx >= 1 && xx <= n && yy >= 1 && yy <= m && k+1 < p[xx][yy]){
			dfs(xx, yy, k+1);
		}
	}
}
int main(){
	cin >> n >> m;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			char ch;
			cin >> ch;
			a[i][j] = ch == '.';
			p[i][j] = INT_MAX;
		}
	}
	dfs(1, 1);
	cout << p[n][m];
	return 0;
}
```
附赠BFS解法：

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
int a[101][101], q[10001][3],
	n, m, num=1, h=1, t=1,
	fx[5] = {0, 0, 1, 0, -1},
	fy[5] = {0, 1, 0, -1, 0};
int main(){
	cin >> n >> m;
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			char q;
			cin >> q;
			if(q == '#') a[i][j] = 114514;
		}
	}
	a[1][1] = q[t][1] = q[t][2] = q[t][3] = 1;
	while(h <= t){
		for(int i=1; i<=4; i++){
			int xx = q[h][1] + fx[i],
				yy = q[h][2] + fy[i],
				ss = q[h][3] + 1;
			if(xx >= 1 && xx <= n && yy >= 1 && yy <= m && a[xx][yy] == 0){
				t++,
				num++,
				a[xx][yy] = num,
				q[t][1] = xx,
				q[t][2] = yy,
				q[t][3] = ss;
				if(xx == n && yy == m){
					cout << ss;
					return 0;
				}
			}
		}
		h++;
	}
	/*debug
	for(int i=1; i<=n; i++){
		for(int j=1; j<=m; j++){
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}
	*/
	return 0;
}
```

