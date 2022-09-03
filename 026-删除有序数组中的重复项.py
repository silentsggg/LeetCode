class Solution:
    # # 暴力解法
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     length = len(nums)
    #     i = 0
    #
    #     while i < length:
    #         j = i +1
    #         while j < length:
    #             if nums[i] == nums[j]:
    #                 nums.pop(j)
    #                 length -= 1
    #                 j -= 1
    #             j += 1
    #         i += 1
    #     return len(nums)

    # #暴力解法2
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     i = 0
    #     length = len(nums)
    #     while i < length-1:
    #         if nums[i] in nums[i+1:]:
    #             nums.pop(i)
    #             length -= 1
    #             i -= 1
    #         i += 1
    #     return length
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        q = 1
        length = len(nums)
        while q < length:
            if nums[p] == nums[q]:
                q += 1
            else:
                nums[p+1] = nums[q]
                q += 1
                p += 1
        return p+1

if __name__ == '__main__':
    s1 = Solution()
    lst1 = [1, 1, 2, 2, 3]
    print(s1.removeDuplicates(lst1))
    print(lst1)

