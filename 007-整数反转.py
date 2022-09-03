# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范[−2^31，2^31− 1] ，就返回 0。

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 反转后的x
        if x >= 0:
            rstrx = int(str(x)[::-1])
        else:
            rstrx = 0 - int(str(x)[::-1][:-1])

        if rstrx < -2 ** 31 or rstrx > 2 ** 31 - 1:
            return 0

        return rstrx