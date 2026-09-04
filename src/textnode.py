from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "**text**"
    ITALIC = "__text__"
    CODE_BLOCK = "`text`"
    LINK = "[text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.value == other.value
        return NotImplemented

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"