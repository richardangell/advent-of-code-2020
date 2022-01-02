import puzzle_1

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "file,expected",
        [("input_1", (70, 7)), ("input_2", (14, 7)), ("input_3", (102, 4))],
    )
    def test_determine_seat_position(self, load_input, file, expected):
        """Test seat positions are calculated correctly."""

        input = load_input(file)

        assert puzzle_1.determine_seat_position(input[0]) == expected

    @pytest.mark.parametrize(
        "file,expected", [("input_1", 567), ("input_2", 119), ("input_3", 820)]
    )
    def test_calculate_seat_id(self, load_input, file, expected):
        """Test seat id calculated correctly."""

        input = load_input(file)

        assert puzzle_1.calculate_seat_id(input[0]) == expected
