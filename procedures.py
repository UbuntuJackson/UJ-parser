from objects import*
from constants_ import*

class Procedure:
    def __init__(self) -> None:
        pass
    
    def is_valid_value(self, _text):
        if _text in characters.OTHER_TOKENS: return False
        if '(' in _text or ')' in _text: return False
        return True
    
    def is_letter_or_digit(self, _ch):
        if _ch in characters.DIGITS or _ch in characters.LETTERS: return True
        return False

    def is_token(self, _text):
        if _text in characters.OTHER_TOKENS or _text in characters.TOKENS: return True
        return False
    
    def is_func_token(self, _text):
        if _text in characters.OTHER_TOKENS: return True
        return False
    
    def is_arithmetic_token(self, _text):
        if _text in characters.TOKENS: return True
        return False

    def determine_type(self, _text):
        if self.is_func_token(_text): return Sin(_text)
        if self.is_arithmetic_token(_text): return Arithmetic(_text)
        if all([self.is_number_char(i) for i in _text]): return Number(_text)
    
    def interrupt(self, _text):
        pass
        

    def to_list_2(self, _inp):
        output = []
        text_chunk = ""
        current_char = None
        former_char = None
        for a,i in enumerate(_inp):
            current_char = i
            
            text_chunk += current_char

            if self.is_arithmetic_token(text_chunk):
                output.append(Wrapper(Arithmetic(text_chunk)))
                text_chunk = ""
                continue
            
            if text_chunk == "(":
                output.append(Wrapper(LeftParen()))
                text_chunk = ""
                continue

            if text_chunk == ")":
                output.append(Wrapper(RightParen()))
                text_chunk = ""
                continue

            if a == len(_inp) - 1:
                if self.is_func_token(text_chunk): output.append(Wrapper(Sin()))
                else: output.append(Wrapper(Number(text_chunk)))
                text_chunk = ""

            if a < len(_inp) - 1:
                if not self.is_letter_or_digit(_inp[a + 1]) and self.is_letter_or_digit(current_char):
                    if self.is_func_token(text_chunk):
                        if text_chunk == "sin": output.append(Wrapper(Sin()))
                        elif text_chunk == "cos": output.append(Wrapper(Cos()))
                        elif text_chunk == "sqrt": output.append(Wrapper(Sqrt()))
                    else: output.append(Wrapper(Number(text_chunk)))
                    text_chunk = ""

            former_char = current_char
        
        return output

    def to_list(self, _inp):
        output = []
        text_chunk = ""
        current_char = None
        former_char = None
        for a,i in enumerate(_inp):
            current_char = i
            
            if current_char in characters.TOKENS:
                output.append(Wrapper(Number(text_chunk)))
                text_chunk = ""
                output.append(Wrapper(Arithmetic(current_char)))
            elif current_char in characters.DIGITS or current_char in characters.LETTERS:
                text_chunk += current_char
            elif current_char in characters.PARENTHESES:
                if current_char == '(': output.append(Wrapper(LeftParen()))
                if current_char == ')': output.append(Wrapper(RightParen()))
                #if a == len(_inp)-1: return
            
            if a == len(_inp)-1 and (current_char in characters.DIGITS or current_char in characters.LETTERS):
                output.append(Wrapper(Number(text_chunk)))

            former_char = current_char
        
        return output
    
    def get_tokens(self, lst):
        token_list = []
        for index, i in enumerate(lst):
            if (type(i.reference) == Arithmetic or
                type(i.reference) == RightParen or
                type(i.reference) == LeftParen): #comparison is insufficient, we should not consider the token if it's already added to the memory tree
                if i.reference.node_a is None and i.reference.node_b is None: token_list.append((index, i))
        
        return token_list

    def pair_parentheses(self, _former, _current):
        if _former == "(" and _current == ")": return (_former, _current)
        return None

    def get_paren_tokens(self, lst):
        token_list = []
        for index, i in enumerate(lst):
            if type(i.reference).__base__ == SingleArgumentToken:
                if i.reference.content != []:
                    continue
            if (type(i.reference).__base__ == SingleArgumentToken or
                type(i.reference) == LeftParen or
                type(i.reference) == RightParen):
                token_list.append((index, i))
        
        return token_list

    def get_prioritised_paren(self, lst):
        current_paren = None
        former_paren = None
        paren_exp = []

        for a, i in enumerate(lst):
            if len(paren_exp) == 0:
                paren_exp.append(i)

            elif len(paren_exp) >= 1:
                if paren_exp[-1][1].reference.index < i[1].reference.index:
                    paren_exp.append(i)
                else:
                    paren_exp = []
                    paren_exp.append(i)
            
            if len(paren_exp) != 0:
                if type(paren_exp[-1][1].reference) == RightParen:
                    return paren_exp
        
        return paren_exp

    def get_prioritised_token(self, lst): #compare current_token that was parenthesis and former token that was a parenthesis
        prioritised_token = None

        current_paren = None
        former_paren = None

        current_token = None
        former_token = None
        for a, i in enumerate(lst):
            if type(current_paren) == RightParen and type(current_token[i]) == LeftParen: pass
            if type(current_token[i]) == RightParen: current_paren = (i)
            #if self.pair_parentheses(current_paren, former_paren) is not None:
            #    return self.pair_parentheses(current_paren, former_paren)
            
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
            
    def make_packed_node(self, _prioritised_token, desired_content = []):
        if type(_prioritised_token.reference) == Arithmetic:
            return Wrapper(Arithmetic(_prioritised_token.reference.operator, desired_content[0], desired_content[1]))
        elif type(_prioritised_token.reference) == Parentheses: #unsure of name
            Wrapper(Parentheses(desired_content[0]))
    
    def make_new_list(self, _made_list, _res, _pri_paren):
        new_list = []
        for a, wrapper in enumerate(_made_list):
            if a == _pri_paren[0][0]:
                new_list.append(_res)
            elif a > _pri_paren[0][0] and a <= _pri_paren[-1][0]:
                continue
            else:
                new_list.append(wrapper)
        
        return new_list

    def pack_prioritised_paren(self, _tok_list, lst):
        content = []
        if len(_tok_list) < 2:
            print("<2")
            return
        #print(_tok_list[-2][0]+1, _tok_list[-1][0])
        for i in range(_tok_list[-2][0]+1, _tok_list[-1][0]):
            content.append(lst[i])
        
        if type(_tok_list[0][1].reference) == LeftParen: return Wrapper(Parentheses(content))
        else: return Wrapper(type(_tok_list[0][1].reference)(content))
    
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
    
    def resolve_tree(self, _exp_tree):

        if type(_exp_tree.reference.node_a.reference) == Arithmetic:
            self.resolve_tree(_exp_tree.reference.node_a)
            #print("resolve node a")
        if type(_exp_tree.reference.node_b.reference) == Arithmetic:
            self.resolve_tree(_exp_tree.reference.node_b)
            #print("resolve node b")
        
        if (type(_exp_tree.reference) == Arithmetic and
            type(_exp_tree.reference.node_a.reference) == Number and
            type(_exp_tree.reference.node_b.reference) == Number):
            #print("makes number")
            _exp_tree.reference = _exp_tree.reference.op()