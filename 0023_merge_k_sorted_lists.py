# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next
        
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        
        return lists[0]

