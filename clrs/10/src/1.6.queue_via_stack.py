import unittest

class Queue(object):
    def __init__(self):
        self.size = 0
        self.inbox = list()
        self.outbox = list()

    def push_back(self, obj):
        if len(self.outbox) == 0:
            self.inbox.append(obj)
            self.size += 1
        else:
            for i in range(self.size):
                self.inbox.append(self.outbox.pop())
            self.inbox.append(obj)
            self.size += 1

    def pop_front(self):
        v = None
        if self.size == 0:
            raise RuntimeError("Downflow")

        if len(self.outbox) >= 1:
            v = self.outbox.pop()
        else:
            for i in range(self.size - 1):
                self.outbox.append(self.inbox.pop())
            v = self.inbox.pop()

        self.size -= 1
        return v


class TestQueue(unittest.TestCase):
    def test_push_pop(self):
        queue = Queue()
        for i in range(10):
            queue.push_back(i)
            self.assertEqual(queue.pop_front(), i)

        for i in range(10):
            queue.push_back(i)
        
        print queue.inbox, queue.outbox
        for i in range(10):
            self.assertEqual(queue.pop_front(), i)

        queue.push_back(1)
        queue.push_back(2)
        self.assertEqual(queue.pop_front(), 1)
        queue.push_back(3)
        self.assertEqual(queue.pop_front(), 2)
        self.assertEqual(queue.pop_front(), 3)

    def test_downflow(self):
        queue = Queue()

        with self.assertRaises(RuntimeError):
            queue.pop_front()
        
        queue.push_back(1)
        queue.pop_front()

        with self.assertRaises(RuntimeError):
            queue.pop_front()

if __name__ == "__main__":
    unittest.main()