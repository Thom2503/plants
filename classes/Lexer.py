import re

TOKENS = (
    'DIGIT', 'SYMBOL', 'EQ',  'LT',    'GT',   'LTE',
    'GTE',   'NEQ',    'VAR', 'VALUE', 'RULE', 'PARAM_RULE', 'KEYWORD'
)


class Lexer:
    input: str
    tokens: list[tuple[str, str]] = []

    def __init__(self, input: str) -> None:
        self.input = input.lstrip()

    def Lex(self) -> list[tuple[str, str]]:
        current_line: int = 0
        for line in self.input.split("\n"):
            current_line += 1
            print(line)
        return self.tokens

    def isKeyword(self, line):
        pass

    def isDigit(self, line):
        pass

    def isSymbol(self, line):
        pass

    def isComparison(self, line):
        pass

    def isVariable(self, line):
        pass

    def isValue(self, line):
        pass

    def isRule(self, line):
        pass

    def isParamRule(self, line):
        pass
