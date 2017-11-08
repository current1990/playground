import unittest
from Queue import Queue

class Stack(object):
    def __init__(self, size):
        self.q1 = Queue(size)
        self.q2 = Queue(size)
        self.active_queue = self.q1
        self.inactive_queue = self.q2
        self.size = 0
    
    def push(self, obj):
        if self.active_queue.full():
            raise RuntimeError("Overflow")
        else:
            self.active_queue.put(obj)
            self.size += 1

    def pop(self):
        if self.active_queue.empty():
            raise RuntimeError("Downflow")
        else:
            for i in range(self.size - 1):
                self.inactive_queue.put(self.active_queue.get())
            self.size -= 1
            self.active_queue, self.inactive_queue = self.inactive_queue, self.active_queue

            return self.inactive_queue.get()

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack(10)
        
        for i in range(10):
            stack.push(i)
        
        for i in range(10):
            self.assertEqual(stack.pop(), 9 - i)

    def test_overflow(self):
        stack = Stack(3)

        for i in range(3):
            stack.push(i)
        
        with self.assertRaises(RuntimeError):
            stack.push(9)

        stack.pop()
        stack.push(9)

        with self.assertRaises(RuntimeError):
            stack.push(9)

    def test_downflow(self):
        stack = Stack(2)

        with self.assertRaises(RuntimeError):
            stack.pop()

        stack.push(1)
        stack.pop()

        with self.assertRaises(RuntimeError):
            stack.pop()

if __name__ == "__main__": 
    unittest.main()