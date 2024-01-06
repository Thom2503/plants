# plants
Program to create visualizations of plants and other fractals in Python using l-systems

## Explenation
For now it's only a simple program with some operations and a simple parser for the turtle in python.
I'm looking into how to make it compatible with some sort of programming language or JSON/toml like config file.
My preference now is for creating a simple programming language for defining rewriting rules, and constants like
the angle or the axiom.

## Progress
I need to do 2 big things;
- [ ] Add parametric grammars, this is somewhat difficult but leads to beatiful pay offs
- [ ] 3D support, for stuff like trees in 3D space
What I need to add for creating a programing language for defining the rules;
- [ ] Defining the grammar of the language
- [ ] A lexer for lexing the input of the file
- [ ] A parser for parsing the tokenized output of the lexer
- [ ] An evaluator to evaluate the parsed content.
- [ ] Map the output of the evaluator to the rewriting system of the l-system

## Dependencies
- Python3.x
- Tkinter

## Running the script
For now it's easy to run this script. The following steps are what you need to follow.
### Clone the repo
Clone deze repo in de top directory van XAMPP dat is htdocs
```bash
$ git clone https://github.com/Thom2503/plants.git
```
### Run the script
Go to the cloned folder.
```bash
$ cd plants
```
Run the `rec.py` script:
```bash
$ python3 rec.py
```

## Editing the rules for creating figures
This is the process to alter the rules for the visualization of the figure.
There are different global variables that you can edit, except for `OPS`. These are `RULES`, `ITERATIONS`, `ANGLE`.
Changing `ITERATIONS` will tell how many times the rewriting is done.
Changing `ANGLE` changes the degrees at which the turtle turns.
`RULES` is where the rules are made;
```python
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
    '+': '+',
    '-': '-',
    '[': '[',
    ']': ']',
```
These rules with the starting input being `X` will output a fractal tree if you call `moveTurtle(createString("X", ITERATIONS))`.

## Resources
Below are some resources that I used while making this.
- [The Algorithmic Beauty of Plants](http://www.algorithmicbotany.org/papers/abop/abop.pdf)
- [L-system](https://en.wikipedia.org/wiki/L-system)
