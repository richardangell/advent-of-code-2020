from marshmallow import Schema, fields, validate, validates, ValidationError

import puzzle_1


def load_input(file: str) -> list[dict]:
    """Load the input file and parse each row into a dict."""

    input = puzzle_1.load_input(file)

    input_dict = [convert_to_dict(row) for row in input]

    return input_dict


def convert_to_dict(passport: str) -> dict:
    """Convert a single passport row from the input into a dict."""

    passport_dict = {}

    passport_split = passport[1:].split(" ")

    for field in passport_split:

        field_value = field.split(":")

        passport_dict[field_value[0]] = field_value[1]

    return passport_dict


def count_valid_passports(input: list[dict]) -> int:
    """Count the number of passports that contain the required fields and are
    therefore valid.
    """

    passports_checked = [passport_valid(passport) for passport in input]

    return sum(passports_checked)


def passport_valid(passport: dict) -> bool:
    """Check is a passport is valid by checking specific rules for each field."""

    check_valid = PassportSchema().validate(passport)

    return check_valid == {}


class PassportSchema(Schema):
    byr = fields.Int(required=True, validate=validate.Range(min=1920, max=2002))
    iyr = fields.Int(required=True, validate=validate.Range(min=2010, max=2020))
    eyr = fields.Int(required=True, validate=validate.Range(min=2020, max=2030))
    hgt = fields.Str(required=True)
    hcl = fields.Str(required=True, validate=validate.Regexp(regex=r"^\#[a-f0-9]{6}$"))
    ecl = fields.Str(
        required=True,
        validate=validate.OneOf(
            choices=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ),
    )
    pid = fields.Str(required=True, validate=validate.Regexp(regex=r"^[0-9]{9}$"))
    cid = fields.Str(require=False)

    @validates("hgt")
    def validate_hgt(self, value):

        units = value[-2:]
        number = value[:-2]

        if units not in ["cm", "in"]:
            raise ValidationError("units not in cm or in.")

        try:
            number_int = int(number)
        except Exception:
            raise ValidationError("number to convert hgt value to int.")

        if units == "cm":

            if not (number_int >= 150 and number_int <= 193):
                raise ValidationError("hgt not in range [150, 193].")

        else:

            if not (number_int >= 59 and number_int <= 76):
                raise ValidationError("hgt not in range [150, 193].")


if __name__ == "__main__":

    input = load_input("input_1.txt")

    result = count_valid_passports(input)

    print(result)
