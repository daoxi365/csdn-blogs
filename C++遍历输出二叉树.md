![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/46fad83deca5480895ab86d75e8c3f0d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/1a49e7d1cb654ce0b82f7b36995b5735.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5r2Y6YGT54a5,size_20,color_FFFFFF,t_70,g_se,x_16)

```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;
struct node{
	int left,right; //左孩子和右孩子
	char value; //值 
}data[101];
int root=0,cnt; //根节点和记录有效字符
char ch; //输入的数据
//构建二叉树
int buildTree(int bt){ //参数：结点的编号 
	cin>>ch;
	if(ch=='.'){ //判断是否为空结点
		bt=0; //赋值为0 
		return bt; //跳出程序 
	} 
	else{ //非空结点，进行先序遍历 
		bt=++cnt; //构造结点 
		data[bt].value=ch; //存放根的值 
		data[bt].left=data[bt].right=0; //左右孩子都归零 
		data[bt].left=buildTree(bt); //递归左子树
		data[bt].right=buildTree(bt); //递归右子树 
	}
	return bt;  //完成递归 
} 
//后序遍历二叉树
void postorder(int bt){
	if(bt){ //非空结点 
		//递归输出根 
		postorder(data[bt].left);
		postorder(data[bt].right);
		cout<<data[bt].value;
	}
} 
//先序遍历
void preorder(int bt){
	if(bt){
		cout<<data[bt].value;
		preorder(data[bt].left);
		preorder(data[bt].right);
	}
} 
//中序遍历
void inorder(int bt){
	if(bt){
		inorder(data[bt].left);
		cout<<data[bt].value;
		inorder(data[bt].right);
	}
} 
int main(){
	root=buildTree(0); //构建二叉树 
	cout<<"后序：";
	postorder(root);
	cout<<endl<<"中序：";
	inorder(root);
	cout<<endl<<"先序：";
	preorder(root);
	cout<<endl; 
	return 0;
}
```

---

后来又学了一段时间，有一次考试我见到了这个题：
<https://www.luogu.com.cn/problem/P1305>

然后考场上瞬间高兴地发飙

```cpp
// Author:PanDaoxi
#include <bits/stdc++.h>
using namespace std;
const int inf = 27;
map <char, string> tree;
int n;
void f(char root){
	if(root == '*') return;
	cout << root;
	f(tree[root][0]);
	f(tree[root][1]);
}
int main(){
	char root;
	cin >> n;
	for(int i=1; i<=n; i++){
		char a, b, c;
		cin >> a >> b >> c;
		if(i == 1) root = a;
		tree[a] = string(1, b) + string(1, c);
	}
	f(root);
	return 0;
}
```
感觉这种方法更简单些，然后这个题 $ac$ 了。
![在这里插入图片描述](https://pic.2ge.org/cdn/?url=https://img-blog.csdnimg.cn/7e4e1327016f43b5bae0e32a4ac819e0.png)
一次过。
