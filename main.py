from procedures import*

def main():
    procedure = Procedure()
    made_list = procedure.to_list("3+3.3-3*2+1")

    
    #print(packed_list)
    #result = procedure.resolve_tree(packed_list[-1])
    #print(result.number)


    while len(made_list) > 1:
        token_list = procedure.get_tokens(made_list)
        prioritised_token = procedure.get_prioritised_token(token_list)
        made_list = procedure.pack(prioritised_token[0], made_list)
    
        print(made_list)
    
    result = None

    while made_list[0].reference.type is not "number":
        procedure.resolve_tree(made_list[0])

    print(made_list[0].reference.number)
    

main()