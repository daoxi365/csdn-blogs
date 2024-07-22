![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b7c2dfa379994aea8dba684ada17e673.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
我写的：

```cpp
```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
	int q[101]={},front=0,rear=0,n=0;
	char t,a[101];
	for(int i=0;cin>>t;i++){
		if(t=='O'){
			if(front>=rear) cout<<"None"<<endl;
			else cout<<q[front++]<<endl;
		}
		if(t=='I') cin>>q[++rear];
	}
	return 0;
} 
```
正确答案：

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
int main(){
    int q[101]={};
    int head ,tail;
    head = tail = 0;
    char ch;
    while(cin >> ch){
        if(ch == 'O'){
            if (head >= tail)
                cout<<"None"<<endl;
            else {
                cout<<q[head]<<endl;
                head++;
            }
        }
        if(ch == 'I'){
            tail++;
            cin >> q[tail];
        }
    } 
    return 0;
}
```

