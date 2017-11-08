import unittest

class Queue(object):
    def __init__(self, size):
        self.size = 0
        self.capacity = size
        self.head_idx, self.tail_idx = 0, 0
        self.storage = [None] * size

    def enqueue(self, obj):
        if self.size == self.capacity:
            err = "Overflow, h=%d, t=%d" % (self.head_idx, self.tail_idx)
            raise RuntimeError(err)
        else:
            self.storage[self.tail_idx] = obj
            self.tail_idx = (self.tail_idx + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise RuntimeError("Downflow")
        else:
            tmp = self.storage[self.head_idx]
            self.storage[self.head_idx] = None
            self.head_idx = (self.head_idx + 1) % self.capacity
            self.size -= 1
            return tmp


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeu(self):
        queue = Queue(3)
        for i in range(10):
            queue.enqueue(i)
            self.assertEqual(queue.dequeue(), i)

            queue.enqueue(i)
            queue.enqueue(i)
            queue.enqueue(i)
            self.assertEqual(queue.dequeue(), i)
            self.assertEqual(queue.dequeue(), i)
            self.assertEqual(queue.dequeue(), i)

    def test_overflow(self):
        queue = Queue(1)
        queue.enqueue(-1)

        for i in range(10):
            with self.assertRaises(RuntimeError):
                queue.enqueue(i)

            self.assertEqual(queue.dequeue(), i - 1)      
            queue.enqueue(i)

    def test_downflow(self):
        queue = Queue(2)

        for i in range(10):
            with self.assertRaises(RuntimeError):
                queue.dequeue()

            queue.enqueue(i)
            self.assertEqual(queue.dequeue(), i)


if __name__ == "__main__":
    unittest.main()
