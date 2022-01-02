from collections import Counter
from typing import TypedDict
import sys

sys.path.append("..")
import helpers  # noqa


class input_line_dict(TypedDict):
    input: str
    letter: str
    min: int
    max: int


def load_input(file: str) -> list[input_line_dict]:
    """Load the input file."""

    lines = helpers.load_input(file, remove_lines_breaks=True)

    return [split_input_line(line) for line in lines]


def split_input_line(line: str) -> input_line_dict:
    """Split one line of the input into a dict with min, max, letter
    and input keys.
    """

    line_split = line.split(": ")

    constraint_split = line_split[0].split(" ")

    min_max = constraint_split[0].split("-")

    required_min = int(min_max[0])
    required_max = int(min_max[1])

    dict_line: input_line_dict = {
        "input": line_split[1],
        "letter": constraint_split[1],
        "min": required_min,
        "max": required_max,
    }

    return dict_line


def check_password_valid(pass_and_rules: input_line_dict) -> bool:
    """Check if a password has the required minimum and no more than
    the maximum of a given letter.
    """

    letters_counter: Counter = Counter()

    for letter in pass_and_rules["input"]:

        letters_counter[letter] += 1

    above_min = letters_counter[pass_and_rules["letter"]] >= pass_and_rules["min"]
    less_than_max = letters_counter[pass_and_rules["letter"]] <= pass_and_rules["max"]

    return above_min & less_than_max


def count_valid_passwords(input: list[input_line_dict]) -> int:
    """Count the number of valid passwords in the input."""

    count = 0

    for pass_and_rule in input:

        if check_password_valid(pass_and_rule):

            count += 1

    return count


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_valid_passwords(input)

    print(result)
