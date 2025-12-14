class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        invertedNumber= 0;
        num=x
        while num>0:
            invertedNumber= (invertedNumber*10)+(num%10)
            num //=10
        return x==invertedNumber
    
solution= Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))