from enum import Enum
from htmlnode import HTMLNode
from parent_node import ParentNode
from node_util import NodeUtil
from textnode import TextNode, TextType

util = NodeUtil()

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UO_LIST = "unordered_list"
    O_LIST = "ordered_list"

class BlockUtil():
    def markdown_to_blocks(self, markdown):
        blocks = markdown.split("\n\n")
        return [block.strip() for block in blocks if block.strip()]


    def block_to_block_type(self, block):
        lines = block.split("\n")
        
        if block.startswith("```\n") and block.endswith("```"):
            return BlockType.CODE

        if (
            block.startswith("# ")
            or block.startswith("## ")
            or block.startswith("### ")
            or block.startswith("#### ")
            or block.startswith("##### ")
            or block.startswith("###### ")
        ):
            return BlockType.HEADING

        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE

        if all(line.startswith("- ") for line in lines):
            return BlockType.UO_LIST

        is_ordered = True
        for i, line in enumerate(lines):
            if not line.startswith(f"{i + 1}. "):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.O_LIST
        
        return BlockType.PARAGRAPH

    def markdown_to_html_node(self, markdown):
        blocks = self.markdown_to_blocks(markdown)
        children = []
        for block in blocks:
            html_node = self.block_to_html_node(block)
            children.append(html_node)
        return ParentNode("div", children, None)

    def block_to_html_node(self, block):
        block_type = self.block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            return self.paragraph_to_html_node(block)
        if block_type == BlockType.HEADING:
            return self.heading_to_html_node(block)
        if block_type == BlockType.CODE:
            return self.code_to_html_node(block)
        if block_type == BlockType.O_LIST:
            return self.olist_to_html_node(block)
        if block_type == BlockType.UO_LIST:
            return self.uo_list_to_html_node(block)
        if block_type == BlockType.QUOTE:
            return self.quote_to_html_node(block)
        raise ValueError("invalid block type")

    def text_to_children(self, text):
        text_nodes = util.text_to_textnodes(text)
        children = []
        for text_node in text_nodes:
            html_node = text_node.text_node_to_html_node()
            children.append(html_node)
        return children

    def paragraph_to_html_node(self, block):
        lines = block.split("\n")
        paragraph = " ".join(lines)
        children = self.text_to_children(paragraph)
        return ParentNode("p", children)

    def heading_to_html_node(self, block):
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break

        if level + 1 >= len(block):
            raise ValueError(f"invalid heading level: {level}")
        text = block[level + 1 :]
        children = self.text_to_children(text)
        return ParentNode(f"h{level}", children)

    def code_to_html_node(self, block):
        if not block.startswith("```") or not block.endswith("```"):
            raise ValueError("invalid code block")
        text = block[4:-3]
        raw_text_node = TextNode(text, TextType.PLAIN)
        child = raw_text_node.text_node_to_html_node()
        code = ParentNode("code", [child])
        return ParentNode("pre", [code])

    def olist_to_html_node(self, block):
        items = block.split("\n")
        html_items = []
        for item in items:
            parts = item.split(". ", 1)
            text = parts[1]
            children = self.text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ol", html_items)

    def uo_list_to_html_node(self, block):
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            children = self.text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ul", html_items)

    def quote_to_html_node(self, block):
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            if not line.startswith(">"):
                raise ValueError("invalid quote block")
            new_lines.append(line.lstrip(">").strip())
        content = " ".join(new_lines)
        children = self.text_to_children(content)
        return ParentNode("blockquote", children)
