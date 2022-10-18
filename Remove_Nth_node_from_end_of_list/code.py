# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #initializing fast and slow pointers
        fast = head
        slow = head
        #moving the fast pointer
        for i in range(0,n):
            fast = fast.next
        if fast==None:
            return head.next
        #moving the slow pointer
        while(fast.next!=None):
            fast = fast.next
            slow = slow.next
        #removing the node by updating links
        slow.next = slow.next.next
        return head
