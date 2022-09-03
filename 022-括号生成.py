# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

class Solution:
    # 方法一：回溯法
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtracking(left, right, inputx):
            # 结束，添加进结果
            if left == n and right == n:
                res.append(inputx)
                return

            # 剪枝
            if right > left:
                return

            # 拼接有效的括号，递归
            if left < n:
                backtracking(left + 1, right, inputx + '(')

            if right < n:
                backtracking(left, right + 1, inputx + ')')

        backtracking(0, 0, '')
        return res

    # # 方法二，暴力法，找到所有的括号组合，去掉不符合的组合
    # def generateParenthesis(self, n: int) -> List[str]:
    #     def combin(arr):
    #         res = []
    #         def permutations(position, end):
    #             if position == end:
    #                 str2 = str(arr).replace('[', '').replace(']', '').replace(',', '').replace('\'', '').replace(' ', '')
    #                 if str2 not in res:
    #                     res.append(str2)
    #                     return
    #             else:
    #                 for index in range(position, end):
    #                     arr[index], arr[position] = arr[position], arr[index]
    #                     permutations(position + 1, end)
    #                     arr[index], arr[position] = arr[position], arr[index]  # 还原到交换前的状态，为了进行下一次交换

    #         permutations(0, len(arr))
    #         return res

    #     # 获得括号的所有组合
    #     arrx = list('(' * n + ')' * n)
    #     rec = combin(arrx)

    #     # 判断括号的有效性
    #     def fun(strx):
    #         stack = []
    #         for item in strx:
    #             if item == '(':
    #                 stack.append(item)
    #             elif not stack:
    #                 return False
    #             else:
    #                 stack.pop()
    #         return True if not stack else False

    #     resx = []

    #     for item in rec:
    #         if fun(item):
    #             resx.append(item)

    #     return resx