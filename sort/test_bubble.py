""" test for sorting algorithms """
import pytest

from bubble import bubble, SortingException

VALID_USECASE = [
    ([], []),
    ([1], [1]),
    ([-1], [-1]),
    ([-2, 1], [-2, 1]),
    ([100, -100, -1110], [-1110, -100, 100]),
    ([5, 3, 2, 4, 1], [1, 2, 3, 4, 5]),
    ([1234, 4567, 567456, 3215, 54745, 1357357],
     [1234, 3215, 4567, 54745, 567456, 1357357]),
    ([1.2, 1.3, 1.1, 1.0, 0.9], [0.9, 1.0, 1.1, 1.2, 1.3]),
    (["test", "test2", "test1", "a22"], ["a22", "test", "test1", "test2"])
]

INVALID_USECASE = [
    ([1, 2, 3, "test", 4], "mixed type present in list"),
    (["test1", "test", 4], "mixed type present in list"),
    (["test", 4], "mixed type present in list"),
]


class TestBubbleSort:
    """ Bubble sort test cases"""
    @pytest.mark.parametrize("test_input, output", VALID_USECASE)
    def test_bubble_sort(self, test_input, output):
        """ test for valid inputs """
        bubble(test_input)
        assert test_input == output

    @pytest.mark.parametrize("test_input, output", INVALID_USECASE)
    def test_bubble_sort_invalid_input(self, test_input, output):
        """ test for invalid inputs """
        with pytest.raises(SortingException) as excinfo:
            bubble(test_input)
        assert str(excinfo.value) == output
