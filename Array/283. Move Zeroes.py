class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[non_zeros] = num
                non_zeros += 1

        for i in range(non_zeros, len(nums)):
            nums[i] = 0

        print(nums)


nums = [2, 2, 2, 35, 0, 1, 0, 3, 12, 1, 2, 4, 53, 0, 3, 0, 34]
sol = Solution()
sol.moveZeroes(nums)