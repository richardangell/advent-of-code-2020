import puzzle_1
import puzzle_2

import pytest


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_count_trees_encountered(self, input_1):
        """Test count_trees_encountered outputs the correct result."""

        assert puzzle_1.count_trees_encountered(input_1, 3, 1) == 7


class TestPuzzle2:
    """Tests for puzzle 2."""

    @pytest.mark.parametrize(
        "x_step,y_step,expected",
        [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)],
    )
    def test_count_trees_encountered(self, input_1, x_step, y_step, expected):
        """Test count_trees_encountered outputs the correct result."""

        assert puzzle_1.count_trees_encountered(input_1, x_step, y_step) == expected

    def test_find_product_of_trees_encountered(self, input_1):
        """Test find_product_of_trees_encountered gives the correct output."""

        routes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

        assert puzzle_2.find_product_of_trees_encountered(input_1, routes) == 336
