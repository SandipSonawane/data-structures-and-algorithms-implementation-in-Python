# 136. Single Number

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def singleNumber(self):
        nums_dict = {}
        for i in self.nums:
            try:
                nums_dict[i] += 1
            except:
                nums_dict[i] = 1
        for i in self.nums:
            if nums_dict[i] == 1:
                return i


sol = Solution([4, 1, 2, 1, 2])
sol.singleNumber()
