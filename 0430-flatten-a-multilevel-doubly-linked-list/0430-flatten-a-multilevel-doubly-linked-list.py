class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head

        while current:
            if current.child:
                next_node = current.next

                current.next = current.child
                current.child.prev = current

                child = current.child

                while child.next:
                    child = child.next

                child.next = next_node

                if next_node:
                    next_node.prev = child

                # Remove child pointer
                current.child = None

            current = current.next

        return head