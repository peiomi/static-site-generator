import unittest
from node_util import NodeUtil
from textnode import TextNode, TextType

util = NodeUtil()

class TestNodeUtil(unittest.TestCase):
    def test_split_text_node(self):
        node = TextNode("This is text with a `code block`", TextType.PLAIN)
        new_nodes = util.split_nodes_delimiter(old_nodes=[node], delimiter="`", text_type=TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_wrong_delimiter(self):
        node = TextNode("This is text with **bold text**", TextType.PLAIN)

        with self.assertRaises(Exception) as context:
            util.split_nodes_delimiter(old_nodes=[node], delimiter="`", text_type=TextType.BOLD)

        self.assertEqual(str(context.exception), "wrong delimiter used")

    def test_no_closing_delimiter(self):
        node = TextNode("This is text with __italic text", TextType.PLAIN)

        with self.assertRaises(Exception) as context:
            util.split_nodes_delimiter(old_nodes=[node], delimiter="__", text_type=TextType.ITALIC)

        self.assertEqual(str(context.exception), "no closing delimiter, invalid Markdown")

    def test_bold_text(self):
        node = TextNode("This is text with **bold text**", TextType.PLAIN)
        new_nodes = util.split_nodes_delimiter(old_nodes=[node], delimiter="**", text_type=TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "bold text")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_italic_text(self):
        node = TextNode("This is text with __italic text__", TextType.PLAIN)
        new_nodes = util.split_nodes_delimiter(old_nodes=[node], delimiter="__", text_type=TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "italic text")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_no_delimiter_in_text(self):
        node = TextNode("Just some text no delili", TextType.PLAIN)
        new_nodes = util.split_nodes_delimiter(old_nodes=[node], delimiter="__", text_type=TextType.ITALIC)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Just some text no delili")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)

    def test_multi_nodes_and_types(self):
        node1 = TextNode("This is text with a `code block` and more text", TextType.PLAIN)
        node2 = TextNode("This is text with a `code block` and **bold text**", TextType.PLAIN)
        new_nodes = util.split_nodes_delimiter(old_nodes=[node1, node2], delimiter="`", text_type=TextType.CODE)
        self.assertEqual(len(new_nodes), 6)
        new_nodes = util.split_nodes_delimiter(old_nodes=new_nodes, delimiter="**", text_type=TextType.BOLD)
        self.assertEqual(len(new_nodes), 8)



if __name__ == "__main__":
    unittest.main()