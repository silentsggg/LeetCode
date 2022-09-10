class Solution:
    # 此递归方法可以实现，不过leetcode提示超出递归最大深度
    # 在本地测试无问题
    # def generate(self, numRows: int) -> list[list[int]]:
    #     res = list()
    #     for i in range(numRows):
    #         res.append(self.triangle(i))
    #     return res

    # def triangle(self, n):
    #     # 基线条件
    #     if n == 1:
    #         return [1]

    #     return self.add_list([0]+self.triangle(n-1), self.triangle(n-1)+[0])

    # def add_list(self, lst1, lst2):
    #     res = list()
    #     len1 = len(lst1)
    #     len2 = len(lst2)

    #     if len1 <= len2:
    #         length = len1
    #     else:
    #         length = len2

    #     for i in range(length):
    #         res.append(lst1[i] + lst2[i])

    #     return res

    # # 利用错位相加的改进法，不使用递归
    # # 其中add_list()函数与递归中相同
    # def generate(self, numRows: int) -> list[list[int]]:
    #     res = list()
    #     if numRows == 1:
    #         return [[1]]
    #     temp = [1]
    #     res.append([1])
    #     for _ in range(2, numRows+1):
    #         temp = self.add_list([0]+temp, temp+[0])
    #         res.append(temp)
    #     return res

    # def add_list(self, lst1, lst2):
    #     res = list()
    #     length = len(lst1)
    #     # 判断列表长短，这里可以不要
    #     # len1 = len(lst1)
    #     # len2 = len(lst2)

    #     # if len1 <= len2:
    #     #     length = len1
    #     # else:
    #     #     length = len2

    #     for i in range(length):
    #         res.append(lst1[i] + lst2[i])

    #     return res

    # 大神解法
    # 注意zip()函数的用法
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res

if __name__ == '__main__':
    s1 = Solution()
    print(s1.generate(5))
