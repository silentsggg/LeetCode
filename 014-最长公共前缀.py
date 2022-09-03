# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

class Solution:
    # # 方法一，横向比较
    # # 1. 找到strs中的最短字符串
    # # 2. 判断最短字符串是否等于其他两个字符串的前k个字符串，k=最短字符串长度-1
    # # 3. 判断最短字符串的长度-1的情况
    # # 4. 判断最短字符串的长度-2的情况
    # # 5. 直到最短字符串长度为0

    #     def longestCommonPrefix(self, strs):

    #         # 找出最短字符串
    #         strmin = strs[0]
    #         for item in strs:
    #             if len(item) <= len(strmin):
    #                 strmin = item

    #         # 判断公共前缀
    #         for i in range(len(strmin)):
    #             str1 = strmin[:len(strmin) - i]
    #             for j in range(len(strs)):
    #                 item1 = strs[j][:len(str1)]
    #                 if str1 != item1:
    #                     break
    #                 if j == len(strs) - 1:
    #                     return str1
    #                 else:
    #                     continue
    #         # 不存在公共前缀
    #         return ''

    # 方法二，纵向比较
    # 依次比较strs中的字符串的每一列，如果相同则进入下一列，直到有不同的，然后输出最后一次获得的结果
    def longestCommonPrefix(self, strs):
        if strs == '':
            return ''

        strmin = strs[0]
        for item in strs:
            if len(item) <= len(strmin):
                strmin = item

        length = len(strmin)
        # start = strs[0]
        res = ''
        for index in range(length):
            for i in range(len(strs)):
                if strs[0][index] == strs[i][index]:
                    if i == len(strs) - 1:
                        res = res + strs[0][index]
                    else:
                        continue
                else:
                    return res
        return res