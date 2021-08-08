# 189. Rotate Array

class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def rotate(self):
        move_to_front = nums[len(nums)-self.k:]

        for i in range(1, len(nums)-k+1):
            nums[len(nums)-i] = nums[len(nums)-i-k]
        for i in range(len(move_to_front)):
            nums[i] = move_to_front[i]
        print(nums)
        return nums


nums = [-1,-100,3,99]
k = 2
sol = Solution(nums, k)
sol.rotate()