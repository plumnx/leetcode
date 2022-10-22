# 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
#
#
# 示例 1：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.

# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]

# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
# 提示：
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def getAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.getAttrs()) + "}"


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1 + num2 + carry

            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return dummy.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0);
        curr = result;

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + curr.val
            val3 = sum // 10
            val4 = sum % 10

            curr.val = val4

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if (l1 or l2) or val3 > 0:
                curr.next = ListNode(val3)
                curr = curr.next if curr else 0

        return result


if __name__ == "__main__":
    # case 1
    # cur = l1 = ListNode(2)
    # cur.next = ListNode(4)
    # cur = cur.next
    # cur.next = ListNode(3)
    #
    # cur = l2 = ListNode(5)
    # cur.next = ListNode(6)
    # cur = cur.next
    # cur.next = ListNode(4)

    # case 2
    cur = l1 = ListNode(9)
    cur.next = ListNode(9)
    cur = cur.next
    cur.next = ListNode(9)

    cur = l2 = ListNode(9)
    cur.next = ListNode(9)
    cur = cur.next
    cur.next = ListNode(9)
    cur = cur.next
    cur.next = ListNode(9)

    print(Solution().addTwoNumbers2(l1, l2))
