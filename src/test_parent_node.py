import unittest
from parent_node import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_grandchildren(self):
        grandchild_node = LeafNode("a", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><a>grandchild</a></span></div>")

    def test_to_html_children_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        child_node = LeafNode("span", "child", props=props)
        parent_node = ParentNode("div", [child_node], props=props)
        self.assertEqual(parent_node.to_html(), "<div href='https://www.google.com' target='_blank'><span href='https://www.google.com' target='_blank'>child</span></div>")

    def test_missing_tags(self):
        with self.assertRaises(TypeError):
            ParentNode([LeafNode("div", "child")])

        parent_node = ParentNode(None, [LeafNode("div", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_missing_children(self):
        with self.assertRaises(TypeError):
            ParentNode("div")

        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_multiple_children_props(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        parent_node = ParentNode("div", children=children, props=props)
        self.assertEqual(parent_node.to_html(), "<div href='https://www.google.com' target='_blank'><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>")

    def test_empty_children(self):
        parent = ParentNode("div", [])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_deep_nesting(self):
        greatgrandchild = LeafNode("a", "text")
        grandchild = ParentNode("span", [greatgrandchild])
        child = ParentNode("p", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(parent.to_html(), "<div><p><span><a>text</a></span></p></div>")

    def test_plain_text_child(self):
        child = LeafNode(None, "hello flying rock")
        parent = ParentNode("div", [child])

        self.assertEqual(parent.to_html(), "<div>hello flying rock</div>")


if __name__ == "__main__":
    unittest.main()
    