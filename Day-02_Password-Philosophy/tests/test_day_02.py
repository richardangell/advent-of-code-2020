import puzzle_1
import puzzle_2

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    @pytest.mark.parametrize("row,expected", [(0, True), (1, False), (2, True)])
    def test_check_password_valid(self, input_1, row, expected):
        """Test check_password_valid returns correct result."""

        assert puzzle_1.check_password_valid(input_1[row]) == expected

    def test_count_valid_passwords(self, input_1):
        """Test count_valid_passwords returns the correct output."""

        assert puzzle_1.count_valid_passwords(input_1) == 2


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize("row,expected", [(0, True), (1, False), (2, False)])
    def test_check_password_valid(self, input_1, row, expected):
        """Test check_password_valid returns correct result."""

        assert puzzle_2.check_password_valid(input_1[row]) == expected

    def test_count_valid_passwords(self, input_1):
        """Test count_valid_passwords returns the correct output."""

        assert puzzle_2.count_valid_passwords(input_1) == 1
