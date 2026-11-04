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