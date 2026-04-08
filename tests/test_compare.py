import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from compare import find_common_lines, find_diff_lines

@pytest.fixture
def sample_data():
    return {"a", "b", "c"}, {"b", "c", "d"}

@pytest.mark.parametrize(
    "lines1, lines2, expected",
    [
        ({"a", "b"}, {"b", "c"}, {"b"}),
        ({"x"}, {"y"}, set()),
    ]
)
def test_common(lines1, lines2, expected):
    assert find_common_lines(lines1, lines2) == expected