class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        an= set(s)
        for i in an:
            if(s.count(i)!=t.count(i)):
                return False
            
        return True
    
solution= Solution()

print(solution.isAnagram(s = "anagram", t = "nagaram"))
print(solution.isAnagram(s = "rat", t = "car"))