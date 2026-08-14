class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case
        if head == None or head.next == None:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        left = head
        right = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge
        dummy = ListNode(0)
        curr = dummy

        while left != None and right != None:

            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        # Attach whatever remains
        if left != None:
            curr.next = left
        else:
            curr.next = right

        return dummy.next