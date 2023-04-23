from src.pre_built.counter import count_ocurrences
import pytest
from unittest.mock import mock_open, patch


@pytest.fixture
def read_file():
    return """
    python,
    python,
    Python,
    python,
    python,
    """


def test_counter(read_file):
    with patch("builtins.open", mock_open(read_data=read_file)):
        assert count_ocurrences("xxx", "python") == 5
