import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_find_elements_that_sum_to_2020(self, input_1):
        """Test find_elements_that_sum_to_2020 output is correct."""

        assert puzzle_1.find_elements_that_sum_to_2020(input_1) == (1721, 299)

    def test_multiply_elements_that_sum_to_2020(self, input_1):
        """Test multiply_elements_that_sum_to_2020 output is correct."""

        assert puzzle_1.multiply_elements_that_sum_to_2020(input_1) == 514579


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_find_elements_that_sum_to_2020(self, input_1):
        """Test find_elements_that_sum_to_2020 output is correct."""

        assert puzzle_2.find_elements_that_sum_to_2020(input_1) == (979, 366, 675)

    def test_multiply_elements_that_sum_to_2020(self, input_1):
        """Test multiply_elements_that_sum_to_2020 output is correct."""

        assert puzzle_2.multiply_elements_that_sum_to_2020(input_1) == 241861950
