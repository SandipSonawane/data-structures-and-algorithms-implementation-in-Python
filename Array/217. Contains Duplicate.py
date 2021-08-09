# 217. Contains Duplicate

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def containsDuplicate(self):
        visited = set()
        for num in self.nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False


sol = Solution([1, 2, 3])
sol.containsDuplicate()