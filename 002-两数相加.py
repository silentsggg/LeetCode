# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 通过反转字符串，str转int再转str来实现
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        int1 = ''
        int2 = ''
        pr1 = l1
        pr2 = l2
        while pr1:
            int1 = int1 + str(pr1.val)
            pr1 = pr1.next
        while pr2:
            int2 = int2 + str(pr2.val)
            pr2 = pr2.next

        sum = int(int1[::-1]) + int(int2[::-1])

        sumr = str(sum)[::-1]

        head = ListNode(int(sumr[0]))
        cur = head
        index = 1
        while index < len(sumr):
            cur.next = ListNode(int(sumr[index]))
            cur = cur.next
            index += 1
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2, l1)
    l3 = ListNode(3, l2)

    l4 = ListNode(4)
    l5 = ListNode(5, l4)
    l6 = ListNode(6, l5)

    s1 = Solution()
    # print(s1.addTwoNumbers(l1, l4).val)
    res = s1.addTwoNumbers(l3, l6)
    while res:
        print(res.val, end='') if res.next else print(res.val)
        res = res.next

    strc = 'string'
    # print(list(strc))
    print(strc[3:0:-1] + strc[0])
