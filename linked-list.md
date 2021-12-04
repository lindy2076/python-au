# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the linked list](#middle-of-the-linked-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import reversed_linked_list as rll


class TestReversedLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = rll.Solution()

    def test_reverse(self):
        expected = self.get_linked_list_values(self.build_linked_list([5, 4, 3, 2, 1]))
        actual = self.get_linked_list_values(self.solution.reverseList(self.create_linked_list(5)))
        self.assertEqual(expected, actual)  # add assertion here

    def test_reverse_empty(self):
        expected = None
        actual = self.solution.reverseList(None)
        self.assertEqual(expected, actual)  # add assertion here

    def create_linked_list(self, n=10):
        prev_link = None
        for i in range(n, 0, -1):
            elem = rll.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = rll.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result


if __name__ == '__main__':
    unittest.main()
```

</blockquote></details>



```python
def reverse_linked_list(head):
    elem = head
    prev_elem = None
    while elem is not None:
        next_elem = elem.next
        elem.next = prev_elem
        prev_elem = elem
        elem = next_elem
    return prev_elem
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import middle_of_the_linlist as midl


class MiddleOfTheLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.solution = midl.Solution()

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = midl.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def get_linked_list_values(self, head):
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def test_middleNode_odd(self):
        test_list = [1, 2, 3, 5, 6]
        test_linked_list = self.build_linked_list(test_list)
        expected = self.build_linked_list(test_list[len(test_list)//2:])
        result = self.solution.middleNode(test_linked_list)
        self.assertEqual(self.get_linked_list_values(expected), self.get_linked_list_values(result))

    def test_middleNode_even(self):
        test_list2 = [1, 2, 3, 5, 6, 7]
        test_linked_list2 = self.build_linked_list(test_list2)
        expected2 = self.build_linked_list(test_list2[len(test_list2) // 2:])
        result2 = self.solution.middleNode(test_linked_list2)
        self.assertEqual(self.get_linked_list_values(expected2), self.get_linked_list_values(result2))


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
    def middleNode(self, head):
        index = 0
        elem = head
        while elem.next is not None:
            index += 1
            elem = elem.next
        elem = head
        index += 1 if index % 2 else 0
        for _ in range(index//2):
            elem = elem.next
        return elem
```