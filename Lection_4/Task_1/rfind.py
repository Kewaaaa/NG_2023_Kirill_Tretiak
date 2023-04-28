import argparse
import os

def showFiles(path, empty=0):
    lst = path.split("/")
    for values in lst:
        print(' '*empty ,values+'/')
        empty += 1


def findFiles(folder, file_title):
    home_dir = os.path.expanduser("~")
    for root, dirs, files in os.walk(home_dir):
        if folder in root:
            folder1 = root
            break
    files = os.listdir(folder1)
    for root, dirs, files in os.walk(folder1):
        for file in files:
            name, ext = os.path.splitext(file)
            if file_title in file:
                path_file = os.sep.join([root, name + ext])
                showFiles(path_file)
                
                
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder")
    parser.add_argument("--file")
    args = parser.parse_args()
    findFiles(args.folder, args.file)


main()
