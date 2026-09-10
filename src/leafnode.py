from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return f"{self.value}"
        
        opening = f"<{self.tag}>"
        closing = f"</{self.tag}>"

        if self.props:
            props = ""
            for prop, val in self.props.items():
                props = props + f" {prop}='{val}'"
            opening = f"<{self.tag}{props}>"
            
        return f"{opening}{self.value}{closing}"

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"

    

