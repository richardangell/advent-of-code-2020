import math
import puzzle_1


def find_product_of_trees_encountered(input: list[str], routes: list[list[int]]) -> int:
    """Find the product of trees encountered in each of the routes provided."""

    trees = [
        puzzle_1.count_trees_encountered(input, route[0], route[1]) for route in routes
    ]

    return math.prod(trees)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    result = find_product_of_trees_encountered(input, routes)

    print(result)
