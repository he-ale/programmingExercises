from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=0
        i=0
        j=1
        while(j<len(nums)):   
            while(j<len(nums) and nums[i]==nums[j]):
                counter+=1
                j+=1

            i+=1
            if(i<len(nums) and j<len(nums)):
                nums[i]=nums[j]
            j+=1
        return len(nums)-counter

solution= Solution()
solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])