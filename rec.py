from turtle import Turtle, Vec2D, position

OPS: set = {
    'F',
    'f',
    '+',
    '-',
    ']',
    '[',
}

RULES: dict[str, str] = {
    # 'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
    'f': 'ffffff',
    'L': 'LF+RFR+FL-F-LFLFL-FRFR+',
    'R': '-LFLF+RFRFR+F+RF-LFL-FR',
    # 'F': 'F-FG+F+FG-F',
    # 'F': 'F+F-F-F+F',
    'G': 'FGFG',
    'X': 'F+[[X]-X]-F[-FX]+X',
    # 'X': 'F[+X][-X]FX',
    'F': 'FF',
    '+': '+',
    '-': '-',
    '[': '[',
    ']': ']',
}

ITERATIONS: int = 7
STEPS: int = 3
ANGLE: int | float = 25.7
"""
#DEFINE N 5
#DEFINE A 90
w -> F-F-F-F
#DEFINE w F-F-F-F
#DEFINE F F-FF--F-F
"""


def moveTurtle(commands: str) -> None:
    t: Turtle = Turtle()
    t.speed("fastest")
    t.screen.tracer(0, 0)
    positions = []
    angles = []
    t.setheading(90)
    t.goto(0, -200)
    for command in commands:
        t.screen.update()
        if command == "F":
            t.down()
            t.forward(STEPS)
            t.up()
        elif command == "f":
            t.forward(STEPS)
        elif command == "+":
            t.left(ANGLE)
        elif command == "-":
            t.right(ANGLE)
        elif command == "[":
            positions.append(t.pos())
            angles.append(t.heading())
        elif command == "]":
            t.goto(positions.pop())
            t.setheading(angles.pop())
        elif command.lower() not in OPS:
            continue
        else:
            exit(1)
    t.hideturtle()
    t.screen.mainloop()


def createString(input: str, iter: int) -> str:
    if (iter == 0):
        return input
    new: str = "".join(map(lambda x: RULES[x], [x for x in input]))
    return createString(new, iter=iter-1)


if __name__ == "__main__":
    print(createString("X", ITERATIONS))
    moveTurtle(createString("X", ITERATIONS))
