class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # s= s[::-1] 이렇게 했는데 안됐음.

        s.reverse()
s = ['a','b','c','d']
a = Solution()

a.reverseString(s)