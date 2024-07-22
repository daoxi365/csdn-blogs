![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719141618822.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
思路：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719142711442.png)
```cpp
#include<iostream>
using namespace std;
int main()
{
	int n,m,cnt=0;
	char a[101][101];
	cin>>n>>m;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cin>>a[i][j];
		}
	}
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(a[i][j]!='*') {
				if(a[i-1][j-1]=='*') cnt++;
				if(a[i-1][j]=='*') cnt++;
				if(a[i-1][j+1]=='*') cnt++;
				if(a[i][j-1]=='*') cnt++;
				if(a[i][j+1]=='*') cnt++;
				if(a[i+1][j-1]=='*') cnt++;
				if(a[i+1][j]=='*') cnt++;
				if(a[i+1][j+1]=='*') cnt++;
				cout<<cnt;
				cnt=0;
			} else cout<<"*";
		}
		cout << endl;
	}
	return 0;
}
```

