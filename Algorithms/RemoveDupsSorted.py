# note that this is a singly linked list 
# (can only move forward through the nodes)
# to move both directions it would be a doubly linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def RemoveDupsSorted(head):
    cur = head
    while cur is not None:
        # while there is a value
        while cur.next is not None and cur.val == cur.next.val:
            # when the current value is equal to the next value
            cur.next = cur.next.next
            # replace the next node, with the node that proceeds it           
            cur = cur.next
            # replace the current node with the node that proceeds it
        return head