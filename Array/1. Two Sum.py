class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        mapped = {}

        for i, num in enumerate(self.nums):
            difference = self.target - num
            if difference in mapped:
                return [mapped[difference], i]
            else:
                mapped[num] = i


sol = Solution(nums=[3, 2, 4], target=6)
print(sol.twoSum())
