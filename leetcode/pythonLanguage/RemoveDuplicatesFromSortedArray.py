from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while(j<len(nums)):   
            while(j<len(nums) and nums[i]==nums[j]):
                print('ok')
                j+=1

            i+=1
            nums[i]=nums[j]
            j+=1
        print(nums)

solution= Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])