import sys

sys.path.append("..")
import helpers  # noqa


def load_input(file: str) -> list[str]:
    """Load the input file."""

    input_processed = []

    input = helpers.load_input(file, remove_lines_breaks=True)

    lines_appended = ""

    for line in input:

        if line == "":

            input_processed.append(lines_appended)

            lines_appended = ""

        else:

            lines_appended += " " + line

    input_processed.append(lines_appended)

    return input_processed


def count_valid_passports(
    input: list[str],
    required_fields: tuple[str, str, str, str, str, str, str] = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ),
) -> int:
    """Count the number of passports that contain the required fields and are
    therefore valid.
    """

    passports_checked = [
        passport_valid(passport, required_fields) for passport in input
    ]

    return sum(passports_checked)


def passport_valid(
    passport: str,
    required_fields: tuple[str, str, str, str, str, str, str] = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ),
) -> bool:
    """Check is a passport is valid, by having all required fields in it."""

    fields_in_passport = [field in passport for field in required_fields]

    return all(fields_in_passport)


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_valid_passports(input)

    print(result)
