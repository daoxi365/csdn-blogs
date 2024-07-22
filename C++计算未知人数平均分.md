![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210712154715755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	// 因为使用do while循环所以人数要改成-1，while循环就是0
	double sum,men = -1,score; 
	do {
		cin >> score;
		sum += score;
		men ++;
	} while (score != 0);
	double avg = (sum / men);
	cout << avg << endl;
	return 0;
} 
```

