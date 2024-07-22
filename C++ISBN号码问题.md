![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719163055764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210719164555178.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[14];
	int b[10],sum=0,len,j=0;
	cin>>a;
	len=strlen(a);
	for(int i=0;i<len;i++){
		if(a[i]=='X') b[j++]=10;
		if(a[i]>='0'&&a[i]<='9') b[j++]=a[i]-'0';
	}
	for(int i=0;i<9;i++) sum+=b[i]*(i+1);
	if(sum%11==b[9]) cout<<"Right"<<endl;
	else{
		if(sum%11==10){
			for(int j=0;j<9;j++){
				if(j==0||j==3){
					cout<<"-";
					continue;
				}
				cout<<b[j];
			}
			cout<<"-X"
		}
		else{
			b[9]=sum%11;
			cout<<b[0]<<"-"<<b[1]<<b[2]<<b[3]<<"-"<<b[4]<<b[5]<<b[6]<<b[7]<<b[8]<<"-"<<b[9];
		}
	}
	return 0;
} 
```

