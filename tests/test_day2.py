import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import pytest
from Day2.day2 import valid_row, updated_valid_row, part_a, part_b

sample_rows = [
    [1, 2, 3],      # valid increasing
    [5, 3, 1],      # valid decreasing
    [1, 5, 2],      # becomes valid after removing one element
    [1, 5, 1],      # cannot be made valid
]


def test_valid_row():
    assert valid_row([1, 2, 3])
    assert valid_row([5, 3, 1])
    assert not valid_row([1, 5, 2])
    assert not valid_row([1, 5, 1])


def test_updated_valid_row():
    # Already valid rows remain valid
    assert updated_valid_row([1, 2, 3])
    # Removal of one element can make the row valid
    assert updated_valid_row([1, 5, 2])
    # This row cannot be made valid even after removing one element
    assert not updated_valid_row([1, 5, 1])


def test_part_a():
    assert part_a(sample_rows) == 2


def test_part_b(capsys):
    result = part_b(sample_rows)
    captured = capsys.readouterr()
    assert captured.out.strip() == "True"
    assert result == 3
