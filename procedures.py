from objects import*

class Procedure:
    def __init__(self) -> None:
        self.TOKENS = "+-*/^"
        self.DIGITS = "0123456789."
    
    def to_list(self, _inp):
        output = []
        text_chunk = ""
        current_char = None
        former_char = None
        for a,i in enumerate(_inp):
            current_char = i
            
            if current_char in self.TOKENS:
                output.append(Wrapper(Number(text_chunk)))
                text_chunk = ""
                output.append(Wrapper(Expression(current_char)))
            elif current_char in self.DIGITS:
                text_chunk += current_char
            
            if a == len(_inp)-1:
                output.append(Wrapper(Number(text_chunk)))

            #former_char = current_char
        
        return output
    
    def get_tokens(self, lst):
        token_list = []
        for index, i in enumerate(lst):
            if i.reference.type == "expression": #comparison is insufficient, we should not consider the token if it's already added to the memory tree
                if i.reference.node_a is None and i.reference.node_b is None: token_list.append((index, i))
        
        return token_list
                

    def get_prioritised_token(self, lst):
        prioritised_token = None
        current_token = None
        former_token = None
        for a, i in enumerate(lst):
            current_token = i
            if former_token is not None:
                if current_token[1].reference.priority > prioritised_token[1].reference.priority:
                    prioritised_token = i
            else:
                prioritised_token = i
            former_token = current_token

        return prioritised_token
            

            
    
    def pack(self, _op_index, lst):
        new_lst = []
        for index, i in enumerate(lst):
            if index == _op_index -1: continue
            if index == _op_index +1: continue
            if index == _op_index:
                expr = Wrapper(Expression(lst[index].reference.operator, lst[index-1], lst[index+1]))
                new_lst.append(expr)
            else:
                new_lst.append(i)
        return new_lst
    
    def resolve_tree(self, _exp_tree):

        if _exp_tree.reference.node_a.reference.type == "expression":
            self.resolve_tree(_exp_tree.reference.node_a)
            #print("resolve node a")
        if _exp_tree.reference.node_b.reference.type == "expression":
            self.resolve_tree(_exp_tree.reference.node_b)
            #print("resolve node b")
        
        if _exp_tree.reference.type == "expression" and _exp_tree.reference.node_a.reference.type == "number" and _exp_tree.reference.node_b.reference.type == "number":
            #print("makes number")
            _exp_tree.reference = _exp_tree.reference.op()