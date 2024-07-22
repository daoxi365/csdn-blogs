![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e24af2bfb85c4b6bb7e644ef615fc884.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/60911370bd7348919ba3b557fd4894c1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/d9287b0cad644702b4266f12eecf22a0.png)

```cpp
//Author:PanDaoxi
/*
#include <iostream> 
#include <cmath>
#include <vector>
#include <algorithm>
#include <functional>
*/
#include <bits/stdc++.h>
using namespace std;
double Length(double R,double b){
	return sqrt(R*R-b*b/4)*2; //求内接矩阵的长度 
}
int main(){
	int n;
	const double l=20,w=2;
	cin>>n;
	//处理n组数据
	while(n--){
		int m;
		double R;
		cin>>m;
		vector<double> Rs; //动态数组
		while(m--){
			cin>>R;
			Rs.push_back(R); //把R放入数组 
		} 
		sort(Rs.begin(),Rs.end(),greater<double>());
		double sum=0;
		int i;
		for(i=0;i!=Rs.size();i++){ //遍历动态数组长度 
			if(sum>l) break; //判断是否完全覆盖草坪
			sum+=Length(Rs[i],w); //计算内接矩阵的长度 
		}
		cout<<i<<endl;
	} 	
	return 0;
} 
```

