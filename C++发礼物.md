![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e1c191e80c034bedafb72abf237e9b21.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/89d8b2ca68d044b5834067d0a0d91579.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm>
using namespace std;
int a[10001],max_,n,cnt=0;
int main(){
	cin>>max_>>n; //最大价值和数量
	for(int i=1;i<=n;i++){
		cin>>a[i];
	} 
	sort(a+1,a+n+1);
	int flag=1; //最小价值物品
	for(int i=n;i>=flag;i--){
		if(a[i]+a[flag]<=max_){
			cnt++;
			flag++;
		}
		else{
			cnt++;
		}
	} 
	cout<<cnt;
	return 0;
}
```
更多题目，敬请期待新文章：动态规划。
