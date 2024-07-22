![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/1474f379dd299757cfd7be14caf322b2.png)（需要文件`in.txt`和`out.txt`，`in.txt`包含内容`0 1 2 3 4 5`，`out.txt`为空文件）
```cpp
#include <cstdio>
#include <iostream> 
using namespace std;

int main(){
	freopen("in.txt","r",stdin);   //设置输入为读取文件 
	freopen("out.txt","w",stdout); //设置输出为写入文件 
	int temp=0,sum=0;
	while(cin>>temp) sum+=temp; //读取文件并计算和 
	cout<<sum<<endl; //保存在文件中 
	fclose(stdin);  //关闭输入重定向
	fclose(stdout); //关闭输出重定向
	return 0;
} 
```

