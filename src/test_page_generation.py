import unittest
from generate_page import extract_title

class TestPageGeneration(unittest.TestCase):
    def test_single_h1(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_h1_with_extra_whitespace(self):
        markdown = "#   Hello   "
        self.assertEqual(extract_title(markdown), "Hello")

    def test_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("Hello")

if __name__ == "__main__":
    unittest.main()