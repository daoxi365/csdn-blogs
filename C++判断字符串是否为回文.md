![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720142043320.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
中国的文化博大精深，有许多这样的对联：

> 雾锁山头山锁雾，天连水尾水连天
> 客上天然居，居然天上客
> 人过大佛寺，寺佛大过人
> 邻居爱我爱居邻，鱼傍水活水傍鱼
> 僧游云隐寺，寺隐云游僧

针对这道题，我的思路是：创建字符串`a`、`b`，将输入字符串`a`遍历，然后`b[i]=a[a长度-(1+i)]`，最后对比两个字符串是否相同。

比较两个字符串是否相同，我们可以使用`strcmp`函数，其返回值如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720143146684.png)


代码如下：
```cpp
#include <iostream>
#include <cstring>
using namespace std;

int main(){
	char a[101],b[101];
	int k=0;
	cin.getline(a,101);
	for(int i=0;i<strlen(a);i++){
		b[k++]=a[i];
	}
	if(strcmp(a,b)==0) cout<<"Yes"<<endl;
	else cout<<"No"<<endl;
	return 0;
} 
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210720143730518.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
汉字也可以！
