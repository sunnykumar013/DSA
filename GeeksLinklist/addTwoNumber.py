# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr_dummy = dummy
        carry = 0
        while l1 or l2 or carry == 1:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            curr_dummy.next = node
            curr_dummy = curr_dummy.next

        return dummy.next


