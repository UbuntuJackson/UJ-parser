import json
from constants_ import*
from disp_user_data import*
from procedures import*

class CommandManager:
    def __init__(self) -> None:
        self.commands = ["save"]

    def command(_inp):
        pass
    
    def is_arithmetic_token(self, _text):
        if _text in characters.TOKENS: return True
        return False

    def ufo_is_letter_or_digit(self, _ch):
        if _ch in characters.DIGITS or _ch in characters.LETTERS: return True
        return False

    def command_cut_off(self, char_1, char_2, _chunk = None):
        if char_1 == " ": return True

        if char_1 == '=': return True

        if char_1 == ",": return True

        if ((self.ufo_is_letter_or_digit(char_1) or self.is_arithmetic_token(char_1) or char_1 == '(' or char_1 == ')') and
            not (self.ufo_is_letter_or_digit(char_2) or self.is_arithmetic_token(char_2) or char_2 == '(' or char_2 == ')')
            ):
            return True
        
        if (not (self.ufo_is_letter_or_digit(char_1) or self.is_arithmetic_token(char_1) or char_1 == '(' or char_1 == ')') and
            (self.ufo_is_letter_or_digit(char_2) or self.is_arithmetic_token(char_2) or char_2 == '(' or char_2 == ')')
            ):
            return True
        
        #if self.is_arithmetic_token(char_1): return True

        return False

    def command_divide_into_chunks(self, _inp):
        outp = []
        chunk = ""
        for a,i in enumerate(_inp):
            if i != " ": chunk += i
            if a == len(_inp) -1:

                outp.append(chunk)
                break

            if self.command_cut_off(_inp[a], _inp[a+1]) and chunk != '':
                outp.append(chunk)
                chunk = ""
        return outp
    
    def assign(self, var, exp):
        user_data.user_vars[var] = float(exp)