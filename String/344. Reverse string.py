class Solution:
    def __init__(self, s):
        self.s = s

    def reverseString(self):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(self.s)
        for i in range(n//2):
            self.s[i], self.s[n-i-1] = self.s[n-i-1], self.s[i]
        return self.s


s = ['h', 'e', 'l', 'l', 'o']
sol = Solution(s)
print(sol.reverseString())
