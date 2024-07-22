![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/40b5f3bb9a7b453d84e89fc1d54c0dc6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/28371c9ac7844efeb5569688b4d12819.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/8174581d20b9432d80f706af63effbfe.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e7a678077ed347df8a3ae7d658f2c56a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2f45fade7c83475a99be84dcaedbae14.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/0e2e8770e09e4219b694a717cda09c97.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4f4e24ec891b4c07bfdb794c7e063541.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
<hr>

`f[i][j]`：**当前物品的最大价值.**
`max()`：求最大值.
`f[i-1][j]`：**没有放入第`i`件物品的最大价值.**
`f[i-1][j-w(i)]+c(i)`：**放入第`i`件物品的最大价值.**

综上，比较放入和不放入时物品的最大价值，放入时减少背包容量（`[j-w(i)]`），增加总价值（`+c(i)`）。

更形象的理解：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b9d114bdf1ca4f18bf2cdf593dc49e6f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9ec48085cce94038a68fadd937de4e7c.png)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/5147f0d0000049dcb0c8b98c4db5b867.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/981dd8e081954aa7b92188efdcb740a1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_14,color_FFFFFF,t_70,g_se,x_16)
所以，原来背包的可容纳重量会减少。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/19e00f7d098d456ca621198b485ee828.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_13,color_FFFFFF,t_70,g_se,x_16)
<hr>

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
// w=重量 c=价值 f=最优解 
int w[101],c[101],f[101][101];
int m,n; // m=背包可承受的最大重量 n=可以预估的物品重量及价值 
int main(){
	cin>>m>>n;
	//存入n件物品的重量及价值
	for(int i=1;i<=n;i++) cin>>w[i]>>c[i]; 
	//动态规划
	for(int i=1;i<=n;i++){ // n件物品 
		for(int j=1;j<=m;j++){ //最大承受量
		//判断当前物品是否可以放入到背包中
		if(j>=w[i]) f[i][j]=max(f[i-1][j],f[i-1][j-w[i]]+c[i]); //哪个价值大，我们要哪个
		else f[i][j]=f[i-1][j]; //否则就不放了			
		}
	} 
	cout<<f[n][m];
	return 0;
}
```


<hr>

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4c0badec00404712aef3cf06e7ff5909.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int w[101],c[101],f[101],m,n;
int main(){
	cin>>m>>n;
	for(int i=1;i<=n;i++) cin>>w[i]>>c[i];
	//动态规划：一维数组
	for(int i=1;i<=n;i++){
		for(int j=m;j>=0;j--){ //大包不能放入小包 
			if(j>=w[i]) f[j]=max(f[j],f[j-w[i]]+c[i]);			
		}
	} 
	cout<<f[m];
	return 0;
} 
```
理解如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/72e3e465b5fc4882b23d63e0eed55be7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

