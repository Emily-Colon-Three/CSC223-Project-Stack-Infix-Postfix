"""InfixToPostfixConverter is a class created with the function of converting an Infix
expression to a Postfix one. It does not contain data members or properties.
The bulk of the class's function is contained in the infix_to_postfix() method, which
keeps an InfixToPostfixConverter object reusable for multiple conversions.
In infix_to_postfix, an infix expression is passed in as an argument, particularly a string,
and then a holding Stack and output list are created, both empty, in order to carry out the
Shunting-Yard algorithm.
Class contains two supporting methods, precendence() and is_operand(). The former returns
an integer for the precedence of an operator, whereas is_operand() determines whether a
given character is an operand, returning a bool that is True if an operand. Both take a
character as input. precedence() contains error handling for if it is used for a non-operator
character, raising ValueError in such a case."""
from stack import Stack

class InfixToPostfixConverter:
    def __init__(self): # There is no unique data held in an object of the class.
        pass

    def infix_to_postfix(self, infix: str):
        holding = Stack()
        output = []
        for ch in infix.replace(" ", ""): # Goes through each character of infix, barring spaces
            if self.is_operand(ch):
                output.append(ch)

            elif ch == '(':
                holding.push(ch)

            elif ch == ')': # When a ) character encountered, drain holding stack until ( found
                while not holding.is_empty():
                    if holding.peek() != "(":
                        output.append(holding.pop())
                    else:
                        break

                if holding.is_empty():
                    raise ValueError("Mismatched parentheses")
                else:
                    holding.pop() # Discards the ( character that terminates while loop

            else: # Token MUST be operator
                while not holding.is_empty(): # Inner condition can't run if holding stack empty; prevents error.
                    if self.precedence(holding.peek()) > self.precedence(ch):
                        output.append(holding.pop())
                    else:
                        break
                holding.push(ch)
        while not holding.is_empty(): # Loop which drains holding stack into output
            output.append(holding.pop())

        if '(' in output: # If '(' remains in output list, there was no matching ')'
            raise ValueError("Mismatched parentheses")

        return " ".join(output) # Output is put into more readable format, given spaces

    def precedence(self, operator) -> int:
        if operator in "*/": # Multiplication or division
            return 2
        elif operator in "+-": # Addition or subtraction
            return 1
        elif operator in "()": # Extra case for when parentheses left in holding stack
            return 0
        else: # Operator is none of the above; Should not be in expression.
            raise ValueError("Invalid Operator")

    def is_operand(self, character) -> bool:
        if character.isalnum(): # Checks that a character is alphanumeric, either a number or letter
            return True
        else:
            return False

# Testing
import unittest

# Tests that a series of valid infix expressions are properly converted to postfix.
class ConversionCases(unittest.TestCase):
    def setUp(self):
        self.converter = InfixToPostfixConverter()

        self.case1 = "A + B"
        self.case2 = "A * B + C"
        self.case3 = "A - B / C"
        self.case4 = "( A + B ) * C"
        self.case5 = "( A * B ) / ( C + D )"
        self.case6 = "A - ( ( B + C ) / D )"

    def test_cases(self):
        self.assertEqual(self.converter.infix_to_postfix(self.case1), "A B +")
        self.assertEqual(self.converter.infix_to_postfix(self.case2), "A B * C +")
        self.assertEqual(self.converter.infix_to_postfix(self.case3), "A B C / -")
        self.assertEqual(self.converter.infix_to_postfix(self.case4), "A B + C *")
        self.assertEqual(self.converter.infix_to_postfix(self.case5), "A B * C D + /")
        self.assertEqual(self.converter.infix_to_postfix(self.case6), "A B C + D / -")

# Tests that certain cases of invalid expressions raise errors
class InvalidExpressions(unittest.TestCase):
    def setUp(self):
        self.converter = InfixToPostfixConverter()

    def test_parentheses(self):
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("A + B ) * C")

        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("( A + B * C")

        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix(") A + B ( * C")

    def test_invalid_tokens(self):
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("A + B ; C")
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("A @ B + C")

    def test_wrong_order(self):
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("A B +")
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("+ A B - C")
        with self.assertRaises(ValueError):
            self.converter.infix_to_postfix("A + - B")