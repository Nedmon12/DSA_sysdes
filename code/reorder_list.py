# Definition of singly-linked list
# class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head:
            #iterator = head
            ittwin = iterator = ListNode()
            ittwin = iterator = head
            while iterator:
                if not iterator.next:
                    # number is to be neighbor to head
                    temp = head
                    head.next = iterator
                    iterator.next = temp.next
                    head = temp.next
                    ittwin.next = None
                ittwin = iterator
                iterator = iterator.next
        head = head.next
