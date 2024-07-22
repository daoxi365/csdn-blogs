![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/864dbe51b934e927bb356da14a1adbf0.png)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
void move(int n,char x,char z,char y){
	//n片圆盘，x为源柱，z为目标柱，y为过渡柱 
	if(n==0) return;
	// 将n-1片圆盘从x柱移至y柱 
	move(n-1,x,y,z);
	cout<<x<<"=>"<<z<<endl;
	move(n-1,y,z,x);
} 
int main(){
	int n;
	cin>>n;
	move(n,'x','z','y');
	return 0;
}
```

