import os
import shutil
import argparse

def delete_bin_and_obj_dirs(path):
    """
    Recursively traverses all directories and deletes all folders named "bin" and "obj".

    Parameters:
        path (str): The path to start the traversal from.
    """
    for entry in os.scandir(path):
        if entry.is_dir():
            if entry.name == "bin" or entry.name == "obj":
                # Удаляем директорию если ее имя "bin" или obj""
                print(f"Deleting {entry.path}")
                shutil.rmtree(entry.path)
            else:
                # Рекурсивно проверяем подкаталоги если имя текщего каталога не "bin" или "obj"
                delete_bin_and_obj_dirs(entry.path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Delete subdirecories "bin" and "obj" in a specified directory.')
    parser.add_argument('-d', '--directory', nargs='?', default='.', help='Directory to clean bin/obj directories in (default: current directory)')
    
    args = parser.parse_args()
    delete_bin_and_obj_dirs(args.directory)