#include "iostream"
#include "cstdlib"

int mcd(int dividend, int divisor){
    dividend= (dividend<0)?-dividend:dividend;
    divisor= (divisor<0)? -divisor: divisor;
    if (divisor==0){
        return dividend;
    }
    return mcd(divisor, dividend%divisor);
}

int iterativeMcd(int dividend, int divisor){
    dividend= abs(dividend);
    divisor= abs(divisor);
    while (divisor!=0)
    {
        int temp= dividend%divisor;
        dividend= divisor;
        divisor= temp;
    }
    return dividend;
}

int main(int argc, char const *argv[])
{
    int result= mcd(48, 18);
    std::cout<< result <<std::endl; 
    
    result= iterativeMcd(15, 25);
    std::cout<< result <<std::endl; 
    return 0;
}


