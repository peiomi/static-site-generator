# run test script with ./test.sh
import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url_provided(self):
        node = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node.url, "https://boot.dev")

    def test_textnode_to_htmlnode(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_textype_LINK_to_html(self):
        node = TextNode("i am a link", TextType.LINK, "https://boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "i am a link")
        self.assertEqual(html_node.props, { "href": "https://boot.dev" })

    def test_texttype_IMAGE_to_html(self):
        node = TextNode("this is an image", TextType.IMAGE, "public/image.img")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src": "public/image.img", "alt": "this is an image" })

    def test_texttype_CODE_to_html(self):
        node = TextNode("this is a code block", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "this is a code block")

    def test_texttype_BOLD_to_html(self):
        node = TextNode("i am bold", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "i am bold")

    def test_texttype_ITALIC_to_html(self):
        node = TextNode("i am italian", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "i am italian")


if __name__ == "__main__":
    unittest.main()