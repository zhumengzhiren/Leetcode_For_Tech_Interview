# 234. 回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# 示例 1：

# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：

# 输入：head = [1,2]
# 输出：false

# 经典题目, 反转链表 + 快慢指针，居然是easy题目

def isPalindrome(self, head):
    # 先写一个快慢指针范式
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 再写一个头插范式
    pre = None
    cur = slow
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 最后写一个双检测范式
    while head and pre:
        if head.val != pre.val:
            return False
        head = head.next
        pre = pre.next
    return True