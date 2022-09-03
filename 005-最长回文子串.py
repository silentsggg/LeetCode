class Solution:
    # # 字符串切片，暴力求解，时间复杂度O(n²)
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) == 1 or len(s) == 0:
    #         return s
    #     # lists = list(s)
    #     length = len(s)
    #     res = ''
    #     # reslen = 0
    #
    #     for i in range(length - 1):
    #         for j in range(length):
    #             # res = s[i:j]
    #             if self.fun(s[i:length-j+i]) and length-j != 1:
    #                 if len(s[i:length-j+i]) > len(res):
    #                     res = s[i:length-j+i]
    #
    #     return res if res else s[0]
    #
    # # 判断一个字符串是否为回文字符串
    # def fun(self, strc):
    #     length = len(strc)
    #     # if length == 0 or length == 1:
    #     #     return True
    #     # 入栈
    #     lst = list(strc)
    #     lstr = lst[::]
    #     lst.reverse()
    #     return lst == lstr

    # 中心扩散，个人版
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        length = len(s)
        res = ''
        for index in range(length):
            rx = True
            ry = True
            l = index - 1
            r = index + 1
            while rx or ry:
                # print('l=',l)
                if l >= 0:
                    if s[l] == s[index]:
                        l -= 1
                    else:
                        rx = False
                else:
                    rx = False
                # print('r=', r)
                if r < length:
                    if s[r] == s[index]:
                        r += 1
                    else:
                        ry = False
                else:
                    ry = False

            # rl = True
            # ry = True
            while True:
                if l >= 0 and r < length:
                    if s[l] == s[r]:
                        l -= 1
                        r += 1
                    else:
                        break
                else:
                    break

            if len(s[l + 1: r]) > len(res):
                res = s[l + 1: r]
        return res if res else s[0]


if __name__ == '__main__':
    s1 = Solution()
    strc1 = 'accabacce'
    strc2 = 'baba'
    print(s1.longestPalindrome(strc1))
