from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("node must have a tag")
        
        if not self.children:
            raise ValueError("node must have children")
        
        children_str = ""

        for child in self.children:
            children_str = children_str + f"{child.to_html()}"

        opening = f"<{self.tag}>"
        closing = f"</{self.tag}>"

        if self.props:
            props = ""
            for prop, val in self.props.items():
                props = props + f" {prop}='{val}'"
            opening = f"<{self.tag}{props}>"
            
        return f"{opening}{children_str}{closing}"

    def __repr__(self):
        return f"tags: {self.tags}, children: {self.children}, props: {self.props}"