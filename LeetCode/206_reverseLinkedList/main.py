from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_list = []
        if len(head) == 0:
            return []
        elif len(head) == 1:
            return head
        elif len(head) == 2:
            # swap head and it's next node
            first = head[0]
            second = first.next
            second.next = first
            first.next = None
            return [second, first]
        elif len(head) > 2:
            return [head[-1]] + self.reverseList(head[1:])
        return reverse_list

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return
        next = head.next
        next = self.reverseList(head.next)
        pass

class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = list(reversed(head))
        for node in head:
            self.nodeSwap(node, node.next)
        return head
    def nodeSwap(self, node1: ListNode, node2: ListNode):
        if node1.next == None:
            return
        node1.val, node2.val = node2.val, node1.val
        node1.next, node2.next = node2.next, node1.next

class Solution4:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (len(head)) <= 1:    # list is zero or one elements
            return
        else:                   # list has two or more elements
            reverseList(head)
        pass


sol = Solution3()
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
print(sol.reverseList([n1,n2,n3,n4,n5]))