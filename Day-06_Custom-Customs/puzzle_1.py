from collections import Counter
import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[list[str]]:
    """Load the input file and return a list of lists of the answers to
    customs questions.
    """

    input = helpers.load_input(file, remove_lines_breaks=True)

    input_grouped = []

    group: list[str] = []

    for row in input:

        if row == "":

            input_grouped.append(group)

            group = []

        else:

            group.append(row)

    input_grouped.append(group)

    return input_grouped


def count_yes_questions(group_answers: list[str]) -> int:
    """Count the number of unique questions that are answered yes to across
    all people in a group.
    """

    yes_counts: Counter = Counter()

    for individual_answers in group_answers:

        for answer in individual_answers:

            yes_counts[answer] += 1

    return len(yes_counts.keys())


def sum_yes_counts(input: list[list[str]]) -> int:
    """Sum the total number of questions answered yes to across all groups."""

    yes_counts = [count_yes_questions(row) for row in input]

    return sum(yes_counts)


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = sum_yes_counts(input)

    print(result)
