from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"ListNode(val={self.val})"

def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, curr = None, head
        print(prv, '-' ,curr)
        while curr:
            t = curr.next
            curr.next = prv
            prv = curr
            curr = t
            print(f"t = {t} curr.next={prv} curr={curr} prv={prv}")
        return prv

# Test the implementation
if __name__ == "__main__":

    # Create test data
    test_data = [5, 4, 3, 2, 1]
    
    # Create linked list from test data
    head = create_linked_list(test_data)
    
    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    # Convert reversed linked list back to list for easy printing
    result = linked_list_to_list(reversed_head)
    
    print(f"Original list: {test_data}")
    print(f"Reversed list: {result}")