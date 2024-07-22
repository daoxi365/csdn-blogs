```cpp
//Author:PanDaoxi
#include <iostream>
using namespace std;

int main()
{
    cout << "请输入运算法则：";
    char x;
    cin >> x;
    int a,b;
    cout << "输入两个数字：";
    cin >> a >> b;

    int result;
    switch (x) {
        case '+':
            result = a + b;
            cout << result << endl;
            break;
        case '-':
            result = a - b;
            cout << result << endl;
            break;
        case '*':
            result = a * b;
            cout << result << endl;
            break;
        case '/':
            if (b != 0) {
                result = a / b;
                cout << result << endl;
                break;
            } else {
                cout << "Divided by 0!" << endl;
                break;
            }
        default:
            cout << "Invalid Operator!" << endl;
            break;
    }

    return 0;
}
```

