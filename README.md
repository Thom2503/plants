# plants
Program to create visualizations of plants and other fractals in Python using l-systems

## Explenation
For now it's only a simple program with some operations and a simple parser for the turtle in python.
I'm looking into how to make it compatible with some sort of programming language or JSON/toml like config file.

## Progress
I need to do 2 big things;
- [x] Stochastic grammars
- [ ] Add context sensitve grammars.
- [ ] Add parametric grammars, this is somewhat difficult but leads to beatiful pay offs
- [ ] 3D support, for stuff like trees in 3D space

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
Run the `main.py` script:
```bash
$ python3 main.py --config /configs/islangs.toml
```

## Editing the rules for creating figures
There are configs in /configs that have the configurations with the rules, axiom, iterations etc.
Look at the files and you can edit them however you want.

## Resources
Below are some resources that I used while making this.
- [The Algorithmic Beauty of Plants](http://www.algorithmicbotany.org/papers/abop/abop.pdf)
- [L-system](https://en.wikipedia.org/wiki/L-system)
