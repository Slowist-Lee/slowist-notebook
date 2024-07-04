#include<iostream>
using namespace std;
class MyClass {
public:
    MyClass(int x): val(x) {}
    void Print() const {cout << "const:val=" << val << '\t';}
    void Print() {cout << "val=" << val << '\t';}
private:
    int val;
};
int main() {
    const MyClass obj1(10);
    MyClass obj2(20);
    obj1.Print();
    obj2.Print();
    return 0;
}