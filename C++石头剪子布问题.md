![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720144017777.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
由于需要判断各类情况，代码有些复杂，如下：
```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int n,x[101],y[101];
	string a,b;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>a>>b;
		if(a=="Rock") x[i]=0;
		else if(a=="Scissors") x[i]=1;
		else if(a=="Paper") x[i]=2;
		if(b=="Rock") y[i]=0;
		else if(b=="Scissors") y[i]=1;
		else if(b=="Paper") y[i]=2;
	}
	for(int i=0;i<n;i++){
		if(x[i]==0){
			if(y[i]==0) cout<<"Tie"<<endl;
			else if(y[i]==1) cout<<"Player 1"<<endl;
			else cout<<"Player 2"<<endl;
		}
		else if(x[i]==1){
			if(y[i]==0) cout<<"Player 2"<<endl;
			else if(y[i]==1) cout<<"Tie"<<endl;
			else if(y)cout<<"Player 1"<<endl;
		}
		else if(x[i]==2){
			if(y[i]==0) cout<<"Player 2"<<endl;
			else if(y[i]==1) cout<<"Player 1"<<endl;
			else cout<<"Tie"<<endl;
		}
	}
	return 0;
}
```

