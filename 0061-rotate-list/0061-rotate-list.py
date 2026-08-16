# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp=head
        len=1
        while temp!=None and temp.next!=None:
            temp=temp.next
            len=len+1

        k=k%len
        temp.next=head
        
        new_tail=head
        for _ in range(len -k-1):
            new_tail=new_tail.next

        new_head=new_tail.next
        new_tail.next=None
        return new_head
        