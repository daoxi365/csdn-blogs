![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/911c7e2557e54a6d9a9ac700551a6790.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_17,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi 
#include <iostream>
using namespace std;
int main(){
	for(int i=5;i>=1;i--){
		for(int j=i;j>=1;j--){
			cout<<"*";
		}
		cout<<endl;
	}
	for(int i=2;i<=5;i++){
		for(int j=1;j<=i;j++){
			cout<<"*";
		}
		cout<<endl;
	} 
	
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/6365483fc4ef4af097afd3aae521561e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
吐槽一下`astyle`，怎么给我整成这样了！

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main()
{
	for(int i=5; i>=1; i--) {
		for(int j=i; j>=1; j--) {
			cout<<"*";
		}
		cout<<endl;
	}
	for(int i=2; i<=5; i++) {
		for(int j=1; j<=i; j++) {
			cout<<"*";
		}
		cout<<endl;
	}

	return 0;
}
```

