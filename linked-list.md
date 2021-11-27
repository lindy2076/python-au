# Linked List

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import intersect_two_linlists as itl


class IntersectionTest(unittest.TestCase):
    def setUp(self):
        self.solution = itl.Solution()

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
            elem = itl.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def build_intersected_linked_lists(self, source1, source2):
        source1 = source1[::-1]
        source2 = source2[::-1]
        prev_link = None
        while source1[0] == source2[0]:
            elem = itl.ListNode(source1[0], prev_link)
            prev_link = elem
            source1.pop(0)
            source2.pop(0)
        prev_link = elem
        for i in source1:
            headA = itl.ListNode(i, prev_link)
            prev_link = headA
        prev_link = elem
        for i in source2:
            headB = itl.ListNode(i, prev_link)
            prev_link = headB
        return headA, headB

    def test_intersection_building(self):
        expected = [8, 9]
        list1, list2 = self.build_intersected_linked_lists([1, 2, 3], [0, 2, 3])
        list1, list2 = list1.next, list2.next
        result = self.get_linked_list_values(list1)
        self.assertEqual(list1, list2)

    def test_no_intersection(self):
        expected = None
        list1 = self.build_linked_list([1, 2])
        list2 = self.build_linked_list([3, 4])
        result = self.solution.getIntersectionNode(list1, list2)
        self.assertEqual(expected, result)

    def test_intersection(self):
        list1, list2 = self.build_intersected_linked_lists([1, 2, 3], [0, 2, 3])
        expected = list1.next
        result = self.solution.getIntersectionNode(list1, list2)
        self.assertEqual(expected, result)


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
    def getIntersectionNode(self, headA, headB):
        elem = headA
        listA = set()
        while elem is not None:
            listA.add(elem)
            elem = elem.next
        elem = headB
        while elem is not None:
            if elem in listA:  # O(1) lol ne O(n) kak v list
                return elem
            elem = elem.next
        return None

```