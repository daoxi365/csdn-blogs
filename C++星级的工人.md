![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/b5c37f2e21974a9a8a8511054063ec67.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/9a5b3fe54bde4d00a4f0580be53e98ff.png)

```cpp
//Author:PanDaoxi
#include <iostream>
#include <algorithm> 
using namespace std;
int wk[10001],od[10001],wk_num[10001],od_num[10001];
int m,n; //m=工作项数 n=工作人数 
int main(){
	bool flag=false; //开关
	cin>>m>>n;
	for(int i=1;i<=m;i++){
		cin>>od[i];
	} 
	for(int j=1;j<=n;j++){
		cin>>wk[j];
	}
	//排序
	sort(od+1,od+m+1); 
	sort(wk+1,wk+n+1);
	int sum=0,cnt=1; //sum=总开销
	for(int i=1;i<=n;i++){
		if(wk[i]>=od[cnt]){
			sum+=wk[i];
			od_num[cnt]=od[cnt];
			wk_num[cnt]=wk[cnt];
			cnt++;
		}
		if(cnt==m+1){
			flag=true;
			break;
		}
	} 
	if(!flag) cout<<"failed"<<endl;
	else{
		cout<<sum<<endl;
		for(int i=1;i<cnt;i++){
			cout<<od_num[i]<<" "<<wk_num[i]<<endl;
		}
	}
	return 0;
} 
```

