题目如下：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210703135530292.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
代码如下：

```cpp
//Author:PanDaoxi
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int x,y,min,max;
    cin >> y;
    cin >> x;
    min = x; // 最大值
    max = x; // 最小值
    double avg = x,z,sum; // 平均值
    z = double(y);   //记录个数
    sum = double(x); // 数字和
    y--;
    while (y--) {
        cin >> x;
        if (x > max) {
            max = x;
        }
        if (x < min) {
            min = x;
        }
        sum += x;
    }

    avg = sum / z;
    cout << max << endl;
    cout << min << endl;
    cout << fixed << setprecision(3) << avg << endl;
    return 0;
}
```
代码截图：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2021070313580092.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)
实现效果：
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210703135930441.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

