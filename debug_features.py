from objects import*

class DebuggningFeatures:
    def __init__(self) -> None:
        self.show_debug_info = False
        self.pr_depth = ""
        self.indent = "  "
    
    def print_tree(self, _exp_tree, _node_name = ""):
        self.pr_depth += self.indent
        if _node_name == "": print("Tree:\n")
        if type(_exp_tree.reference) == Arithmetic:
            if _node_name != "": print(self.pr_depth + _node_name)
            if type(_exp_tree.reference.node_a.reference) == Arithmetic:
                self.print_tree(_exp_tree.reference.node_a, "node_a: ")
            elif type(_exp_tree.reference.node_a.reference) == Number:
                self.print_tree(_exp_tree.reference.node_a, "node_a: ")
            
            print(self.pr_depth + "|  |")
            print(self.pr_depth + "--" + "(" + _exp_tree.reference.operator + ")")
            print(self.indent + self.pr_depth + " |")

            if type(_exp_tree.reference.node_b.reference) == Arithmetic:
                self.print_tree(_exp_tree.reference.node_b, "node_b: ")
            elif type(_exp_tree.reference.node_b.reference) == Number:
                self.print_tree(_exp_tree.reference.node_b, "node_b: ")

        elif type(_exp_tree.reference) == Number:
            print(self.pr_depth + _node_name + str(_exp_tree.reference.number))
            if _node_name == "node_b: ": print("")
        
        elif _node_name == "single_argument_expression":
            pass

        
        self.pr_depth = self.pr_depth[:-2]


debug_ent = DebuggningFeatures()