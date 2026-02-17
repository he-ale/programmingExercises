class Solution:

    def sumTwo(self, nums, target):
        numbers= {}
        for index, num in enumerate(nums):
            if num in numbers:
                return [numbers[num], index]
        
            numbers[target-num]= index

solution= Solution()
print(solution.sumTwo(nums = [2,7,11,15], target = 9))
print(solution.sumTwo(nums = [3,2,4], target = 6))