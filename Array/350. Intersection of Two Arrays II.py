# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1, nums2):
        intersect = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return intersect


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sol = Solution()
print(sol.intersect(nums1, nums2))