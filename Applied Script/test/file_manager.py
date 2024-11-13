"""
File manager:
1. Visa alla filer i en katalog
2. kopiera alla filer i en katalog
3. flytta filer
"""

import argparse
from pathlib import Path
import shutil
import os
from datetime import datetime

def list_files(directory, file_type=None):
    files = []
    for item in Path(directory).iterdir():
        if item.is_file() and (file_type is None or item.suffix == file_type):
            files.append(item.name)
    return files

def copy_files(directory, dest, file_type=None):
    Path(dest).mkdir(parents=True, exist_ok=True)
    files_copied = []
    for item in Path(directory).iterdir():
        if item.is_file() and (file_type is None or item.suffix == file_type):
            shutil.copy(item, Path(dest) / item.name)
            files_copied.append(item.name)
    return files_copied

def move_files(directory, dest, file_type=None):
    Path(dest).mkdir(parents=True, exist_ok=True)
    files_moved = []
    for item in Path(directory).iterdir():
        if item.is_file() and (file_type is None or item.suffix == file_type):
            shutil.move(item, Path(dest) / item.name)
            files_moved.append(item.name)
    return files_moved

def delete_files(directory, file_type=None):
    files_deleted = []
    for item in Path(directory).iterdir():
        if item.is_file() and (file_type is None or item.suffix == file_type):
            os.remove(item)
            files_deleted.append(item.name)
        return files_deleted

def write_log(operation, files, dest=None):
    with open("file_log.txt", "a") as file:
        file.write(f"{datetime.now()} - Operation: {operation}")
        if dest:
            file.write(f"Destination: {dest} \n")
        file.write("Files affected: \n")
        for f in files:
            file.write(f"{f} \n")
        file.write("\n")


def main():
    parser = argparse.ArgumentParser(description="File manager")
    parser.add_argument("directory", help="Target directory")

    parser.add_argument("-o", "--operation", choices=["list", "copy", "move", "delete"], required=True, help="Helps operation to perform")

    parser.add_argument("-d", "--destination", help="Destination directory")
    parser.add_argument("-f", "--filetype", help="Filter files by type")

    args = parser.parse_args()

    if args.operation == "list":
        files = list_files(args.directory, args.filetype)
        print(f"Files in directory {args.directory}: ")
        for file in files:
            print(file)

    elif args.operation == "copy":
        if not args.destination:
            print("-d required to copy files")
            return
        files_copied = copy_files(args.directory, args.destination, args.filetype)
        print(f"Files in directory {args.directory} copied to {args.destination} ")
        for file in files_copied:
            print(file)
        write_log("Copy", files_copied, args.destination)       

    elif args.operation == "move":
        if not args.destination:
            print("-d required to move files")
            return
        files_moved = move_files(args.directory, args.destination, args.filetype)
        print(f"Files in directory {args.directory} moved to {args.destination} ")
        for file in files_moved:
            print(file)       
        write_log("Move", files_moved, args.destination)       


    elif args.operation == "delete":
        files_deleted = delete_files(args.directory, args.filetype)
        print(f"Files deleted: ")
        for file in files_deleted:
            print(file)
        write_log("Delete", files_deleted)       






if __name__ == "__main__":
    main()