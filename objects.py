from constants_ import*
import math

class Wrapper:
    def __init__(self, reference) -> None:
        self.reference = reference

class Expression:
    def __init__(self, content) -> None:
        self.content = content
    def pack(self, _op_index, lst):
        new_lst = []

        #expr = Wrapper(lst[_op_index].reference.operator, lst[_op_index-1], lst[_op_index+1])
        for index, i in enumerate(lst):
            
            if index == _op_index -1: continue
            if index == _op_index +1: continue
            if index == _op_index:
                expr = Wrapper(Arithmetic(lst[index].reference.operator, lst[index-1], lst[index+1]))
                new_lst.append(expr)
            else:
                new_lst.append(i)
            
        return new_lst

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


class Parentheses(Expression):
    def __init__(self, content = None) -> None:
        self.content = content
    def op(self):
        self.content = self.pack(self.content)
        return self.content

    
class LeftParen:
    def __init__(self) -> None:
        self.index = 1
class RightParen:
    def __init__(self) -> None:
        self.index = 2

class PrioritisedToken:
    def __init__(self) -> None:
        self.index = None

class ParenthesesToken:
    def __init__(self, index_left, index_right) -> None:
        self.index_left = None
        self.index_right = None

class SingleArgumentToken:
    def __init__(self, content = None) -> None:
        self.content = content
        self.index = 0

class Sin(SingleArgumentToken, Expression):
    def __init__(self, content = None) -> None:
        super().__init__()
    def op(self):
        self.content = self.pack(self.content)
        return math.sin(self.content)

class Cos(SingleArgumentToken, Expression):
    def __init__(self, content = None) -> None:
        super().__init__()
    def op(self):
        self.content = self.pack(self.content)
        return math.cos(self.content)

class Sqrt(SingleArgumentToken, Expression):
    def __init__(self, content = None) -> None:
        super().__init__()
    def op(self):
        self.content = self.pack(self.content)
        return math.sqrt(self.content)
