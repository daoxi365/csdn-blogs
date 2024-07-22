![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/20210713141823566.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
#include <iostream>
using namespace std;

int main(){
	double score = 0,min = 101,max = -1,sum = 0;
	for (int i = 1;i <= 10;i ++){
		cin >> score;
		sum += score;
		if (score < min){
			min = score;
		}
		if (score > max){
			max = score;
		}
	}
	double avg = (sum - max - min) / 8;
	cout << avg << endl;
	return 0;
} 
```

