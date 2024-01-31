reverse list and return count??

```
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        def delnode(node, tail): 
            tail.next = node.next

        prev = None
        while head:
           temp = head.next
           head.next = prev
           prev = head
           head = temp
        
        count = 0
        while count <= n:
            if count == n:
                delnode(head, tail)
            count +=1
            tail = head
            head = head.next
        prev = None
        while head:
           temp = head.next
           head.next = prev
           prev = head
           head = temp

```