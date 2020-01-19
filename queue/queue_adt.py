"""
Use linked list as underlying container (do not use array). Implement circular queue ADT
createQueue: create a circular queue.
enqueue: queue insert.
dequeue: queue delete.
queueFront: retrieve the data at the front.
queueCount: return the number of elements in the queue. destroyQueue

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
    def __init__(self, node=None):
        self.rear = node
        self.front = None
        self.count = 0


def enqueue(queue, value):
    node = Node(value)
    if get_queue_count(queue) == 0:
        queue.rear = node
        queue.front = node
    else:
        node.before_node = queue.rear
        queue.rear.next_node = node
        queue.rear = node
    queue.count += 1


def dequeue(queue):
    if get_queue_count(queue) == 0:
        raise Exception('큐가 비어있습니다.')
    else:
        result = queue.rear.value
        if get_queue_count(queue) > 1:
            queue.rear = queue.rear.before_node
        queue.rear.next_node = None
    queue.count -= 1
    return result


def get_queue_front(queue):
    return queue.front.value


def get_queue_count(queue):
    return queue.count


def destroy_queue(queue):
    while get_queue_count(queue) > 0:
        dequeue(queue)


class QueueTestCase(unittest.TestCase):

    def test_enqueue(self):
        q1 = Queue()
        enqueue(q1, 10)
        enqueue(q1, 20)
        enqueue(q1, 30)

        assert get_queue_count(q1) == 3
        assert get_queue_front(q1) == 10
        assert q1.rear.value == 30

    def test_dequeue(self):
        q1 = Queue()
        for value in range(1, 5):
            enqueue(q1, value)
        assert get_queue_count(q1) == 4

        assert dequeue(q1) == 4
        assert dequeue(q1) == 3
        assert dequeue(q1) == 2
        assert dequeue(q1) == 1
        with self.assertRaises(Exception):
            dequeue(q1)

    def test_destroy(self):
        q1 = Queue()
        for value in range(1, 5):
            enqueue(q1, value)
        assert get_queue_count(q1) == 4

        destroy_queue(q1)
        assert get_queue_count(q1) == 0
