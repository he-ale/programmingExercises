from typing import List
class Solution:

    def repeatedNTimes(self, nums: List[int]) -> int:
        register= {}
        for num in nums:
            if register.get(num)!=None:
                return num
            register[num]= 1;

solution= Solution()
print(solution.repeatedNTimes([1,2,3,3]))
