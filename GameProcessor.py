from random import randint


class DigitsGame:
    def __init__(self):
        self.number = ""
        self.turn = 0
        self.started = False

    def start(self):
        self.number = self.generate_number()
        self.turn = 0
        self.started = True

    def check(self, num):
        num = str(num)

        on_place = 0
        out_place = 0

        for ind, digit in enumerate(num):
            if self.number[ind] == digit:
                on_place += 1
            elif digit in self.number:
                out_place += 1

        self.turn += 1

        return self.turn, num, on_place, out_place

    def generate_number(self):
        variants = list(range(0, 10))
        out = ""

        for _ in range(4):
            out += str(variants.pop(randint(0, len(variants) - 1)))

        return out
