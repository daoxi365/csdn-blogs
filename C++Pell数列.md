![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/3fa78e2e26cc4ecaa1ac28736e7486b2.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include<cstdio>  
#include<cmath>  
#include<cstring>  
#include<algorithm>  
#include<iostream>  
using namespace std;  
long long b[1000010];  
long long r[1000010]; 
long long pell(int n){  
    if(n<3) return n;  
    if(b[n]==0) b[n]=(2*pell(n-1)+pell(n-2))%100000; 
    return (b[n]%32767);  
}
int main(){  
    int n,x;  
    cin>>n;  
    for(int i=1;i<=n;i++){  
        cin>>x;  
        r[i]=pell(x);  
    }  
    for(int j=1;j<=n;j++){
        cout<<r[j]<<endl;
    }
} 
```

