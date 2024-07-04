/*
1、声明一个复数类Complex（类私有数据成员为double型的real和image）
2、定义构造函数，用于指定复数的实部与虚部。
3、定义取反成员函数，调用时能返回该复数的相反数（实部、虚部分别是原数的相反数）。
4、定义成员函数Print()，调用该函数时，以格式(real, image)输出当前对象。
5、编写加法友元函数，以复数对象c1，c2为参数，求两个复数对象相加之和。
6、主程序实现：
（1）读入两个实数，用于初始化对象c1。
（2）读入两个实数，用于初始化对象c2。
（3）计算c1与c2相加结果，并输出。
（4）计算c2的相反数与c1相加结果，并输出。
c1|2.5 3.7
c2|4.2 6.5
输出共三行:
第一行是c1与c2之和；
第二行是c2的相反数与c1之和；
第三行是c2 。
(6.7, 10.2)
(-1.7, -2.8)
(4.2, 6.5)
*/
#include <iostream>
using namespace std;

class Complex { // 形状类
private:
    double real; //实部
    double image; //虚部
public:
    Complex(double r = 0, double i = 0) : real(r), image(i) {} //构造
    double Xor() { // 取反
        return -real;
    }
    char *Print() { //输出当前对象
        return "-1";
    }
};

//实在懒得写了，这是半成品，等我暑假学一遍c++





int main() {
    int n;
    double s;
    
    cin >> n >> s;
    RegularPolygon p(n, s);
    cout << p.getArea() << endl;
    cout << p.getPerimeter() << endl;

    return 0;
}


//标答

#include <iostream>
using namespace std;

class Complex {
private:
    double real;
    double image;

public:
    // 构造函数
    Complex(double r = 0, double i = 0) : real(r), image(i) {}

    // 取反成员函数
    Complex negate() const {
        return Complex(-real, -image);
    }

    // 成员函数Print()，用于输出复数
    void Print() const {
        cout << "(" << real << ", " << image << ")" << endl;
    }

    // 友元函数，用于复数加法
    friend Complex add(const Complex &c1, const Complex &c2);
};

// 友元函数实现复数加法
Complex add(const Complex &c1, const Complex &c2) {
    return Complex(c1.real + c2.real, c1.image + c2.image);
}

int main() {
    double real1, image1, real2, image2;

    // 读入两个实数，用于初始化对象c1
    cin >> real1 >> image1;
    Complex c1(real1, image1);

    // 读入两个实数，用于初始化对象c2
    cin >> real2 >> image2;
    Complex c2(real2, image2);

    // 计算c1与c2之和，并输出
    Complex sum = add(c1, c2);
    sum.Print();

    Complex neg_c2 = c2.negate();
    Complex sum_with_neg_c2 = add(c1, neg_c2);
    sum_with_neg_c2.Print();

    // 输出c2
    c2.Print();

    return 0;
}



