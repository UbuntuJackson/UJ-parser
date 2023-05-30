from procedures import*
from constants_ import*
from debug_features import*
#from command_manager import*

application_name = "UFO-Parser"

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

        if 'q' == inp_:
            break
        if 'd' == inp_:
            debug_ent.show_debug_info = not debug_ent.show_debug_info
            if debug_ent.show_debug_info: print("[!] Debugging-info enabled")
            else: print("[!] Debugging-info disabled")
            continue
        if inp_ == "constants":
            characters.display_const_table = not characters.display_const_table
            continue
        
        #command = CommandManager()
        #res = command.command_divide_into_chunks(inp_)
        #print(res)
        #continue

        chunk_list = parser.ufo_divide_into_chunks(inp_)

        made_list = parser.ufo_evaluate_chunks(chunk_list)
        print(made_list)
        tok = [0]
        tok = parser.get_paren_tokens(made_list)

        while len(tok) != 0:
            tok = parser.get_paren_tokens(made_list)
            pri_paren = parser.get_prioritised_paren(tok)
            res = parser.pack_prioritised_paren(pri_paren, made_list)
            #print(res.reference.content)
            made_list = parser.make_new_list(made_list, res, pri_paren)
            tok = parser.get_paren_tokens(made_list)
            if len(tok) == 0: break

        expr = Expression(made_list)

        ans = expr.op()
        print(ans.number)

        """while len(pri_paren) != 0:
            tok = procedure.get_paren_tokens(made_list)
            pri_paren = procedure.get_prioritised_paren(tok)
            #made_list = procedure.pack_paren_token(pri_paren)

            pass #parentheses expressions found"""

        #print([i.reference for i in made_list])

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