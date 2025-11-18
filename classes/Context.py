from typing import Dict, LiteralString, List, Tuple
from classes.Static import Static


class Context(Static):
    @staticmethod
    def apply_context(
        input_string: str,
        rules: Dict[Tuple[str], str],
        ignore_symbols: List[str]
    ) -> LiteralString:
        """
        Apply context-sensitive production rules to an L-system string.

        :param input_string: The string to transform.
        :param rules: A dictionary of rules in the form {(left_context, symbol, right_context): replacement}.
        :param ignore_symbols: A set of symbols to ignore during context matching.
        :return: The transformed string.
        """
        output = []
        n = len(input_string)

        for i in range(n):
            symbol = input_string[i]

            # Skip ignored symbols
            if symbol in ignore_symbols:
                output.append(symbol)
                continue

            # Determine the effective left and right context, skipping ignored symbols
            left_context = None
            for j in range(i - 1, -1, -1):
                if input_string[j] not in ignore_symbols:
                    left_context = input_string[j]
                    break

            right_context = None
            for j in range(i + 1, n):
                if input_string[j] not in ignore_symbols:
                    right_context = input_string[j]
                    break

            # Check if a rule exists for this context
            matched_rule = False
            for (left, center, right), replacement in rules.items():
                if (left == left_context or left is None) and \
                   (center == symbol) and \
                   (right == right_context or right is None):
                    output.append(replacement)
                    matched_rule = True
                    break

            # If no rule matched, apply the identity transformation
            if not matched_rule:
                output.append(symbol)

        return ''.join(output)
