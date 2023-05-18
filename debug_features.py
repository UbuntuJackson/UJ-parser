class DebuggningFeatures:
    def __init__(self) -> None:
        self.show_debug_info = False
        self.pr_depth = ""
        self.indent = "  "
    
    def print_tree(self, _exp_tree, _node_name = ""):
        self.pr_depth += self.indent
        if _node_name == "": print("Tree:\n")
        if _exp_tree.reference.type == "expression":
            if _node_name != "": print(self.pr_depth + _node_name)
            if _exp_tree.reference.node_a.reference.type == "expression":
                self.print_tree(_exp_tree.reference.node_a, "node_a: ")
            elif _exp_tree.reference.node_a.reference.type == "number":
                self.print_tree(_exp_tree.reference.node_a, "node_a: ")
            
            print(self.pr_depth + "|  |")
            print(self.pr_depth + "--" + "(" + _exp_tree.reference.operator + ")")
            print(self.indent + self.pr_depth + " |")

            if _exp_tree.reference.node_b.reference.type == "expression":
                self.print_tree(_exp_tree.reference.node_b, "node_b: ")
            elif _exp_tree.reference.node_b.reference.type == "number":
                self.print_tree(_exp_tree.reference.node_b, "node_b: ")

        elif _exp_tree.reference.type == "number":
            print(self.pr_depth + _node_name + str(_exp_tree.reference.number))
            if _node_name == "node_b: ": print("")
        
        elif _node_name == "single_argument_expression":
            pass

        
        self.pr_depth = self.pr_depth[:-2]


debug_ent = DebuggningFeatures()