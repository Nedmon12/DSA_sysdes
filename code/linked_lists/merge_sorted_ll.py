# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list1.val > list2.val:
        #    list3 = list2
        #    list2 = list2.next
        #else:
        #    list3 = list1
        #    list1 = list1.next
        #while list1 and list2:
        #    if list1.val > list2.val:
        #        list3.val = list2.val
        #        list2 = list2.next
        #    else:
        #        list3.val = list1.val
        #        list1 = list1.next
        #    list3 = list3.next

        #return list3
        head = lenode = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                lenode.next = list2
                list2 = list2.next
            else:
                lenode.next = list1
                list1 = list1.next
            lenode = lenode.next

        lenode.next = list1 or list2

        return head.next

