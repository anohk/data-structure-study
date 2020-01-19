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
        self.top = node
        self.front = None
        self.count = 0


def enqueue(queue, value):
    node = Node(value)
    if get_queue_count(queue) == 0:
        queue.top = node
        queue.front = node
    else:
        node.before_node = queue.top
        queue.top.next_node = node
        queue.top = node
    queue.count += 1


def dequeue(queue):
    if get_queue_count(queue) == 0:
        raise
    else:
        result = queue.top.value
        if get_queue_count(queue) > 1:
            queue.top = queue.top.before_node
        queue.top.next_node = None
    queue.count -= 1
    return result


def get_queue_front(queue):
    return queue.front.value


def get_queue_count(queue):
    return queue.count


class QueueTestCase(unittest.TestCase):

    def test_queue(self):
        Q1 = Queue()
        enqueue(Q1, 10)
        enqueue(Q1, 20)
        enqueue(Q1, 30)

        assert get_queue_count(Q1) == 3
        assert dequeue(Q1) == 30
        assert get_queue_front(Q1) == 10
