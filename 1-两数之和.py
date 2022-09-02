'''
- 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
- 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
- 你可以按任意顺序返回答案。
- 能否给出一个时间复杂度小于O(n²)的算法
'''


class Solution(object):
    '''
    # 暴力循环解法
    # 时间复杂度O(n²)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsl = len(nums)
        for i in range(numsl - 1):
            for j in range(i + 1, numsl):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    '''

    # 使用哈希表（key-value)，即字典与enumerate()函数
    # 时间复杂度O(n)
    # 定义一个空字典

    # 使用python自带的enumerate()方法获取可迭代对象的值与索引，这里可迭代对象是列表 nums
    # 使用enumerate()方法时，第一个获取索引，第二个获取值
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for index, i in enumerate(nums):
            # 查找在哈希表中是否存在目标target与列表数字之间的差值，如果有，说明列表nums中有满足条件的成员
            if target - i in hashmap:
                return [hashmap[target - i], index]
            # 没有就将i, index的键值对插入hashmap
            hashmap[i] = index
        return []


if __name__ == '__main__':
    s1 = Solution()
    print(s1.twoSum([2, 7, 11, 15], 9))
    print(s1.twoSum([11, 22, 3, 18, 24], 22))
    print(s1.twoSum([11, 22, 3, 18, 24], 25))

    str1 = 'string'
    print(str1[len(str1)-1::-1])