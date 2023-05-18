class ConstLists:
    def __init__(self) -> None:
        self.TOKENS = "+-*/^"
        self.DIGITS = "0123456789."
        self.PARENTHESES = "()"
        self.LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        self.constant_table = {
            "g" : 9.82,
            "coulumb_constant" : 8.9875517923 * 10 ** 9
        }

    def get_constant(self, _const):
        return self.constant_table[_const]

characters = ConstLists()