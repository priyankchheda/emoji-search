""" Tests for sorting algorithms
"""

import pytest

from py3algorithm.sort import bubble, selection, insertion, shell


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
    ([1.2, -1.3, 1.1, -1.0, 0.9], [-1.3, -1.0, 0.9, 1.1, 1.2]),
    (["test", "test2", "test1", "a22"], ["a22", "test", "test1", "test2"])
]


@pytest.mark.parametrize("test_input, output", VALID_USECASE)
def test_bubble_sort(test_input, output):
    """ test for valid inputs """
    bubble(test_input)
    assert test_input == output


@pytest.mark.parametrize("test_input, output", VALID_USECASE)
def test_selection_sort(test_input, output):
    """ test for valid inputs """
    selection(test_input)
    assert test_input == output


@pytest.mark.parametrize("test_input, output", VALID_USECASE)
def test_insertion_sort(test_input, output):
    """ test for valid inputs """
    insertion(test_input)
    assert test_input == output


@pytest.mark.parametrize("test_input, output", VALID_USECASE)
def test_shell_sort(test_input, output):
    """ test for valid inputs """
    shell(test_input)
    assert test_input == output
