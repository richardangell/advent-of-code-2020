import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load the input file."""

    return helpers.load_input(file, remove_lines_breaks=True)


def count_trees_encountered(input: list[str], x_step: int, y_step: int) -> int:
    """Count the number of trees that would be encountered by taking the
    path (right 3, down 1) down the slope from [0,0] start position.
    """

    tree_count = 0

    x = 0
    y = 0

    n_steps = (len(input) - 1) / y_step

    for _ in range(int(n_steps)):

        x += x_step
        y += y_step

        x = x % len(input[0])

        if input[y][x] == "#":

            tree_count += 1

    return tree_count


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_trees_encountered(input, 3, 1)

    print(result)
