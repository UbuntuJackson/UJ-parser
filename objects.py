from constants_ import*
import math

class Wrapper:
    def __init__(self, reference) -> None:
        self.reference = reference

class Expression:
    def __init__(self, content = []) -> None:
        self.content = content

    def get_tokens(self, lst):
        token_list = []
        for index, i in enumerate(lst):
            if (type(i.reference) == Arithmetic or
                type(i.reference) == RightParen or
                type(i.reference) == LeftParen): #comparison is insufficient, we should not consider the token if it's already added to the memory tree
                if i.reference.node_a is None and i.reference.node_b is None: token_list.append((index, i))
        
        return token_list

    def get_prioritised_token(self, lst): #compare current_token that was parenthesis and former token that was a parenthesis
        prioritised_token = None

        current_paren = None
        former_paren = None

        current_token = None
        former_token = None
        for a, i in enumerate(lst):
            #if type(current_paren) == RightParen and type(current_token[i]) == LeftParen: pass
            #if type(current_token[i]) == RightParen: current_paren = (i)

            
            current_token = i
            #if current_token in characters.PARENTHESES: current_paren = current_token

            if former_token is not None:
                if current_token[1].reference.priority > prioritised_token[1].reference.priority:
                    prioritised_token = i
            else:
                prioritised_token = i
            former_token = current_token
            former_paren = current_paren

        return prioritised_token

    def refresh_list(self, _op_index, lst):
        new_lst = []

        #expr = Wrapper(lst[_op_index].reference.operator, lst[_op_index-1], lst[_op_index+1])
        for index, i in enumerate(lst):
            
            if index == _op_index -1: continue
            if index == _op_index +1: continue
            if index == _op_index:
                expr = Arithmetic(lst[index].reference.operator, lst[index-1], lst[index+1])
                new_lst.append(expr)
            else:
                new_lst.append(i.reference)
            
        return new_lst

    def pack(self):

        while len(self.content) > 1:
            token_list = self.get_tokens(self.content)
            prioritised_token = self.get_prioritised_token(token_list)
            self.content = self.refresh_list(prioritised_token[0], self.content)
        
        self.content = self.content[0]
        
    
    def pack_parentheses(self):
        pass
    
    def op(self):
        self.pack()
        return self.content.op()

class Arithmetic:
    def __init__(self, operator, node_a = None, node_b = None) -> None:
        self.node_a = node_a
        self.node_b = node_b
        self.operator = operator

        self.priority = None

        self.expectations = ["number", "arithmetic", "left_paren"]
        self.pending_expectation = []

        for a, i in enumerate(characters.TOKENS):
            if self.operator == i: self.priority = a 

    def resolve_expectation(self):
        pass

    def op(self):
        

        if self.operator == "+":
            return Number(self.node_a.op().number + self.node_b.op().number)
        elif self.operator == "-":
            return Number(self.node_a.op().number - self.node_b.op().number)
        elif self.operator == "*":
            return Number(self.node_a.op().number * self.node_b.op().number)
        elif self.operator == "/":
            return Number(self.node_a.op().number / self.node_b.op().number)
        elif self.operator == "^":
            return Number(self.node_a.op().number ** self.node_b.op().number)

class Number:
    def __init__(self, number) -> None:
        if number in characters.constant_table.keys():
            self.number = characters.get_constant(number)
        else:
            self.number = float(number)
    
    def op(self):
        return self


class Parentheses(Expression):
    def __init__(self, content = []) -> None:
        super().__init__(content)
    def op(self):
        self.pack()
        return self.content.op() #alrady a number
        

    
class LeftParen:
    def __init__(self) -> None:
        self.index = 1
        self.expectations = ["number", "arithmetic"]
        self.pending_expectation = ["right_paren"]
    
    def evaluate_expecation(self, arg = None):
        pass

    def resolve_expectation(self):
        pass

class RightParen:
    def __init__(self) -> None:
        self.index = 2
        self.expectations = ["number", "arithmetic", "end of exp"]
    
    def evaluate_expectation(self, arg = "end_of_exp"):
        if arg == "end_of_exp": return ("end_of_exp" in self.expectations) #if returns true, then we're fine

class PrioritisedToken:
    def __init__(self) -> None:
        self.index = None

class ParenthesesToken:
    def __init__(self, index_left, index_right) -> None:
        self.index_left = None
        self.index_right = None
    def op(self):
        self.content = self.pack(self.content)[0]
        return math.sin(self.content)

class SingleArgumentToken:
    def __init__(self, content) -> None:
        self.index = 0
        self.content = content

class Sin(SingleArgumentToken, Expression):
    def __init__(self, content = []) -> None:
        super().__init__(content)
    def op(self):
        self.pack()
        return Number(math.sin(self.content.op().number))

class Cos(SingleArgumentToken, Expression):
    def __init__(self, content = []) -> None:
        super().__init__(content)
    def op(self):
        self.pack()
        return Number(math.cos(self.content.op().number))

class Sqrt(SingleArgumentToken, Expression):
    def __init__(self, content = []) -> None:
        super().__init__(content)
    def op(self):
        self.pack()
        return Number(math.sqrt(self.content.op().number))
