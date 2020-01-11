"""
Implement stack ADT.
 CreateStack: allocate memory and initialize.
 Push
 Pop
 Stack Top
 DestroyStack : remove all items and deallocate memory.
 CatStack : concatenate two stacks.

- with LinkedList
"""

import unittest


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class MyStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        new_node = Node(data)
        if self.count > 0:
            new_node.next_node = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.count <= 0:
            return

        result = self.top.data
        self.top = self.top.next_node
        self.count -= 1
        return result

    def top(self):
        return self.top

    def cat(self, stack):
        temp = MyStack()
        for i in range(stack.count):
            temp.push(stack.pop())

        for i in range(self.count):
            self.push(temp.pop())


class MyStackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = MyStack()

    def test_push(self):
        self.stack.push(1)

        assert self.stack.count == 1
        assert self.stack.top.data == 1

    def test_multiple_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        assert self.stack.count == 3
        assert self.stack.top.data == 3

    def test_pop(self):
        self.stack.push(1)
        result = self.stack.pop()

        assert result == 1
        assert self.stack.count == 0
        assert self.stack.top is None

    def test_multiple_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        assert self.stack.count == 3
        assert self.stack.top.data == 3

        result = self.stack.pop()
        assert result == result
        assert self.stack.count == 2
        assert self.stack.top == 2

    def test_cat(self):
        stack1 = MyStack()
        stack2 = MyStack()

        for i in range(3):
            stack1.push(i)
            stack2.push(i+3)

        stack1.cat(stack2)

        assert stack1.count == 6
        assert stack1.top.data == 5


if __name__ == '__main__':
    unittest.main()
