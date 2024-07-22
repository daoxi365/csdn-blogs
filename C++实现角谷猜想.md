> 好久没有写文章了，如果大家想看我继续更新，请看我的`bilibili`<a href="http://topurl.cn/pdxbz">《潘道熹的视频》</a>；如果需要文件，请看我的`Coding`仓库<a href="http://topurl.cn/pdxgit">《潘道熹的仓库》</a>。感谢！

今天我们来看一道题目：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210703131127580.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
题目要求我们使用`C++`语言完成。分析题目后我们可得知要用到`while`语句，代码如下：

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;

int main()
{
    int x,y;
    cout << "输入一个正整数："; // 请求用户输入
    cin >> x;
    y = x;

    if (x > 1) {
        while (x / 2) {
            if (x % 2 == 0) {
                x /= 2;
                cout << y << "/2=" << x << endl;
            } else {
                x *= 3;
                x += 1;
                cout << y << "*3+1=" << x << endl;
            }

            if (x > 1 && y > 1) {
                y = x / 2;
                cout << x << "/2=" << y << endl;
                x /= 2;
            }
        }
        cout << "End" << endl;
    } else {
        cout << "End" << endl;
    }
    return 0;
}
```
代码截图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2021070313202867.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)


实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210703131841917.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
<hr>

于2022年2月22日更新：
递归也可以这样写：

```cpp
// Author:PanDaoxi
#include <iostream>
using namespace std;
int f(int n){
	if(n==1) return 0;
	if(n%2){
		cout<<endl<<n<<"*3+1="<<3*n+1;
		return f(3*n+1);	
	}
	else{
		cout<<endl<<n<<"/2="<<n/2;
		return f(n/2);
	}	
}
int main(){
	int n;
	cin>>n;
	f(n);
	return 0;
}
 
```

