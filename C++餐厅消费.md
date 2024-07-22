![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7d4bf88c69624a37a95f7ae192d4708a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
直接暴力穷举！
```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	for(int i=1;i<=30;i++){
		for(int j=1;j<=30;j++){
			for(int k=1;k<=30;k++){
				if(i+j+k==30&&i*30+j*20+k*10==500){
					cout<<i<<" "<<j<<" "<<k<<endl;
				}
			}
		}
	}
	return 0;
} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/e38300b85669440098acbc9f0c287aab.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

