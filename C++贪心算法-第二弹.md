![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b0bae47f7eea4ce3b3bff2821fd5a5e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/59d4af388c704dcd90ff79195bb1349c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1f31c83e52fd4a35b34c7cf6906fa17d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/126fc13f941d4c389d9ca76a76957212.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4ce7fa7358ab4a2b9395fc5a0214f882.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <cmath> 
using namespace std;
int a1,a2,a3,a4,a5,a6,sum=0;
int main(){ 
	cin>>a1>>a2>>a3>>a4>>a5>>a6;
	sum=a4+a5+a6;
	sum+=ceil(a3/4.0); //向上取整
	a3%=4; //得到多余a3商品
	a1-=min(a1,a5*11); //a5商品：用a1填空 
	if(a2<a4*5){ //a4填空：2*2的地方 
		a1-=min(a1,(a4*5-a2)*4); 
	}
	a2-=min(a2,a4*5);
	//a3填空
	if(a3==3){ 
		if(!a2){
			a1-=min(a1,4); //先占2*2的位置  
		}
		a2-=min(a2,1);
		a1-=min(a1,5);
	} 
	if(a3==2){
		if(a2<3){
			a1-=min(a1,(3-a2)*4);
		}
		a2-=min(a2,6);
		a2-=min(a1,3);
	}
	if(a3==1){
		if(a2<5){
			a1-=min(a1,(5-a2)*4);
		}
		a1-=min(a1,7);
		a2-=min(a2,5);
	}
	sum+=ceil(a2/9.0);
	a2%=9;
	if(a2){ //a2箱子不为0 
		a1-=min(a1,(9-a2)*4);
	}
	sum+=ceil(a1/36);
	cout<<sum<<endl;
	return 0;
}
```

