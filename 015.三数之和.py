class Solution:
    # 列表先排序
    # 三重指针，第一个指针遍历列表，后面两个指针做双重指针
    # 第二个指针从小到大，第三个指针从大到小遍历
    # 因为列表经过了排序，所以第二个指针指向的元素值会越来越大，而第三个指针指向的元素值会越来越小，
    # 这样可以将双指针枚举的空间复杂度由O(n²)减小到O(n),加上最外层循环，总时间复杂度为O(n²)

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        res = []
        # 第一个指针，用于遍历列表nums；第二个指针在第一个指针后面；第三个指针k，从列表最后开始往前遍历到第二个指针；
        # 由于第二、第三指针的起点是动态的，所以在枚举时定义
        # first, second, third = 0, 1, length - 1
        nums.sort()

        for first in range(length):
            # 保证取到的第一个数与上一次不同
            if first > 0 and nums[first] == nums[first-1]:
                continue

            # 寻找第二指针和第三指针指向的元素的和
            target = -nums[first]
            # 第三指针指向列表最右
            third = length - 1
            # 使用第二指针遍历第一指针右侧的元素
            for second in range(first+1, length):
                # 保证取到的数和上次不同
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                # second 指针在 first的右侧
                # 循环3
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 判断出上面的循环时，元素之和及指针情况
                # 出循环3第一种情况，指针重合,说明第二指针后面也不会有合适的数了，因为列表经过排序，后面的数更大
                # 所以从下一个第一指针继续
                if second == third:
                    break
                # 出循环3第二种情况，nums[second] + nums[third] !> target
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res


if __name__ == '__main__':
    s1 = Solution()
    lst1 = [-1, 0, 1, 2, -1, -4]
    lst1.sort()
    lst2 = [-23,-67,32,21,-65,46,73,42,93,9,-61,-79,-51,61,-15,49,92,-34,50,1,26,-12,68,-97,-17,51,-55,75,-56,-95,-70,-42,91,-18,-64,20,33,-20,19,61,-89,81,-73,82,-23,-65,51,-88,15,-48,24,34,0,-24,37,22,28,-67,-25,-61,-57,-74,65,50,-66,24,99,80,44,85,20,-4,-9,-81,87,-82,-100,51,-83,9,-31,37,23,-61,53,-14,-51,88,56,27,42,-52,-97,37,36,-59,-45,95,46,-1,-100,-38,66,44,27,-97,12,-43,84,-53,93,18,-40,-38,34,85,53,-50,-14,-6,98,-77,-17,50,-65,52,-46,-94,49,72,-2,-82,45,-39,-58,67,82,63,95,-32,47,15,-20,46,5,17,-40,-95,97,-9,11,8,-51,-24,-50,-37,-72,-57,26,26,19,71,-42]
    lst2.sort()
    # print(s1.threeSum(lst2))
    print(lst2)
