# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足
# arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]的下标i

class Solution:
    # # O(n)解法
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     # 调用函数max，返回列表最大值，然后找出最大值的索引值
    #     return arr.index(max(arr))

    # O(logn)解法
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 找到山峰数的判断条件是
        # 如果山峰数的索引是n，则arr[n-1] < arr[n] < arr[n+1]
        # 使用二分查找算法
        # 如果arr[mid]<arr[mid+1],说明山峰数在右边
        # 如果arr[mid]<arr[mid-1],说明山峰数在左边

        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        return mid