import os
import glob

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    for file in glob.glob(f"{dirname}/*"):
        if os.path.getsize(file) / ONE_KB >= size_in_kb:
            yield file
