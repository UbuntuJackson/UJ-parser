from procedures import*
from constants_ import*

def main():
    inp_ = input("Type here: ")

    for i in inp_:
        if not (i in characters.DIGITS or i in characters.TOKENS):
            print("INVALID CHARACTERS")
            return

    procedure = Procedure()
    made_list = procedure.to_list(inp_)

    while len(made_list) > 1:
        token_list = procedure.get_tokens(made_list)
        prioritised_token = procedure.get_prioritised_token(token_list)
        made_list = procedure.pack(prioritised_token[0], made_list)
    
        #print(made_list)
    
    result = None

    while made_list[0].reference.type != "number":
        procedure.resolve_tree(made_list[0])

    print(made_list[0].reference.number)
    

main()