class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        list1 = nums1+nums2
        list1.sort()
        n = len(list1)
        if n % 2 == 1: return list1[n//2]
        return (list1[n//2] + list1[(n//2) - 1])/2.0

sol = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
result = sol.findMedianSortedArrays(nums1, nums2)
print(result)
