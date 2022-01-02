import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load the input file."""

    return helpers.load_input(file, remove_lines_breaks=True)


def determine_seat_position(boarding_pass: str) -> tuple[int, int]:
    """Calculate seat row and column from the boarding pass."""

    seat_row = find_seat_position(boarding_pass[:7], "F", "B") - 1

    seat_column = find_seat_position(boarding_pass[7:], "L", "R") - 1

    return seat_row, seat_column


def find_seat_position(code: str, lower_char: str, upper_char: str) -> int:
    """Find seat position as integer between 1 and 2 ^ (no. instructions)."""

    start = 1
    end = 2 ** len(code)

    for char_index in range(len(code)):

        start, end = narrow_seat_position(
            code[char_index], lower_char, upper_char, start, end
        )

    if not start == end:

        raise ValueError(f"unique seat position not found - {start} to {end}")

    return start


def narrow_seat_position(
    char: str, lower_char: str, upper_char: str, lower_limit: int, upper_limit: int
) -> tuple[int, int]:
    """Half the range of the seat position ([lower_limit, upper_limit]) given the value of char."""

    half_range = (upper_limit - lower_limit + 1) / 2

    if char == lower_char:

        return lower_limit, int(upper_limit - half_range)

    elif char == upper_char:

        return int(lower_limit + half_range), upper_limit

    else:

        raise ValueError(
            f"unexpected char ({char}) with lower_char ({lower_char}) and upper_char ({upper_char})"
        )


def calculate_seat_id(boarding_pass: str) -> int:
    """Calculate seat id from boarding pass."""

    row, column = determine_seat_position(boarding_pass)

    return (row * 8) + column


def find_max_set_id(input: list[str]) -> int:
    """Find the maximum seat id in the input file."""

    seat_ids = [calculate_seat_id(boarding_pass) for boarding_pass in input]

    return max(seat_ids)


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = find_max_set_id(input)

    print(result)
