import os
from functools import reduce


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dirs, files = 0, 0

    for _, dirs_list, files_list in os.walk(directory):
        dirs += len(dirs_list)
        files += len(files_list)

    return dirs, files

    # functional variant:
    # return reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), (
    #     (len(dirs), len(files)) for _, dirs, files in os.walk(directory)
    # ))
