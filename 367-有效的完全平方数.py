# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true，否则返回false
# 不要使用任何内置的库函数，如sqrt

class Solution:
    # # O(n)解法
    # def isPerfectSquare(self, num: int) -> bool:
    #     i = 1
    #     while i*i < num:
    #             i += 1

    #     return i*i == num

    # O(logn)解法，二分查找
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 4:
            return num == 4 or num == 1 or num == 0

        start = 3
        # 当整数n大于4时，其开方数n^1/2小于n/2，利用这个可以将二分查找范围缩小一半
        end = int(num / 2)

        while start <= end:
            mid = int((start + end) / 2)
            if mid ** 2 == num:
                return True

            if mid ** 2 < num:
                start = mid + 1
            else:
                end = mid - 1

        return False

    # # LeetCode 牛人解法
    # def isPerfectSquare(self, num: int) -> bool:
    #     return num**0.5%1 == 0