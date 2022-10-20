class Solution:
    def twoSum(self, nums, target):
        memo = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in memo:
                return [memo[complement], i]
            memo[nums[i]] = i

def test_case():
    sol = Solution()
    nums = [2,7,11,15]
    target = 9

    expected = [0,1]

    got = sol.twoSum(nums, target)
    assert got == expected

if __name__ == '__main__':
    test_case()