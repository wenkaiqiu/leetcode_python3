"""
https://leetcode.com/problems/add-two-numbers/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v = l1.val + l2.val
        out = ListNode(v % 10)
        s = v // 10
        p = out
        while l1.next is not None or l2.next is not None:
            val = 0
            if l1.next is None:
                l2 = l2.next
                val = l2.val + s
            elif l2.next is None:
                l1 = l1.next
                val = l1.val + s
            else:
                l1 = l1.next
                l2 = l2.next
                val = l1.val + l2.val + s
            p.next = ListNode(val % 10)
            s = val // 10
            p = p.next
        if s != 0:
            p.next = ListNode(s)
        return out

    def addTwoNumbers2(self, l1, l2):
        """
        worse one
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        p1 = l1
        int1 = 0
        base = 1
        while p1 is not None:
            int1 += p1.val * base
            base *= 10
            p1 = p1.next

        p2 = l2
        int2 = 0
        base = 1
        while p2 is not None:
            int2 += p2.val * base
            base *= 10
            p2 = p2.next

        val = int1 + int2
        out = ListNode(val % 10)
        val = val // 10
        p = out
        while val != 0:
            p.next = ListNode(val % 10)
            p = p.next
            val = val // 10
        return out

    def __init__(self):
        input1 = ListNode(2)
        input1.next = ListNode(4)
        input1.next.next = ListNode(5)
        input2 = ListNode(5)
        input2.next = ListNode(6)
        input2.next.next = ListNode(4)
        res = self.addTwoNumbers(input1, input2)
        self.print_list(res)

    def print_list(self, l):
        print(l.val, end='')
        while l.next is not None:
            l = l.next
            print(' -> ', end='')
            print(l.val, end='')


Solution()
