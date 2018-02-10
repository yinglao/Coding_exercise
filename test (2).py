#Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
#If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
#You may not alter the valuess in the nodes, only nodes itself may be changed.
#Only constant memory is allowed.

#Example
#Given this linked list: 1->2->3->4->5
#
#For k = 2, you should return: 2->1->4->3->5
#
#For k = 3, you should return: 3->2->1->4->5
#
"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        nk = self.reverse(dummy, k)
        while nk:
            nk = self.reverse(nk, k)
        return dummy.next ##
        
        
    def reverse(self, head, k):
        '''
        head -> n1 -> n2 -> n3... -> nk -> nkplus
        head    n1 <- n2 <- n3... <- nk    nkplus
        head -> nk ->... -> n1 -> nkplus
        '''
        
        if head is None or head.next is None:
            return None
        
        nk = head
        n1 = head.next
        for i in range(k):
            if nk is None:
                return None
            nk = nk.next
        
        if nk is None:
            return None
        nkplus = nk.next
        head.next = None
        nk.next = None ##
        
        cur, post = n1, n1.next
        #print cur.val, post.val
        for i in range(1, k):
            temp = post.next
            post.next = cur
            cur, post = post, temp
        
        head.next = nk
        n1.next = nkplus
        #print head.val, n1.val, nk.val
        
        return n1