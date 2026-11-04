"""The PostfixEvaluator class is used to find the numeric value of postfix expressions.
This evaluation takes place in the evaluate_postfix() method.
The evaluate_postfix() function takes postfix, a string holding a postfix expression, and
processes it into a series of operations that are executed, utilizing a stack for its
algorithm. It returns an int or float of the evaluated expression. However, if the method
encounters the sign of an error, such as operators not having necessary operands to use,
ValueError will be raised. Additionally, dividing by 0 raises ZeroDivisionError."""
from stack import Stack

class PostfixEvaluator:
    def __init__(self): # No data members, objects reusable across evaluations
        pass

    def evaluate_postfix(self, postfix: str) -> int | float:
        stack = Stack()

        for ch in postfix.split():
            if ch.isdigit():
                stack.push(int(ch))
            else: # ch should be operator
                if stack.size() < 2:
                    raise ValueError("Not enough operands.")

                b = stack.pop()
                a = stack.pop()

                if ch == '+':
                    stack.push(a + b)
                elif ch == '-':
                    stack.push(a - b)
                elif ch == '*':
                    stack.push(a * b)
                elif ch == '/':
                    if b == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    stack.push(a / b)
                else:
                    raise ValueError("Unknown Operator")
        if stack.size() > 1:
            raise ValueError("Too many operands.")
        return stack.pop()

# Testing
import unittest

class ValidPostfix(unittest.TestCase):
    def setUp(self):
        self.evaluator = PostfixEvaluator()

        self.case1 = "5 3 +"
        self.case2 = "8 2 - 3 +"
        self.case3 = "5 3 8 * +"
        self.case4 = "6 2 / 3 +"
        self.case5 = "5 3 8 * + 2 /"

    def test_cases(self):
        self.assertEqual(self.evaluator.evaluate_postfix(self.case1), 8)
        self.assertEqual(self.evaluator.evaluate_postfix(self.case2), 9)
        self.assertEqual(self.evaluator.evaluate_postfix(self.case3), 29)
        self.assertEqual(self.evaluator.evaluate_postfix(self.case4), 6.0)
        self.assertEqual(self.evaluator.evaluate_postfix(self.case5), 14.5)

class InvalidPostfix(unittest.TestCase):
    def setUp(self):
        self.evaluator = PostfixEvaluator()

    def test_insufficient_operands(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("5 +")
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("25 23 + -")

    def test_too_many_operands(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("5 3 6 +")
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("23 28 + 6 8 /")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.evaluator.evaluate_postfix("5 0 /")

    def test_invalid_tokens(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("1 2 %")
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("5 3 * ;")

    def test_malformed(self):
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix("9 + 10")