from collections import Counter
import puzzle_1


def count_questions_answered_by_all(group_answers: list[str]) -> int:
    """Count the number of questions for which everyone in the group answered yes."""

    group_size = len(group_answers)

    yes_counts: Counter = Counter()

    for individual_answers in group_answers:

        for answer in individual_answers:

            yes_counts[answer] += 1

    questions_answered_by_all = 0

    for _, count in yes_counts.items():

        if count == group_size:

            questions_answered_by_all += 1

    return questions_answered_by_all


def sum_questions_answered_by_all(input: list[list[str]]) -> int:
    """Sum the total number of questions answered yes by all members of a group,
    across all groups.
    """

    yes_counts = [count_questions_answered_by_all(row) for row in input]

    return sum(yes_counts)


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = sum_questions_answered_by_all(input)

    print(result)
