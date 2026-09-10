import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello Floating Rock!")
        self.assertEqual(node.to_html(), "<p>Hello Floating Rock!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "click", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href='https://www.google.com'>click</a>")

    def test_value_missing(self):
        with self.assertRaises(TypeError):
            LeafNode("div")

        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
    
