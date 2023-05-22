from procedures import*
from constants_ import*
from debug_features import*

application_name = "uj-parser"

def main():

    while True:
        print("\n########################## " + application_name + " ###########################\n")
        print("[!] Press q and hit ENTER to quit\n")

        if characters.display_const_table:
            characters.print_constant_table()
            print("\n###############################################################################\n")
        

        inp_ = input("Type here: ")

        if inp_ == "":
            print("[!] Invalid: No string")
            continue
        
        """if (not inp_ in characters.commands and
            not any([(letter in inp_) for letter in characters.DIGITS]) and
            not any([(letter in inp_) for letter in characters.TOKENS])):
            print("[!] Invalid, not a command, digit, or token")
            continue"""

        if 'q' in inp_:
            break
        if 'd' in inp_:
            debug_ent.show_debug_info = not debug_ent.show_debug_info
            if debug_ent.show_debug_info: print("[!] Debugging-info enabled")
            else: print("[!] Debugging-info disabled")
            continue
        if inp_ == "constants":
            characters.display_const_table = not characters.display_const_table
            continue

        procedure = Procedure()
        made_list = procedure.to_list_2(inp_)
        tok = procedure.get_paren_tokens(made_list)
        pri_paren = procedure.get_prioritised_paren(tok)

        res = procedure.pack_prioritised_paren(pri_paren, made_list)

        """while len(pri_paren) != 0:
            tok = procedure.get_paren_tokens(made_list)
            pri_paren = procedure.get_prioritised_paren(tok)
            #made_list = procedure.pack_paren_token(pri_paren)

            pass #parentheses expressions found"""

        print(res)

        continue

        while len(made_list) > 1:
            token_list = procedure.get_tokens(made_list)
            prioritised_token = procedure.get_prioritised_token(token_list)
            made_list = procedure.pack(prioritised_token[0], made_list)

        if debug_ent.show_debug_info: debug_ent.print_tree(made_list[0])

        while type(made_list[0].reference) != Number:
            procedure.resolve_tree(made_list[0])

        print("(=) " + str(made_list[0].reference.number))
    

main()