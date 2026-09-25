from block_type import BlockUtil
import os

util = BlockUtil()

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read files
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    html_node = util.markdown_to_html_node(markdown)
    print(repr(html_node))
    content = html_node.to_html()

    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", content)

    directory = os.path.dirname(dest_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_page)
