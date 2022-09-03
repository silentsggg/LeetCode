# 递归判断一个数num是否为2的幂次方

class Solution:
    # # 递归
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n == 1:
    #         return True
    #     elif n < 1:
    #         return False
    #     else:
    #         return self.isPowerOfTwo(n/2)

    # 普通算法
    def isPowerOfTwo(self, n: int) -> bool:
        if n % 2 != 0 and n != 1:  # 排除n=1的情况，1%2=1，但是1是2零次方
            return False

        while n > 1:
            n /= 2

        return n == 1


if __name__ == '__main__':
    s1 = Solution()
    print(s1.isPowerOfTwo(128))
    print(0%2)
