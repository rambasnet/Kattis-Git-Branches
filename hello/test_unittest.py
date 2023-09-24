"""Test module for hello.py.
"""

import unittest
from hello import answer


class TestHello(unittest.TestCase):
    """Test class for hello.py."""

    def test_answer(self) -> None:
        """Test answer() function."""
        self.assertEqual(answer(), "Hello World!")
