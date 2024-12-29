from typing import Any, Dict, List
from turtle import Turtle
from random import uniform, choices
import tomllib


class DOL:
    ops: List[str] = [
        'F', 'f', '+', '-', '^', '&', '\\', '/', '|', '$', '[', ']', '{', 'G',
        '.', '~', '!', '`', '%'
    ]
    rules: Dict[str, str]
    probs: Dict[str, Dict[str, Any]] = {}
    iterations: int
    angle: float
    steps: int
    axiom: str

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

                self.rules = data['rules']
                if "probabilities" in data:
                    self.probs = data['probabilities']
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
        new: str = "".join(map(self._setRule, [x for x in axiom]))
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
