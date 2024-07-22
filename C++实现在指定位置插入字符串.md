```cpp
#include <iostream> 
#include <cstring>
using namespace std;

int main(){
	char a[101],b[101];
	int l,n,i;
	cin>>a>>n>>b;
	l=strlen(a);
	cout<<l<<endl;
	for(i=0;i<=l;i++){
		if(a[i]=='a'){
			cout<<i+1<<endl;
			break;
		}
	}
	for(i=0;i<n-1;i++) cout<<a[i];
	cout<<b;
	for(i=n-1;i<l;i++) cout<<a[i];
	return 0;
}
```

