# Arrays

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import square_array as sa


class SquareArrayTest(unittest.TestCase):
    def setUp(self):
        self.solution = sa.Solution()

    def test_empty_list(self):
        expected = []
        result = self.solution.sortedSquares([])
        self.assertEqual(expected, result)

    def test_diff_signs(self):
        test_data = [-2, -1, 2, 4, 10]
        expected = sorted([i * i for i in test_data])
        result = self.solution.sortedSquares(test_data)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()


```


</blockquote></details>

```python
class Solution:
    def sortedSquares(self, data):
        left_index = 0
        right_index = len(data) - 1
        result = []
        while left_index <= right_index:
            if data[left_index]**2 > data[right_index]**2:
                result.append(data[left_index]**2)
                left_index += 1
            else:
                result.append(data[right_index]**2)
                right_index -= 1
        return result[::-1]

```
