#include <iostream>
#include <cmath>

class Solution {
public:
    double myPow(double x, int n) {
        double result= pow(x, n);
        return result;
    }
};

int main(int argc, char const *argv[])
{
    Solution solution;
    double result= solution.myPow(2.10000, 3);
    std::cout << result <<std::endl;
    return 0;
}
