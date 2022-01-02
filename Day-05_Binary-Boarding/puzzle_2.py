import puzzle_1


def find_seat_id(input: list[str]):
    """Find the seat id that is missing from the list but the previous and next seat ids are present."""

    seat_ids = [puzzle_1.calculate_seat_id(boarding_pass) for boarding_pass in input]

    seat_ids = sorted(seat_ids)

    for seat_index in range(1, len(seat_ids) - 1):

        prev_seat_in_ids = seat_ids[seat_index - 1] == seat_ids[seat_index] - 1
        next_seat_in_ids = seat_ids[seat_index + 1] == seat_ids[seat_index] + 1

        if not (prev_seat_in_ids and next_seat_in_ids):

            return seat_ids[seat_index] + 1


if __name__ == "__main__":

    input = puzzle_1.load_input("input_1.txt")

    result = find_seat_id(input)

    print(result)
