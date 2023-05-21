from constants_ import*
import math

class Wrapper:
    def __init__(self, reference) -> None:
        self.reference = reference

class Arithmetic:
    def __init__(self, operator, node_a = None, node_b = None) -> None:
        self.node_a = node_a
        self.node_b = node_b
        self.operator = operator

        self.priority = None
        
        for a, i in enumerate(characters.TOKENS):
            if self.operator == i: self.priority = a 

    def op(self):
        if self.operator == "+":
            return Number(self.node_a.reference.number + self.node_b.reference.number)
        elif self.operator == "-":
            return Number(self.node_a.reference.number - self.node_b.reference.number)
        elif self.operator == "*":
            return Number(self.node_a.reference.number * self.node_b.reference.number)
        elif self.operator == "/":
            return Number(self.node_a.reference.number / self.node_b.reference.number)
        elif self.operator == "^":
            return Number(self.node_a.reference.number ** self.node_b.reference.number)

class Number:
    def __init__(self, number) -> None:
        if number in characters.constant_table.keys():
            self.number = characters.get_constant(number)
        else:
            self.number = float(number)


class Parentheses:
    def __init__(self, content = None) -> None:
        self.content = content

    
class LeftParen:
    def __init__(self) -> None:
        pass
class RightParen:
    def __init__(self) -> None:
        pass

class PrioritisedToken:
    def __init__(self) -> None:
        self.index = None

class ParenthesesToken:
    def __init__(self, index_left, index_right) -> None:
        self.type = "paren_oken"
        self.index_left = None
        self.index_right = None

class Sin:
    def __init__(self, content = None) -> None:
        self.content = content
    def op(self):
        return math.sin(self.content)

class Cos:
    def __init__(self, content = None) -> None:
        self.content = content
    def op(self):
        return math.sin(self.content)

class Sqrt:
    def __init__(self, content = None) -> None:
        self.content = content
    def op(self):
        return math.sin(self.content)
