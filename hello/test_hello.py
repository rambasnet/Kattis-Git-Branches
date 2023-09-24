"""Test module for hello.py 
"""

# import unittest
from hello import answer


def test_answer() -> None:
    """Test answer() function."""
    assert answer() == "Hello World!"
