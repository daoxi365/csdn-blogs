![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/277f49d7ee0044582ee8bbde1e2ced42.png)

```cpp
#include <iostream>
using namespace std;

int rabbit(int month){
	int num=0;
	if(month<=2) num=1;
	else num=rabbit(month-1)+rabbit(month-2);
	return num;
} 
int main(){
	cout<<rabbit(12);
}
```

