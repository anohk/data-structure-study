"""
Implement a function that checks if a string has correct brace pairs(i.e. (, {, [) .
 Use your Stack ADT.
 If the source code has correct pairs, print ‘yes’.
 If the function find a wrong brace, print ‘no’.
 You have to check all kinds of brace ‘( )’, ‘{ }’, ‘[ ]’.
 Input : a single line of characters.
"""

import unittest

from .stack import MyStack as Stack

braces = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def check_brace(input_string):
    stack = Stack()
    for char in input_string:
        if char in braces.keys():
            stack.push(char)
        elif char in braces.values():
            if stack.count > 0 and char == braces[stack.top.data]:
                stack.pop()
            elif stack.count == 0 or char != braces[stack.top.data]:
                return 'no'

    if stack.count == 0:
        return 'yes'
    else:
        return 'no'


class BraceCheckTestCase(unittest.TestCase):

    def test_check_brace(self):
        input_string = '(abc)'
        assert check_brace(input_string) == 'yes'

    def test_check_brace_wrong(self):
        input_string = '((abc)'
        assert check_brace(input_string) == 'no'

        input_string = ')(abc)'
        assert check_brace(input_string) == 'no'

    def test_check_multiple_brace(self):
        assert check_brace('So when I die (the [first] I will see in (heaven) is a score list).') == 'yes'
        assert check_brace('[ first in ] ( first out ).') == 'yes'
        assert check_brace('([ (([( [ ] ) ( ) (( ))] )) ]).') == 'yes'

        assert check_brace('Half Moon tonight (At least it is better than no Moon at all]).') == 'no'
        assert check_brace('A rope may form )( a trail in a maze.') == 'no'
        assert check_brace('Help( I[m being held prisoner in a fortune cookie factory)].') == 'no'
        assert check_brace('{](( )} (( ))] )) ]).') == 'no'


if __name__ == '__main__':
    unittest.main()
