from textnode import TextType, TextNode

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


            
