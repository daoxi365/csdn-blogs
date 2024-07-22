![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/e3e4071b635c43d150830a7de4128749.png)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int queue[1001];
int index=0;
void output(){
	for(int i=0;i<index;i++) cout<<queue[i]<<" ";
	cout<<endl;
}
void step(int n){
	if(n==0){
		output();
		return;
	}
	queue[index++]=1;
	step(n-1);
	--index;
	if(n>1){
		queue[index++]=3;
		step(n-2);
		--index;
	}
}
int main(){
	int n;
	cin>>n;
	step(n);
	return 0;
}
```

