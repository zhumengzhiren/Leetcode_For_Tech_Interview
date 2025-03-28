# 876. 链表的中间结点
# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。

# 如果有两个中间结点，则返回第二个中间结点。

# 示例 1：

# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。
# 示例 2：

# 输入：head = [1,2,3,4,5,6]
# 输出：[4,5,6]
# 解释：该链表有两个中间结点，值分别为 3 和 4 ，返回第二个结点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 注意，该算法总是会返回第二个中间节点。如果有两个中间节点，则返回第二个中间节点。
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(middleNode(head).val) # 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(middleNode(head).val) # 4

