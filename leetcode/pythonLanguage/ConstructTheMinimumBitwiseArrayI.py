from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans =[]
        for num in nums:
            if(num%2==0):
                ans.append(-1)
            else:
                ans.append(num - ((num + 1) & (-num - 1)) // 2)
        return ans

solution= Solution()

print(solution.minBitwiseArray([2,3,5,7]))
print(solution.minBitwiseArray([11,13,31]))