import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_return_str(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        return_value = node.props_to_html()
        self.assertIsInstance(return_value, str)

    def test_props_return_empty_str(self):
        node = HTMLNode()
        return_value = node.props_to_html()
        self.assertEqual(return_value, "")


if __name__ == "__main__":
    unittest.main()