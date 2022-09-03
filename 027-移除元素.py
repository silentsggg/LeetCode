class Solution:
    # # 列表pop，注意元素index与数组长度在pop后需要进行调整
    # def removeElement(self, nums: list[int], val: int) -> int:
    #     length = len(nums)
    #     index = 0
    #     while index < length:
    #         if nums[index] == val:
    #             nums.pop(index)
    #             length -= 1
    #             index -= 1
    #         index += 1
    #
    #     return length

    # 双指针
    # 设置左右两个指针，同时指向列表第一个元素
    # 如果右指针元素不等于val，说明该元素是最后列表中的元素，将该元素的值拷贝至左指针元素，并同时右移左右指针
    # 如果右指针元素等于val，说明该元素不是最后列表的元素，这时左指针不动，右指针右移
    # 直到右指针指向nums的length，需要返回的列表长度为左指针+1

    def removeElement(self, nums: list[int], val: int) -> int:
        # 定义左右指针,指向nums的第一个元素
        p = 0
        q = 0
        length = len(nums)
        while q < length:
            # 右指针元素不等于val
            if nums[q] != val:
                nums[p] = nums[q]
                p += 1
                q += 1
            # 右指针元素等于val
            else:
                q += 1
        return p


if __name__ == '__main__':
    s1 = Solution()
    str1 = [1, 2, 3, 5, 1, 1, 7]
    print(s1.removeElement(str1, 1))
    print(str1)
