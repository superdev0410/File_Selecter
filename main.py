"""
main module
"""

import argparse
import os
import shutil


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

    # add arguments to addparser
    addparser.add_argument("files", nargs="+", help="list of filepaths to add")

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

    return parser.parse_args()


def add(filepaths: list):
    """add files to source folder

    Args:
        filepaths (list): list of files
    """

    # get source directory
    sourcedir = __file__[:-7] + "/Source"
    # check it is exist or not
    if not os.path.exists(sourcedir):
        os.mkdir(sourcedir)
    # get number of files in source folder
    size = len(os.listdir(sourcedir))

    # copy files to source folder and rename it
    for filepath in filepaths:
        size += 1
        shutil.copy(filepath, sourcedir + "/" + str(size) + ".png")


def choose(num: int, destination: str):
    """randomly choose files and copy to destination folder

    Args:
        num (int): number of files to choose
        destination (str): destination folder path
    """
    pass


def main():
    """
    main function
    """

    # parse command line arguments
    args = get_args()
    if args.command == "add":
        # start add command
        add(args.files)

    elif args.command == "choose":
        # start choose command
        choose(args.num, args.destination)


if __name__ == "__main__":
    main()
