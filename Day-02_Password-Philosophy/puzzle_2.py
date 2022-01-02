import puzzle_1


def check_password_valid(pass_and_rules: puzzle_1.input_line_dict) -> bool:
    """Check if exactly one of the required positions in the input is the
    correct character.
    """

    position_1 = (
        pass_and_rules["input"][pass_and_rules["min"] - 1] == pass_and_rules["letter"]
    )
    position_2 = (
        pass_and_rules["input"][pass_and_rules["max"] - 1] == pass_and_rules["letter"]
    )

    return position_1 != position_2


def count_valid_passwords(input: list[puzzle_1.input_line_dict]) -> int:
    """Count the number of valid passwords in the input."""

    count = 0

    for pass_and_rule in input:

        if check_password_valid(pass_and_rule):

            count += 1

    return count


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = count_valid_passwords(input)

    print(result)
