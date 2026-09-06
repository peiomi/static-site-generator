# run script with ./main.sh
from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK.name, "https://www.boot.dev")
    print(text_node.__repr__())

if __name__ == "__main__":
    main()
