# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        res = []
        maxlen = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            res.clear()
            res.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in res:
                    res.append(s[j])
                else:
                    break
            if len(res) >= maxlen:
                maxlen = len(res)

        return maxlen