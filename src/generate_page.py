from block_type import BlockUtil
import os

util = BlockUtil()

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read files
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    html_node = util.markdown_to_html_node(markdown)
    content = html_node.to_html()

    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", content)

    html_page = html_page.replace("href='/", f"href='{basepath}")
    html_page = html_page.replace('href="/', f'href="{basepath}')

    html_page = html_page.replace("src='/", f"src='{basepath}")
    html_page = html_page.replace('src="/', f'src="{basepath}')


    print("BASEPATH:", basepath)
    print(html_page)

    directory = os.path.dirname(dest_path)

    if directory:
        os.makedirs(directory, exist_ok=True)


    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        source = os.path.join(dir_path_content, item)
        dest = os.path.join(dest_dir_path, item)
        print(f"source={source}")
        print(f"dest={dest}")

        if os.path.isfile(source):
            dest = dest.replace(".md", ".html")
            generate_page(source, template_path, dest, basepath)

        else:
            os.mkdir(dest)
            generate_pages_recursive(source, template_path, dest, basepath)
