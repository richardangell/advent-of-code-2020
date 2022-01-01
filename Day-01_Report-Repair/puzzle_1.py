import math
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[int]:
    """Load the input file."""

    return helpers.load_input_int(file, remove_lines_breaks=True)


def find_elements_that_sum_to_2020(input: list[int]) -> tuple[int, int]:
    """Find elements of the input that sum to 2020."""

    for value in input:

        remainder = 2020 - value

        if remainder in input:

            return value, remainder

    raise ValueError("unable to find 2 elements that sum to 2020")


def multiply_elements_that_sum_to_2020(input: list[int]) -> int:
    """Find the product of elements that sum to 2020 in the input."""

    values = find_elements_that_sum_to_2020(input)

    return math.prod(values)


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = multiply_elements_that_sum_to_2020(input)

    print(result)
