![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/dbd517dba4fc1b2256c9d3e986141b09.png)

```cpp
#include <iostream>
#include <cstring>
using namespace std;
struct student{
	string name="";
	int chinese=0,math=0;
	double avg=0.0;
}stu[101];

int main(){
	int n;
	double sum=0.0,a=0.0;
	cin>>n;
	int x=n;
	for(int i=0;i<n;i++){
		cin>>stu[i].name;
		cin>>stu[i].chinese;
		cin>>stu[i].math;
		stu[i].avg=(stu[i].chinese+stu[i].math)/2.0;
	}
	for(int i=0;i<n;i++) sum+=stu[i].avg;
	a=sum/n;
	for(int i=0;i<n;i++){
		if(stu[i].avg<a) cout<<stu[i].name<<" "<<stu[i].chinese<<" "<<stu[i].math<<" "<<stu[i].avg<<endl;
		else x--;
	}
	if(x==0) cout<<"none"<<endl;
	return 0;
} 
```

