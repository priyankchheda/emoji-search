""" test for sorting algorithms """
import pytest

from bubble import bubble
from utils import SortingException
from dataset import VALID_USECASE, INVALID_USECASE


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
