class DispUserData:
    def __init__(self) -> None:
        self.user_vars = {}
    def parse_var_expr(self, expr):
        for a, i in enumerate(expr):
            if i == '=':
                self.user_vars[expr[:a]] = expr[a+1:]

d = DispUserData()

inp = input()

d.parse_var_expr(inp)

print(d.user_vars)