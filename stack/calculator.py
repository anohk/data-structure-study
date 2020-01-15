"""
 Implement a function that calculates an infix formula.
 Use your Stack ADT.
 Support arithmetic operations (‘+, -, *, /’) and brace (‘( )’).
 Only non-negative single-digit integers are allowed for input.
 If a formula can not be calculated, print error message.
 e.g., divide by zero, invalid formula
 Input: a single line of formula.
"""

import unittest

from .stack import MyStack as Stack

operators = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}
opening_brace = '('
closing_brace = ')'


def calculate_with_operation(operand1, operand2, operation):
    operand1, operand2 = float(operand1), float(operand2)

    if operation is '+':
        return operand1 + operand2
    elif operation is '-':
        return operand1 - operand2
    elif operation is '*':
        return operand1 * operand2
    elif operation is '/':
        if operand2 == 0:
            raise Exception('DIVIDED_BY_ZERO')
        return operand1 / operand2


def calculate_postfix(postfix_formula):
    postfix_formula = postfix_formula.strip()
    numbers = Stack()
    for op in postfix_formula:
        if op.isnumeric():
            numbers.push(op)
        else:
            if numbers.count < 2:
                raise Exception('INVALID_FORMULA')
            operand2 = numbers.pop()
            operand1 = numbers.pop()
            numbers.push(calculate_with_operation(operand1, operand2, op))
    return numbers.top.data


def add_operators(postfix_formula, stack, target):
    if stack.count == 0 or stack.top.data is opening_brace:
        stack.push(target)
        return postfix_formula

    if operators[stack.top.data] >= operators[target]:
        postfix_formula += stack.pop()

    stack.push(target)

    return postfix_formula


def change_to_postfix_formula(infix_formula):
    infix_formula = infix_formula.strip()
    postfix_formula = ''
    stack = Stack()

    for target in infix_formula:
        if target.isnumeric():
            postfix_formula += target

        elif target in operators.keys():
            postfix_formula = add_operators(postfix_formula, stack, target)

        elif target is opening_brace:
            stack.push(target)

        elif target is closing_brace:
            for operator in range(stack.count):
                if stack.top.data is opening_brace:
                    stack.pop()
                    break
                else:
                    postfix_formula += stack.pop()

    while stack.count > 0:
        postfix_formula += stack.pop()

    return postfix_formula


def calculate_infix(infix_formula):
    postfix_formula = change_to_postfix_formula(infix_formula)
    try:
        result = calculate_postfix(postfix_formula)
    except Exception as e:
        return e
    else:
        return result


class CalculateInfixFormulaTestCase(unittest.TestCase):
    def test_calculate_post_fix(self):
        assert calculate_postfix('123*45/-+') == 6.2
        assert calculate_postfix('12345*+*+') == 47

    def test_change_to_postfix_formula(self):
        infix_formula = '1 + 2 * 3 - 4 / 5'
        assert change_to_postfix_formula(infix_formula) == '123*45/-+'
        infix_formula = '(1 + 2) * (3 - 4) / 5'
        assert change_to_postfix_formula(infix_formula) == '12+34-*5/'

    def test_calculate(self):
        infix_formula = '1 + 2 * 3 - 4 / 5'
        assert calculate_infix(infix_formula) == 6.2
        infix_formula = '(1 + 2) * (3 - 4) / 5'
        assert calculate_infix(infix_formula) == -0.6

        infix_formula = '1 + + 2'
        with self.assertRaises(Exception) as context:
            calculate_infix(infix_formula)
            assert context.exception == 'INVALID_FORMULA'

        infix_formula = '1 / (2 - 2)'
        with self.assertRaises(Exception) as context:
            calculate_infix(infix_formula)
            assert context.exception == 'DIVIDED_BY_ZERO'

    # TODO: 이 케이스들에 대해서  postfix_formula 변환 테스트도 작성
    def test_calculate_only_close_bracket(self):
        infix_formula = "3)"
        with self.assertRaises(Exception) as context:
            calculate_infix(infix_formula)
            assert context.exception == 'INVALID_FORMULA'

    def test_calculate_only_number(self):
        infix_formula = "3"
        assert calculate_infix(infix_formula) == 3 

if __name__ == '__main__':
    unittest.main()
