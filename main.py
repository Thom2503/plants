from argparse import ArgumentParser, Namespace
from classes.DOL import DOL


def main() -> None:
    description: str = "Make plants from the command line using a turtle"
    parser: ArgumentParser = ArgumentParser(description=description)
    parser.add_argument("--config", help="Path to TOML configuration")
    args: Namespace = parser.parse_args()

    dol: DOL = DOL(args.config)
    dol.moveTurtle()


if __name__ == "__main__":
    main()
