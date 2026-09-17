from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    PLAIN = "text"
    BOLD = "**text**"
    ITALIC = "__text__"
    CODE = "`text`"
    LINK = "[text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text == other.text and self.text_type == other.text_type and self.url == other.url
        return NotImplemented

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.name}, {self.url})"


    def text_node_to_html_node(self):
        if not isinstance(self.text_type, TextType):
            raise ValueError("text_type must be a TextType enum")

        if self.text_type == TextType.PLAIN:
            return LeafNode(tag=None, value=self.text)

        elif self.text_type == TextType.BOLD:
            return LeafNode(tag="b", value=self.text)

        elif self.text_type == TextType.ITALIC:
            return LeafNode(tag="i", value=self.text)

        elif self.text_type == TextType.CODE:
            return LeafNode(tag="code", value=self.text)

        elif self.text_type == TextType.LINK:
            props = { "href": self.url }
            return LeafNode(tag="a", value=self.text, props=props)

        elif self.text_type == TextType.IMAGE:
            props = { "src": self.url, "alt": self.text }
            return LeafNode(tag="img", value="", props=props)