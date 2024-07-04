#include <iostream>
#include <cmath> 
using namespace std;

class shape { // 形状类
public:
    double getArea() { // 求面积
        return -1;
    }
    double getPerimeter() { // 求周长
        return -1;
    }
};

const double PI = 3.14159265358979323846;

class RegularPolygon : public shape {
private:
    int n; 
    double s; 
public:
    RegularPolygon(int numSides, double sideLength) : n(numSides), s(sideLength) {}

    double getArea() {
        return n*s*s/(4*tan(PI/n)); 
    }

    double getPerimeter() {
        return n * s;
    }
}; 

int main() {
    int n;
    double s;
    
    cin >> n >> s;
    RegularPolygon p(n, s);
    cout << p.getArea() << endl;
    cout << p.getPerimeter() << endl;

    return 0;
}