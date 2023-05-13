from constants_ import*

class Wrapper:
    def __init__(self, reference) -> None:
        self.reference = reference

class Expression:
    def __init__(self, operator, node_a = None, node_b = None) -> None:
        self.node_a = node_a
        self.node_b = node_b
        self.operator = operator
        self.type = "expression"
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
        self.number = float(number)
        self.type = "number"