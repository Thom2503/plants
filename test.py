from typing import LiteralString


def apply_context_sensitive_lsystem(
    input_string,
    rules,
    ignore_symbols
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


# Example usage
if __name__ == "__main__":
    # Define context-sensitive L-system rules
    production_rules = {
        ('0', '0', '0'): '0',  # 0<0>0 → 0
        ('0', '0', '1'): '1[+F1F1]',  # 0 < 0 > 1 → 1[+F1F1]
        ('0', '1', '0'): '1',  # 0<1>0 → 1
        ('0', '1', '1'): '1',  # 0<1>1 → 1
        ('1', '0', '0'): '0',  # 1<0>0 → 0
        ('1', '0', '1'): '1F1',  # 1 < 0 > 1 → 1F1
        ('1', '1', '0'): '0',  # 1<1>0 → 0
        ('1', '1', '1'): '0',  # 1<1>1 → 0
        ('*', '+', '*'): '-',  # *<+>* → -
        ('*', '-', '*'): '+',  # *<->* → +
    }

    # Ignored symbols
    ignored = {'+', '-', 'F'}

    # Initial string
    input_str = "F1F1F1"

    # Number of iterations
    iterations = 30

    # Apply the rules iteratively
    current_string = input_str
    for _ in range(iterations):
        current_string = apply_context_sensitive_lsystem(current_string, production_rules, ignored)

    print("Final String:", current_string)
