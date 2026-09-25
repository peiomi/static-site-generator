# run script with ./main.sh
from copy_static import copy_dir
import os
import shutil
from generate_page import generate_page

def main():
    public_dir = "public"
    static_dir = "static"
    # delete public
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # make new one
    os.mkdir(public_dir)

    # copy static -> public
    copy_dir(static_dir, public_dir)

    # generate html pages
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
