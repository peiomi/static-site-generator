import re
from textnode import TextType, TextNode
from regex import extract_markdown_images, extract_markdown_links

class NodeUtil():
    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        if delimiter not in text_type.value:
                raise Exception("wrong delimiter used")

        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN or delimiter not in node.text:
                new_nodes.append(node)
                continue

            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("no closing delimiter, invalid Markdown")
            for i, text in enumerate(split_text):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text=text, text_type=TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(text=text, text_type=text_type))
                    

        return new_nodes

    def split_nodes_image(self, old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN:
                new_nodes.append(node)
                continue

            matches = extract_markdown_images(node.text)
            remaining = node.text 
            for alt, url in matches:
                image_markdown = f"![{alt}]({url})"
                before, remaining = remaining.split(image_markdown, 1)

                if before:
                    new_nodes.append(TextNode(text=before, text_type=TextType.PLAIN))

                new_nodes.append(TextNode(text=alt, text_type=TextType.IMAGE, url=url))

            if remaining:
                new_nodes.append(TextNode(text=remaining, text_type=TextType.PLAIN))

        return new_nodes
            


    def split_nodes_link(self, old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.PLAIN:
                new_nodes.append(node)
                continue

            matches = extract_markdown_links(node.text)
            remaining = node.text
            for text, url in matches:
                link_markdown = f"[{text}]({url})"
                before, remaining = remaining.split(link_markdown, 1)

                if before:
                    new_nodes.append(TextNode(text=before, text_type=TextType.PLAIN))

                new_nodes.append(TextNode(text=text, text_type=TextType.LINK, url=url))

            if remaining:
                new_nodes.append(TextNode(text=remaining, text_type=TextType.PLAIN))

        return new_nodes
