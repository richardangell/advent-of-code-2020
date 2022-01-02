import puzzle_1
import puzzle_2


class TestPuzzle1:
    """Tests for puzzle 1."""

    def test_sum_yes_counts(self, input_1):
        """Test that the sum of all questions answered yes to is correct."""

        assert puzzle_1.sum_yes_counts(input_1) == 11


class TestPuzzle2:
    """Tests for puzzle 2."""

    def test_sum_questions_answered_by_all(self, input_1):
        """Test sum_questions_answered_by_all gives the correct output."""

        assert puzzle_2.sum_questions_answered_by_all(input_1) == 6
