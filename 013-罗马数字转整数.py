class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = dictr[s[0]]
        for i in range(1, len(s)):
            if dictr[s[i]] > dictr[s[i - 1]]:
                sum = sum - dictr[s[i - 1]] * 2 + dictr[s[i]]
            else:
                sum += dictr[s[i]]

        return sum