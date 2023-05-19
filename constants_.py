class ConstLists:
    def __init__(self) -> None:
        self.display_const_table = False

        self.TOKENS = "+-*/^"
        self.DIGITS = "0123456789."
        self.PARENTHESES = "()"
        self.LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        self.constant_table = {
            "g" : 9.82,
            "coulumb_constant" : 8.9875517923 * 10 ** 9,
            "universal_gravitational_constant" : 6.6743 * 10 ** -11,
            "G": 6.6743 * 10 ** -11,

            "pi" : 3.141592653589,
            "e" : 2.71828,
            "eulers number" : 2.71828,

            "nano" : 10 ** -9,
            "micro" : 10 ** -6,
            "milli" : 10 ** -3,

            "kilo" : 10 ** 3,
            "mega" : 10 ** 6,
            "giga" : 10 ** 9
        }
        self.commands = ["d", "q"]

    def get_constant(self, _const):
        return self.constant_table[_const]
    def print_constant_table(self):
        for k, i in self.constant_table.items():
            print(str(k) + " = " + str(i))

characters = ConstLists()