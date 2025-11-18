from typing import Any, Dict, List, Tuple
from turtle import Turtle
from random import uniform, choices
from classes.Context import Context
from classes.NoRuleFoundException import NoRuleFoundException
import tomllib


class DOL:
    ops: List[str] = [
        'F', 'f', '+', '-', '^', '&', '\\', '/', '|', '$', '[', ']', '{', 'G',
        '.', '~', '!', '`', '%'
    ]
    rules: Dict[str, str]
    probs: Dict[str, Dict[str, Any]] = {}
    contexts: Dict[Tuple[str], str] = {}
    ignores: List[str] = []
    contextBased: bool = False
    iterations: int
    angle: float
    steps: int
    axiom: str
    commands: str

    def __init__(self, configuration_file: str) -> None:
        self.parseTOML(configuration_file)

    def parseTOML(self, configuration_file: str) -> None:
        """
        Parse the TOML configuration file to configure the turtle to be moved

        :params self: object - this object
        :params configuration_file: str - the toml file to be read out
        """
        try:
            with open(configuration_file, "rb") as configuration:
                data: Dict[str, Any] = tomllib.load(configuration)
                self.iterations = data['system']['iterations']
                self.angle = data['system']['angle']
                self.steps = data['system']['steps']
                self.axiom = data['system']['axiom']
                self.commands = self.axiom

                self.rules = data['rules']
                if "probabilities" in data:
                    self.probs = data['probabilities']
                if "contexts" in data:
                    for symbol, rules in data['contexts'].items():
                        print("Contexts:", self.contexts)
                        print("Rules being applied:", rules)
                        self.contexts[symbol] = {}
                        for rule in rules:
                            if rule['rule'] not in self.rules:
                                raise NoRuleFoundException()
                            left = rule['left'] if rule['left'] != "*" else None
                            right = rule['right'] if rule['right'] != "*" else None
                            key = (left, symbol, right)
                            self.contexts[symbol][key] = self.rules.get(rule['rule'], None)
                if "ignore" in data['system']:
                    self.ignores = data['system']['ignore']
                if "context" in data['system']:
                    self.contextBased = data['system']['context']
        except IOError:
            print("Could not read", configuration_file)

    def _setRule(self, rule: str) -> str:
        if rule in self.rules:
            return self.rules[rule]
        elif rule in self.probs:
            probabilities = [float(x['probability']) for x in self.probs[rule]]
            rules = [x for x in self.rules]
            return self.rules[choices(rules, probabilities)[0]]
        else:
            return rule

    def _applyContextRules(self, axiom: str) -> str:
        output = []
        n = len(axiom)

        for i in range(n):
            symbol = axiom[i]

            if symbol in self.ignores:
                output.append(symbol)
                continue

            left_context = None
            for j in range(i - 1, -1, -1):
                if axiom[j] not in self.ignores:
                    left_context = axiom[j]
                    break

            right_context = None
            for j in range(i + 1, n):
                if axiom[j] not in self.ignores:
                    right_context = axiom[j]
                    break

            matched_rule = False
            for (left, center, right), replacement in self.contexts.get(symbol, {}).items():
                if (left == left_context or left == "*") and \
                   (center == symbol) and \
                   (right == right_context or right == "*"):
                    output.append(replacement)
                    matched_rule = True
                    break

            if not matched_rule:
                output.append(symbol)

        return ''.join(output)

    def createString(self, axiom: str, n: int) -> str:
        """
        Create the string for the turtle to use to create beautiful images
        It is based on production rules like, a creates ab and b creates a
        which makes a ab aba abaab, ....

        :params self: object - this object
        :params axiom: str - the starting point (like a)
        :params n: int - the amount of iterations it needs to do
        """
        if (n == 0):
            return axiom
        if self.contextBased:
            output = axiom
            for _ in range(self.iterations):
                output = Context.apply_context(output, self.contexts, self.ignores)
            return output
        else:
            new: str = "".join(self._setRule(x) for x in axiom)
            self.commands = new
            return self.createString(new, n=n-1)

    def moveTurtle(self) -> None:
        commands: str = self.createString(self.axiom, self.iterations)
        t: Turtle = Turtle()
        t.speed("fastest")
        t.screen.tracer(0, 0)
        positions = []
        angles = []
        t.setheading(90)
        for command in commands:
            t.screen.update()
            if command == "F":
                t.down()
                t.forward(self.steps)
                t.up()
            elif command == "G":
                t.down()
                t.forward(self.steps)
                t.up()
            elif command == "f":
                t.forward(self.steps)
            elif command == "+":
                t.left(self.angle)
            elif command == "-":
                t.right(self.angle)
            elif command == "[":
                positions.append(t.pos())
                angles.append(t.heading())
            elif command == "]":
                t.color((0, uniform(0, 1), 0))
                t.goto(positions.pop())
                t.setheading(angles.pop())
            elif command.lower() not in self.ops:
                continue
            else:
                exit(1)
        t.hideturtle()
        t.screen.mainloop()
