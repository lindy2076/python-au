# Linked List

+ [Palindrome Linked List](#palindrome-linked-list)

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import palindrome_linlist as pll


class PalindromeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = pll.Solution()

    def build_linked_list(self, source):
        prev_link = None
        for i in source[::-1]:
            elem = pll.ListNode(i, prev_link)
            prev_link = elem
        return elem

    def test_palindrome_even_list(self):
        test_list = [1, 2, 2, 1]
        test_linked_list = self.build_linked_list(test_list)
        expected = True
        result = self.solution.isPalindrome(test_linked_list)
        self.assertEqual(expected, result)

    def test_palindrome_odd_list(self):
        test_list2 = [1, 2, 3, 2, 1]
        test_linked_list2 = self.build_linked_list(test_list2)
        expected2 = True
        result2 = self.solution.isPalindrome(test_linked_list2)
        self.assertEqual(expected2, result2)

    def test_palindrome_list_of_one(self):
        test_list3 = [1]
        test_linked_list3 = self.build_linked_list(test_list3)
        expected3 = True
        result3 = self.solution.isPalindrome(test_linked_list3)
        self.assertEqual(expected3, result3)

    def test_palindrome_random_list(self):
        test_list4 = [1, 2, 1, 1]
        test_linked_list4 = self.build_linked_list(test_list4)
        expected4 = False
        result4 = self.solution.isPalindrome(test_linked_list4)
        self.assertEqual(expected4, result4)


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
    def isPalindrome(self, head):
        list_len = 0
        elem = head
        list_values = []
        while elem is not None:
            list_values.append(elem.val)
            list_len += 1
            elem = elem.next
        first_part, second_part = list_values[:(list_len + 1) // 2], list_values[list_len // 2:]
        return second_part == first_part[::-1]
```