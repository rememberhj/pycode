

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def list_to_linked_list(lst):
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next
    
    return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n):
        # 由于可能会删除链表头部，用哨兵节点简化代码
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        dummy = ListNode(0, head)
        print(object2Map(dummy))
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
            print(object2Map(dummy))
        cur.next = cur.next.next
        return dummy.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        #return dummy.next
def object2Map(obj:object):
    """对象转Dict"""
    if obj is None:
        return None
    if type(obj) == list:
        return [ object2Map(obj_item) for obj_item in obj]
    if obj.__dict__ is None:
        return obj
    m = {}
    for k in obj.__dict__.keys():
        v = obj.__dict__[k]
        if hasattr(v, "__dict__"):
            m[k] = object2Map(v)
        else:
            m[k] = v
    return m
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [1, 3, 3, 6, 7]
my_linked_list1 = list_to_linked_list(my_list1)
my_linked_list2 = list_to_linked_list(my_list2)
"""
print(object2Map(my_linked_list))
"""

print(object2Map(Solution().mergeTwoLists(my_linked_list1,my_linked_list2)))