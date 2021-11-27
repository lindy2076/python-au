# Linked List

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import merge_two_linlists as mtl


class MergeTwoLinkedListsTest(unittest.TestCase):
    def setUp(self):
        self.solution = mtl.Solution()

    def build_linked_list(self, source):
        if source is None or not source:
            return None
        prev_link = None
        for i in source[::-1]:
            elem = mtl.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def test_merging(self):
        list1 = [1, 3, 4]
        list2 = [1, 2, 5, 6]
        linked_list1 = self.build_linked_list(list1)
        linked_list2 = self.build_linked_list(list2)

        result = self.solution.mergeTwoLists(linked_list1, linked_list2)
        expected = self.build_linked_list([1, 1, 2, 3, 4, 5, 6])
        self.assertEqual(self.get_linked_list_values(expected), self.get_linked_list_values(result))

    def test_merge_empty(self):
        list1 = []
        list2 = [1, 2]
        linked_list1 = self.build_linked_list(list1)
        linked_list2 = self.build_linked_list(list2)

        result = self.solution.mergeTwoLists(linked_list1, linked_list2)
        expected = self.build_linked_list([1, 2])
        self.assertEqual(self.get_linked_list_values(expected), self.get_linked_list_values(result))


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode()
        head = result
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                result.next, list1 = list1, list1.next
            else:
                result.next, list2 = list2, list2.next
            result = result.next
        if list1 is not None:
            result.next = list1
        if list2 is not None:
            result.next = list2
        return head.next
```