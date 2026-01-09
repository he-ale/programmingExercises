from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        register= {}
        for i in range(len(nums)):
            aux= target-nums[i]
            if(register.get(aux)!=None):
                return[register.get(aux), i]
            register[nums[i]]= i
        return []
    
solution= Solution()

print(solution.twoSum(nums = [2,7,11,15], target = 9))
print(solution.twoSum(nums = [3,2,4], target = 6))
print(solution.twoSum(nums = [3,3], target = 6))