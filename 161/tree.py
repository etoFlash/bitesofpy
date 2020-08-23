import os
import glob


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dirs_count = 0
    files_count = 0

    for dir_or_file in glob.glob(os.path.join(directory, "**"), recursive=True)[1:]:
        if os.path.isdir(dir_or_file):
            dirs_count += 1
        elif os.path.isfile(dir_or_file):
            files_count += 1

    return dirs_count, files_count
