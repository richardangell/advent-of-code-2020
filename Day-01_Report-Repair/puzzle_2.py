import math

import puzzle_1


def find_elements_that_sum_to_value(
    input: list[int], target_value: int
) -> tuple[int, int]:
    """Find elements of the input that sum to a particular target_value."""

    for value in input:

        remainder = target_value - value

        if remainder in input:

            return value, remainder

    raise ValueError(f"unable to find 2 eleemnts that sum to {target_value}")


def find_elements_that_sum_to_2020(input: list[int]) -> tuple[int, int, int]:
    """Find elements of the input that sum to 2020."""

    for value in input:

        remainder = 2020 - value

        values_that_sum_to_remainder = find_elements_that_sum_to_value(input, remainder)

        if values_that_sum_to_remainder is not None:

            return (
                value,
                values_that_sum_to_remainder[0],
                values_that_sum_to_remainder[1],
            )

    raise ValueError("unable to find 3 elements that sum to 2020")


def multiply_elements_that_sum_to_2020(input: list[int]) -> int:
    """Find the product of elements that sum to 2020 in the input."""

    values = find_elements_that_sum_to_2020(input)

    return math.prod(values)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = multiply_elements_that_sum_to_2020(input)

    print(result)
