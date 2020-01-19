"""
Use linked list as underlying container (do not use array). Implement circular queue ADT
createQueue: create a circular queue.
enqueue: queue insert.
dequeue: queue delete.
queueFront: retrieve the data at the front.
queueCount: return the number of elements in the queue.

Example:
    Q1 = createQueue(); enqueue(Q1, 10); enqueue(Q1, 20); enqueue(Q1, 30);
    c1 = queueCount(Q1); dequeue(Q1); queueFront(Q1);
    c2 = queueCount(Q1); destroyQueue(Q1);
"""
import unittest


class Node:
    def __init__(self, value, before_node=None, next_node=None):
        self.value = value
        self.before_node = before_node
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def enqueue(self, value):
        node = Node(value)
        if self.count == 0:
            self.rear = node
            self.front = node
        else:
            node.before_node = self.rear
            self.rear.next_node = node
            self.rear = node
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('큐가 비어있습니다.')
        elif self.count == 1:
            result = self.rear.value
            self.rear = None
            self.front = None
        else:
            result = self.rear.value
            self.rear = self.rear.before_node
            self.rear.next_node = None
        self.count -= 1
        return result

    def get_queue_front(self):
        if self.front:
            return self.front.value
        else:
            raise

    def get_queue_count(self):
        return self.count


class QueueTestCase(unittest.TestCase):

    def test_enqueue(self):
        q1 = Queue()
        q1.enqueue(10)
        q1.enqueue(20)
        q1.enqueue(30)

        assert q1.get_queue_count() == 3
        assert q1.get_queue_front() == 10
        assert q1.rear.value == 30

    def test_dequeue(self):
        q1 = Queue()
        for value in range(1, 5):
            q1.enqueue(value)
        assert q1.get_queue_count() == 4

        assert q1.dequeue() == 4
        assert q1.dequeue() == 3
        assert q1.dequeue() == 2
        assert q1.dequeue() == 1
        with self.assertRaises(Exception):
            q1.dequeue()
        assert q1.get_queue_count() == 0
