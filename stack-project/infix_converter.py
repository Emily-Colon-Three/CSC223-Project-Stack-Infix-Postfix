"""InfixToPostfixConverter is a class created with the function of converting an Infix
expression to a Postfix one. It does not contain data members or properties."""
from stack import Stack

class InfixToPostfixConverter:
    def __init__(self): # There is no unique data held in an object of the class.
        pass

    def precedence(self, operator):
        if operator in "*/":
            return 2
        elif operator in "+-":
            return 1
        else: # Operator is none of the above
            raise ValueError("Unexpected operator")

    def is_operand(self, character) -> bool:
        if character.isalnum(): # Checks that a character is alphanumeric, either a number or letter
            return True
        else:
            return False