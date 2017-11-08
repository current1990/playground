import unittest

class DoubleStack(object):
    def __init__(self, size):
        self.size = size
        self.left_idx = -1
        self.right_idx = size
        self.storage = [None] * size

    def push_left(self, obj):
        if self.left_idx == self.right_idx - 1:
            raise RuntimeError("Left Overflow")
        else:
            self.left_idx += 1
            self.storage[self.left_idx] = obj

    def pop_left(self):
        if self.left_idx == -1:
            raise RuntimeError("Left Downflow")
        else:
            tmp = self.storage[self.left_idx]
            self.storage[self.left_idx] = None
            self.left_idx -= 1
            return tmp

    def push_right(self, obj):
        if self.right_idx == self.left_idx + 1:
            raise RuntimeError("Right Overflow")
        else:
            self.right_idx -= 1
            self.storage[self.right_idx] = obj

    def pop_right(self):
        if self.right_idx == self.size:
            raise RuntimeError("Right Downflow")
        else:
            tmp = self.storage[self.right_idx]
            self.storage[self.right_idx] = None
            self.right_idx += 1
            return tmp

    def __str__(self):
        return str(self.storage)


class TestDoubleStack(unittest.TestCase):
    """ Test Case for DoubleStack """
    def test_left(self):
        """ Test for left end """
        stack = DoubleStack(3)
        for i in range(3):
            stack.push_left(i)

        self.assertEquals(stack.storage, [0, 1, 2])

        # Left Overflow
        with self.assertRaises(RuntimeError):
            stack.push_left(123)

        for i in range(3):
            r = stack.pop_left()
            self.assertEquals(r, 2 - i)

        # Left Downflow
        with self.assertRaises(RuntimeError):
            stack.pop_left()

    def test_right(self):
        """ Test for right end """
        stack = DoubleStack(3)
        for i in range(3):
            stack.push_right(i)

        self.assertEquals(stack.storage, [2, 1, 0])

        # Right Overflow
        with self.assertRaises(RuntimeError):
            stack.push_right(123)

        for i in range(3):
            r = stack.pop_right()
            self.assertEquals(r, 2 - i)

        # Right Downflow
        with self.assertRaises(RuntimeError):
            stack.pop_right()

    def test_two_way_push(self):
        stack = DoubleStack(8)
        expected_result = [0, 1, 2, 3, 3, 2, 1, 0]

        for i in range(4):
            stack.push_left(i)
            stack.push_right(i)

        self.assertEquals(stack.storage, expected_result)


if __name__ == "__main__":
    unittest.main()
