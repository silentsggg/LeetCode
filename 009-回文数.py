# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]