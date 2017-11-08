import unittest

class Deque(object):
    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.storage = [None] * size
        self.head_idx, self.tail_idx = 0, size - 1
 
    def push_front(self, obj):
        if self.size == self.capacity:
            raise RuntimeError("Overflow")
        else:
            self.storage[self.head_idx] = obj
            self.size += 1
            self.head_idx = (self.head_idx + 1) % self.capacity

    def pop_front(self):
        if self.size == 0:
            raise RuntimeError("Downflow")
        else:
            self.head_idx = (self.head_idx - 1) % self.capacity
            tmp = self.storage[self.head_idx]
            self.storage[self.head_idx] = None
            self.size -= 1
            return tmp

    def push_back(self, obj):
        if self.size == self.capacity:
            raise RuntimeError("Overflow")
        else:
            self.storage[self.tail_idx] = obj
            self.size += 1
            self.tail_idx = (self.tail_idx - 1) % self.capacity

    def pop_back(self):
        if self.size == 0:
            raise RuntimeError("Downflow")
        else:
            self.tail_idx = (self.tail_idx + 1) % self.capacity
            tmp = self.storage[self.tail_idx]
            self.storage[self.tail_idx] = None
            self.size -= 1
            return tmp

    def __str__(self):
        return str(self.storage)


class TestDeque(unittest.TestCase):
    def test_two_way_push(self):
        deque = Deque(10)
        for i in range(5):
            deque.push_back(i)
            deque.push_front(i)

        for i in range(5):
            self.assertEqual(deque.pop_front(), 4 - i)

        for i in range(5):
            self.assertEqual(deque.pop_front(), i)

        for i in range(10):
            deque.push_front(i)

        for i in range(10):
            self.assertEqual(deque.pop_back(), i)

    def test_overflow(self):
        deque = Deque(3)
        for i in range(3):
            deque.push_front(i)

        with self.assertRaises(RuntimeError):
            deque.push_back(1)
        
        with self.assertRaises(RuntimeError):
            deque.push_front(1)

    def test_downflow(self):
        deque = Deque(3)

        with self.assertRaises(RuntimeError):
            deque.pop_front()
        
        with self.assertRaises(RuntimeError):
            deque.pop_back()


if __name__ == "__main__":
    unittest.main()
