class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s= s.strip()
        if len(s)==0:
            return True
        i, j= 0, len(s)-1
        while (j>i):
            if (not self.isValid(s[i])):
                i+=1
                continue
            
            if (not self.isValid(s[j])):
                j-=1
                continue
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True

    
    def isValid(self, c:str)->bool:
        return ('a'<=c <='z') or ('0'<=c<='9')

solution= Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome("A man, a plan, a canal: Panama"))