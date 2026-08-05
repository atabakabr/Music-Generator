import random
import string

class Grammar:

    def __init__(self):
        self.rules = {}

    def load(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                left, rest = line.split("->")
                right, prob = rest.split("|")

                left = left.strip()
                symbols = right.strip().split()
                probability = float(prob.strip())

                if left not in self.rules:
                    self.rules[left] = []

                self.rules[left].append((symbols, probability))


    def add_rule(self, left, right, probability):
        if left not in self.rules:
            self.rules[left] = []

        self.rules[left].append((right, probability))

    def get_rules(self, non_terminal):

        return self.rules.get(non_terminal, [])

        
    def choose_rule(self, non_terminal):

        rules = self.get_rules(non_terminal)

        choices = [rule[0] for rule in rules]

        weights = [rule[1] for rule in rules]

        return random.choices(
            choices,
            weights=weights,
            k=1
        )[0]

    def is_non_terminal(self, symbol):
        return symbol in self.rules