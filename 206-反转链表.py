# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 使用栈
    # 先将n-1个结点入栈，然后再出栈
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        lst = []
        curr = head
        # 入栈
        while curr.next:
            lst.append(curr)
            curr = curr.next
        # 出栈
        head = curr
        while lst:
            curr.next = lst.pop()
            curr = curr.next
        # 注意这时curr指向node1，但是node1.next=node2，所以出栈循环结束后必须将node1的next指向None,否则在打印链表时会无限循环
        curr.next = None
        return head

    # # 迭代，需要指向当前结点的指针curr，指向上一结点的指针prev，指向下一结点的指针next
    # # 反转的操作为，让当前结点的指针指向上一结点；prev指向curr结点；curr结点指向下一结点
    # # 迭代条件为curr结点部位None
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     curr = head

    #     while curr:
    #         next = curr.next    # 创建指向当前curr的下一结点的指针
    #         curr.next = prev    # 反转，curr的下一结点为上一节点
    #         prev = curr # 下一步的上一节点为当前curr结点
    #         curr = next # 当前curr结点指向下一结点

    #     return prev


if __name__ == '__main__':
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    s1 = Solution()
    newhead = s1.reverseList(node1)

    while newhead:
        print(newhead.val, end=' -> ') if newhead.next else print(newhead.val)
        newhead = newhead.next
