![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210716162010285.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include<iostream>
using namespace std;

int main(){     
    int a[10][10];
    for(int i=0;i<10;i++){
    	for(int j=0;j<10-i;j++) cout<<" ";
    	for(int k=0;k<=i;k++){
    		if(k==0||k==i) a[i][k]=1;
    		else a[i][k]=a[i-1][k-1]+a[i-1][k];
    		cout<<a[i][k]<<" ";	
		}
		cout<<endl;
	}
	return 0;
} 
```

