# Design

+ [Min Stack](#min-stack)

## Min Stack

https://leetcode.com/problems/min-stack/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
import min_stack as ms


class MinStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.minstack = ms.MinStack()

    def test_case1(self):
        result = self.minstack
        expected = '[]'
        self.assertEqual(expected, str(result))

    def test_case2(self):
        result = []
        obj = self.minstack
        result.append(None)
        result.append(obj.push(-2))
        result.append(obj.push(0))
        result.append(obj.push(-3))
        result.append(obj.getMin())
        result.append(obj.pop())
        result.append(obj.top())
        result.append(obj.getMin())
        expected = [None, None, None, None, -3, None, 0, -2]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

```

</blockquote></details>


```python
class MinStack:
    def __init__(self):
        self.stack = []  # первым индексом хранится значение, вторым - последнее мин значение

    def __str__(self):
        return str(self.stack)

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:  # тут же и обнуляется минимальное если удалили
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:  # если есть чет в куче то выкидываем свежайший мин
            return self.stack[-1][1]
        else:  # выкидываем максимально возможное число
            return 2**31

```
