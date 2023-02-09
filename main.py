"""
main module
"""

import argparse
import os
import random
import shutil
import sys


def get_args() -> argparse.Namespace:
    """parse command line arguments

    Returns:
        argparse.Namespace: parsed arguments
    """

    # define parsers and subparsers
    parser = argparse.ArgumentParser(description="Choose and add files to source folder.")
    subparsers = parser.add_subparsers(dest="command")
    addparser = subparsers.add_parser("add", help="add files to source folder")
    chooseparser = subparsers.add_parser("choose", help="choose files and copy to anohter folder")
    renameparser = subparsers.add_parser("rename", help="rename files in source folder")

    # add arguments to addparser
    addparser.add_argument("files", nargs="+", help="list of filepaths to add")
    addparser.add_argument(
        "-s", "--source",
        default="E:\\MyProgram\\File Selecter\\Source",
        help="source image directory",
    )

    # add arguments to chooseparser
    chooseparser.add_argument(
        "-n", "--num",
        type=int,
        help="number of files to choose",
        default=50
    )
    chooseparser.add_argument(
        "-d", "--destination",
        help="destination folder path",
        default="E:\\MyProgram\\Screenshot\\Source"
    )
    chooseparser.add_argument(
        "-s", "--source",
        default="E:\\MyProgram\\File Selecter\\Source",
        help="source image directory",
    )

    # add argument to renameparser
    renameparser.add_argument(
        "-s", "--source",
        default="E:\\MyProgram\\File Selecter\\Source",
        help="source image directory",
    )

    return parser.parse_args()


def add(filepaths: list, sourcedir: str):
    """add files to source folder

    Args:
        filepaths (list): list of files
        sourcedir (str): path of source directory
    """

    # get number of files in source folder
    size = len(os.listdir(sourcedir))

    # copy files to source folder and rename it
    for filepath in filepaths:
        size += 1
        shutil.copy(filepath, sourcedir + "/" + str(size) + ".png")


def choose(num: int, destination: str, sourcedir: str):
    """randomly choose files and copy to destination folder

    Args:
        num (int): number of files to choose
        destination (str): destination folder path
        sourcedir (str): path of source directory
    """

    # get files in source folder
    sourcefiles = os.listdir(sourcedir)

    # choose files
    if len(sourcefiles) < num:
        print("Number of files are smaller than required files")
        sys.exit()
    files = random.choices(sourcefiles, k=num)


    # remove all files in destination folder
    dest_files = os.listdir(destination)
    for file in dest_files:
        os.remove(destination + "\\" + file)

    # copy files
    name = 1
    for file in files:
        shutil.copy(sourcedir + "\\" + file, destination + "\\" + str(name) + ".png")
        name += 1


def rename(sourcedir: str):
    """
    rename all files in source folder

    Args:
        sourcedir (str): path of source directory
    """

    # get source directory
    sourcedir = __file__[:-7] + "/Source"
    # check it is exist or not
    if not os.path.exists(sourcedir):
        os.mkdir(sourcedir)
    # get files in source folder
    sourcefiles = os.listdir(sourcedir)

    # rename all files
    for sourcefile in sourcefiles:
        os.rename(sourcedir + "\\" + sourcefile, sourcedir + "\\" + sourcefile + "_temp")
    name = 1
    for sourcefile in sourcefiles:
        os.rename(sourcedir + "\\" + sourcefile + "_temp", sourcedir + "\\" + str(name) + ".png")
        name += 1


def main():
    """
    main function
    """

    # parse command line arguments
    args = get_args()
    if args.command == "add":
        # start add command
        add(args.files, args.source)

    elif args.command == "choose":
        # start choose command
        if args.num <= 0:
            print("Number of files must be integer bigger than 0.")
            return
        choose(args.num, args.destination, args.source)

    elif args.command == "rename":
        # start rename command
        rename(args.source)


if __name__ == "__main__":
    main()
