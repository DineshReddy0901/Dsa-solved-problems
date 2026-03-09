# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        # if head is None:
        #     return False
        # current = head
        # temp = current.next
        # if current.next is None:
        #     return False
        # while current:
        #     current = current.next
        #     if current == temp:
        #         return True
        #     else:
        #         return False



         slow = head
         fast = head
         while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
         return False

        