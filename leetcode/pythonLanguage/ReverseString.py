from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        iMax=len(s)-1
        iMin=0
        while iMin<iMax:
            aux= s[iMax]
            s[iMax]=s[iMin]
            s[iMin]=aux
            iMin+=1
            iMax-=1
        return s

solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))
print(solution.reverseString(["H","a","n","n","a","h"]))