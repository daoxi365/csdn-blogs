![=](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/f58c2437c5ef4bb685a8b60a09951eb4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
struct person{
	char name[10001];
	int time;
}p[101];
int islong(person a,person b){
	return a.time<b.time;
}
int main(){
	int n,k;
	cin>>n>>k;	
	for(int i=0;i<n;i++) cin>>p[i].name>>p[i].time;
	sort(p,p+n,islong);
	for(int i=1;i<=n;i++) if(i==k) cout<<p[i-1].name<<endl;
} 
```

