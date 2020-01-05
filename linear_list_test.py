import unittest


class MyList:

    def __init__(self):
        self.list = {}
        self.counter = 0

    def append(self, element):
        self.list[self.counter] = element
        self.counter += 1

    def retrieve(self):
        return self.list[0]


class MyTestCase(unittest.TestCase):

    # myList ADT
    # set of elements
    # append
    # retrieve : return first element

    def setUp(self) -> None:
        self.target = MyList()

    def test_something(self):
        # append
        self.target.append(0)
        self.target.append(1)

        # retrieve
        assert self.target.retrieve() == 0


if __name__ == '__main__':
    unittest.main()
