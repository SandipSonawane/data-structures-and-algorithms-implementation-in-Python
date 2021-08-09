# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1, nums2):
        intersect = []
        for num in nums2:
            if num in nums1:
                intersect.append(num)
        return intersect


nums1 = [1,2,2,1]
nums2 = [2,2]

sol = Solution()
sol.intersect(nums1, nums2)