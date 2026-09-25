import os
import shutil

def copy_dir(static, public):
    items = os.listdir(static)

    for item in items:
        static_path = os.path.join(static, item)
        public_path = os.path.join(public, item)

        if os.path.isfile(static_path):
            print(f"copying {static_path} to {public_path}")
            shutil.copy(static_path, public_path)

        else:
            os.mkdir(public_path)
            copy_dir(static_path, public_path)