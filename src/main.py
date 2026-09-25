# run script with ./main.sh
from copy_static import copy_dir
import os
import shutil
from generate_page import generate_pages_recursive
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sysargv[1]

    public_dir = "docs"
    static_dir = "static"
    content_dir = "content"
    # delete public
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # make new one
    os.mkdir(public_dir)

    # copy static -> public
    copy_dir(static_dir, public_dir)

    # generate html pages
    generate_pages_recursive(content_dir, "template.html", public_dir, basepath)

if __name__ == "__main__":
    main()
