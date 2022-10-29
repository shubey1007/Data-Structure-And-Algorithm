class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if(res in nums[i+1:]):
                return [i, nums[i+1:].index(res)+i+1]
        
