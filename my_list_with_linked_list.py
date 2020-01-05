"""
MyList ADT:

Object : 순서가 있는 여러개의 object 집합
Operations : (괄호안은 충족되어야 하는 시간복잡도)
    get(n) : n번째 아이템 return (n)
    append(item) : item 제일 뒤에 붙이기 (n)
    remove(index): index번째 아이템 삭제하고 return (n)
    insert(index, item) : index번째에 아이템 추가하기 (n)
    예외상황, 오류는 적절하게 처리하시면 됩니다.

LinkedList로 구현하기
"""
import unittest


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyList:

    def __init__(self):
        self.counter = 0
        self.header = None

    def append(self, node):
        """마지막 노드 뒤에 새로운 노드를 추가한다"""
        pointer = self.header

        if pointer is None:
            self.header = node
        else:
            while pointer.next_item:
                pointer = pointer.next_item
            pointer.next_item = node
        self.counter += 1

    def get(self, index):
        """index 번째 노드의 값을 리턴한다."""
        self.validate_index(index)
        pointer = self.header

        idx = 0
        while idx < self.counter:
            if idx == index:
                result = pointer.value
                return result

            pointer = pointer.next_item
            idx += 1

    def remove(self, index):
        """index 번째 노드를 삭제하고 리턴한다."""
        self.validate_index(index)
        pointer = self.header

        idx = 0
        pre_pointer = pointer
        while idx < self.counter:
            if idx == index:
                pre_pointer.next_item = pointer.next_item
                result = pointer.value
                self.counter -= 1

                if index == 0:
                    self.header = pointer.next_item

                return result

            pre_pointer = pointer
            pointer = pointer.next_item
            idx += 1

    def insert(self, index, node):
        """index번째에 item을 추가한다."""
        self.validate_index(index)
        pointer = self.header
        pre_pointer = pointer

        idx = 0
        while idx < self.counter:
            if idx == index:
                if index == 0:
                    node.next_item = pre_pointer
                    self.header = node
                else:
                    node.next_item = pre_pointer.next_item
                    pre_pointer.next_item = node
                self.counter += 1
                break
            else:
                pre_pointer = pointer
                pointer = pointer.next_item
            idx += 1

    def validate_index(self, index):
        """전달받은 index값이 MyList에서 유효한지 검사한다."""
        if self.counter <= index:
            raise IndexError


def get_all_items(my_list):
    result = []
    pointer = my_list.header
    for i in range(my_list.counter):
        result.append(pointer.value)
        pointer = pointer.next_item
    return result


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.target = MyList()

    def test_append(self):
        self.target.append(Node(3))
        assert self.target.counter == 1
        assert get_all_items(self.target) == [3]

        self.target.append(Node(4))
        assert self.target.counter == 2
        assert get_all_items(self.target) == [3, 4]

        self.target.append(Node(5))
        assert self.target.counter == 3
        assert get_all_items(self.target) == [3, 4, 5]

    def test_get(self):
        self.target.append(Node(3))
        self.target.append(Node(4))
        self.target.append(Node(5))
        assert self.target.get(0) == 3
        assert self.target.get(1) == 4
        assert self.target.get(2) == 5

    def test_remove(self):
        self.target.append(Node(3))
        self.target.append(Node(4))
        self.target.append(Node(5))

        assert self.target.remove(1) == 4
        assert self.target.counter == 2
        assert get_all_items(self.target) == [3, 5]

    def test_remove_header(self):
        self.target.append(Node(3))
        self.target.append(Node(4))
        self.target.append(Node(5))

        assert self.target.remove(0) == 3
        assert self.target.counter == 2
        assert get_all_items(self.target) == [4, 5]

        self.target.append(Node(3))
        assert self.target.counter == 3
        assert get_all_items(self.target) == [4, 5, 3]

        self.target.remove(2)
        assert self.target.counter == 2
        assert get_all_items(self.target) == [4, 5]

    def test_insert(self):
        self.target.append(Node(3))
        self.target.append(Node(4))
        self.target.append(Node(5))

        self.target.insert(1, Node(6))
        assert get_all_items(self.target) == [3, 6, 4, 5]

        self.target.insert(0, Node(2))
        assert get_all_items(self.target) == [2, 3, 6, 4, 5]

        self.target.insert(4, Node(8))
        assert get_all_items(self.target) == [2, 3, 6, 4, 8, 5]


if __name__ == '__main__':
    unittest.main()
