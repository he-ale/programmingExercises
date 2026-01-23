# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while head:
            uniq = head.next
            while uniq and uniq.val== head.val:
                uniq = uniq.next
            head.next = uniq
            head = head.next
        return root
        
            

solution= Solution()
solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None))))))
solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(1, None))))
solution.deleteDuplicates(ListNode())