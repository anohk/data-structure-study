class Node:
    def __init__(self, data):
        pass


class OrderedList:

    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    # 프린트하는 함수를 따로 지정해주지 않으면, 노드를 돌면서 데이터 객체 그대로 print 한다.
    # 프린트하는 함수를 지정하면, 노드를 돌면서 해당 함수에 데이터 객체를 넘긴다.
    def print_all(self, special_print_function=None):
        pass

    # TODO search 메소드에서 iterator 패턴을 사용할 것

    # return : Tuple of (matching node, previous node).
    # matching node : Key에 정확히 대응하는 노드
    # previous node : macthing node가 있을 때는 이전 노드. 없을 때는, key가 삽입된다면 해당 노드의 이전 노드가 될 노드
    def search(self, key):
        pass

    # TODO insert, remove, retrieve 메소드에서 search 메소드를 사용할 것

    # return : 성공 여부 boolean type
    def insert(self, data):
        pass

    # return : 지워진 데이터. 없을 경우 None
    def remove(self, key):
        pass

    # return : key에 대응하는 데이터. 없을 경우 None
    def retrieve(self, key):
        pass

    def is_empty(self):
        pass
