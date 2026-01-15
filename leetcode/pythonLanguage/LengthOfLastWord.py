class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        i= len(s)-1
        counter = 0
        while( i>=0 and s[i]==' '):
            i-=1

        while( s[i]!=' ' and i>=0):
            counter+=1
            i-=1

        return counter
    
solution= Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))