class Solution:
    def plusOne(self, digits):
        ls = len(digits)
        for index in reversed(range(ls)):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
        digits.insert(0, 1)
        return digits


sol = Solution()
print(sol.plusOne([1,9]))
