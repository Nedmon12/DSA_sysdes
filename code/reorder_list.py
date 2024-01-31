class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        prev = None
        while head:
           temp = head.next
           head.next = prev
           prev = head
           head = temp
        tail = None
        prevy = prev
        count = 1
        if count == n:
            heady = None
            prevy = prevy.next
            while prevy:
                temp = prevy.next
                prevy.next = heady
                heady = prevy
                prevy = temp
            return heady
        while count <= n and prev:
            if count == n:
                #if count == 1:
                    #prev = prev.next
                    #break
                if prev.next is None:
                    if tail is not None:
                        tail.next = None
                        break
                else:
                    tail.next = prev.next
                    break
            count +=1
            tail = prev
            prev = prev.next
        head = None
        while prevy:
           temp = prevy.next
           prevy.next = head
           head = prevy
           prevy = temp
        return head


