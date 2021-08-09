class Solution:
    def plusOne(self, digits):
        digits = reversed(digits)
        if digits[len(digits)-1] < 9:
            digits[len(digits)-1] = digits[len(digits)-1] + 1
        else:
            digits.insert(1, 0)
        return digits


sol = Solution()
print(sol.plusOne([1,9]))
