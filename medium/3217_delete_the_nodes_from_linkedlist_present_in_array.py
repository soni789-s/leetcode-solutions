# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        curr=ListNode()
        dummy=curr
        while head!=None:
            if head.val not in nums:
                curr.next=ListNode(head.val)
                head=head.next
                curr=curr.next    
            else:
                head=head.next
        return dummy.next