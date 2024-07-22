![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/51ebf7667ee95b0feb0df83147115da8.png)
要用到结构体：
```cpp
#include <iostream>
using namespace std;
struct student{
	string name;
	int chinese,math,total;
}stu[101]; 
int main(){
	int n,max=0,num=0;
	cin>>n;
	for(int i=0;i<n;i++) {
		cin>>stu[i].name; 
		cin>>stu[i].chinese;
		cin>>stu[i].math;
		stu[i].total=stu[i].chinese+stu[i].math;
	}
	for(int i=0;i<n;i++){
		if(stu[i].total>max){
			max=stu[i].total;
			num=i;
		}
	}
	cout<<stu[num].name<<" "<<stu[num].chinese<<" "<<stu[num].math<<" "<<stu[num].total<<endl;
	return 0;
} 
```
或（其实是一样的）：
```cpp
#include <iostream>
using namespace std;struct student{string name;int chinese,math,total;}stu[101]; int main(){int n,max=0,num=0;cin>>n;for(int i=0;i<n;i++){cin>>stu[i].name;cin>>stu[i].chinese;cin>>stu[i].math;stu[i].total=stu[i].chinese+stu[i].math;}for(int i=0;i<n;i++){if(stu[i].total>max）{max=stu[i].total;num=i;}}cout<<stu[num].name<<" "<<stu[num].chinese<<" "<<stu[num].math<<" "<<stu[num].total<<endl;return 0;} 
```

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/img_convert/be63d5217437cf317e8fbf496af9c8dc.png)

