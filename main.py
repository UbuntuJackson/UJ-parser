from procedures import*
from constants_ import*
from debug_features import*

application_name = "uj-parser"

def main():

    while True:
        print("\n########################## " + application_name + " ###########################\n")
        print("[!] Press q and hit ENTER to quit\n")

        inp_ = input("Type here: ")

        if inp_ == "":
            print("Invalid: No string")
            continue

        if 'q' in inp_:
            break
        if 'd' in inp_:
            debug_ent.show_debug_info = not debug_ent.show_debug_info
            if debug_ent.show_debug_info: print("[!] Debugging-info enabled")
            else: print("[!] Debugging-info disabled")
            continue

        #for i in inp_:
        #    if not (i in characters.DIGITS or i in characters.TOKENS):
        #        print("INVALID CHARACTERS")
        #        return

        procedure = Procedure()
        made_list = procedure.to_list(inp_)

        while len(made_list) > 1:
            token_list = procedure.get_tokens(made_list)
            prioritised_token = procedure.get_prioritised_token(token_list)
            made_list = procedure.pack(prioritised_token[0], made_list)
        
            #print(made_list)

        if debug_ent.show_debug_info: debug_ent.print_tree(made_list[0])

        while made_list[0].reference.type != "number":
            procedure.resolve_tree(made_list[0])

        print("(=) " + str(made_list[0].reference.number))
    

main()