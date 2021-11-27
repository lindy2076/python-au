# Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)

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