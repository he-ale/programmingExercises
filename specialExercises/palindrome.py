class Solution:

    def palindrome(self, s: str):
        i= 0
        j= len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    
solution= Solution()

print(solution.palindrome('abba'))
print(solution.palindrome('abcba'))