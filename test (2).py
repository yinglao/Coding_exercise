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