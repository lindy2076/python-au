# Linked List

+ [Sort List](#sort-list)

## Sort List
 
https://leetcode.com/problems/sort-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import linked_list_sort as lsort


class LinkedListSortCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = lsort.Solution()

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def build_linked_list(self, source):
        if source is None or not source:
            return None
        prev_link = None
        for i in source[::-1]:
            elem = lsort.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def test_sorting(self):
        list1 = self.build_linked_list([1, 3, 2, 6, 5])
        expected = [1, 2, 3, 5, 6]
        result = self.solution.sortList(list1)
        self.assertEqual(expected, self.get_linked_list_values(result))

    def test_sorting_empty(self):
        list1 = []
        self.assertEqual(None, self.solution.sortList([]))


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>



```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution: 
    def sortList(self, head):
        elem = head
        if not elem:
            return None
        list_links = []
        while elem is not None:
            list_links.append(elem)
            elem = elem.next
        sorted_list = sorted(list_links, key=lambda x: x.val)
        for i, elem in enumerate(sorted_list):
            if i == 0:
                head = elem
            if i + 1 < len(sorted_list):
                elem.next = sorted_list[i + 1]
            else:
                elem.next = None
        return head
```