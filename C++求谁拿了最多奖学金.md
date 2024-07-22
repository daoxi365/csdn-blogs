![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/4ad4c3e3158149fd86c643f9a7ef9a71.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct student{
	char name[21];
	int avg,review;
	char iswest,leader;
	int text,total;
}stu[101];
int main(){
	int n,sum=0,max=0,num=0;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>stu[i].name;
		cin>>stu[i].avg;
		cin>>stu[i].review;
		cin>>stu[i].leader;
		cin>>stu[i].iswest;
		cin>>stu[i].text;
	}
	for(int i=0;i<n;i++){
		if(stu[i].avg>80&&stu[i].text>=1) stu[i].total+=8000;
		if(stu[i].avg>85&&stu[i].review>80) stu[i].total+=4000;
		if(stu[i].avg>90) stu[i].total+=2000;
		if(stu[i].avg>85&&stu[i].iswest=='Y') stu[i].total+=1000;
		if(stu[i].avg>80&&stu[i].leader=='Y') stu[i].total+=850;
	}
	for(int i=0;i<n;i++){
		if(stu[i].total>max){
			max=stu[i].total;
			num=i;	
		}
	}
	cout<<stu[num].name<<endl;
	cout<<stu[num].total<<endl;
	for(int i=0;i<n;i++) sum+=stu[i].total;
	cout<<sum<<endl;
	return 0;
}
```
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/2435bed494774f47838ad878cb348375.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1BhbkRhb3hpMjAyMA==,size_16,color_FFFFFF,t_70)

