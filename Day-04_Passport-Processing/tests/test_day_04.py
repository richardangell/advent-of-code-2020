import puzzle_1
import puzzle_2

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize(
        "row,expected", [(0, True), (1, False), (2, True), (3, False)]
    )
    def test_passport_valid(self, input_1, row, expected):
        """Test passport_valid gives correct output."""

        assert puzzle_1.passport_valid(input_1[row]) == expected

    def test_count_valid_passports(self, input_1):
        """Test count_valid_passports gives correct output."""

        assert puzzle_1.count_valid_passports(input_1) == 2


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize("file,expected", [("input_2", 0), ("input_3", 4)])
    def test_count_valid_passports(self, load_input, file, expected):
        """Test count_valid_passports gives correct output."""

        assert puzzle_2.count_valid_passports(load_input(file)) == expected
