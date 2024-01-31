
```
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
```

break list in half
	use fast and slow pointers to get to half of the list
reverse the link for second half

merge both halfs by alternating between first and second

```
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fastPointer , slowPointer = head.next, head
        while fastPointer and fastPointer.next:
             slowPointer = slowPointer.next
             fastPointer = fastPointer.next.next

        second = slowPointer.next
        prev = slowPointer.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
```