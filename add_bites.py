# author: @Flash (https://github.com/etoFlash)
import glob
import re
import os
import requests
import zipfile
import traceback
LIST_PYBITES = "List of PyBites:"
files_to_unzip = []
files_unzipped = []
unzip_errors = []
readme = []
pat_filename = r".*?([0-9]{1,3})\.zip"
pat_title = r"<title>.*?(([0-9]{1,3}).*?)</title>"
pat_tags = r"<a class=\"tag\" href=\".*?\">(.*?)</a>"
pat_level = r"<img class=\"biteImg\" src=\".*?\" alt=\"(.*?) level\">"


for file in glob.glob("*.zip"):
    result = re.search(pat_filename, file)
    if result:
        files_to_unzip.append(file)
        num = result.group(1)
        if os.path.exists(num):
            unzip_errors.append("folder exists")
            continue
        try:
            bite_page = f"https://codechalleng.es/bites/{num}"
            r = requests.get(bite_page)
            re_title = re.search(pat_title, str(r.content))
            assert num == re_title.group(2), f"Title and file Bite's numbers should be match"
            title = re_title.group(1)
            list_tags = re.findall(pat_tags, str(r.content))
            tags = ", ".join(t for t in list_tags if t != "+")
            level = re.search(pat_level, str(r.content)).group(1)
            if not readme:
                with open("README.md", "r") as f:
                    readme = f.read().splitlines()
            new_line = f"| | [{title}](/{num}) | [(click)](https://codechalleng.es/bites/{num}) | {level} | {tags} |"
            for line in readme[readme.index(LIST_PYBITES) + 4:]:
                r = re.search(r"\(/([0-9]{1,3})\)", line)
                if r:
                    if int(num) < int(r.group(1)):
                        readme.insert(readme.index(line), new_line)
                        break
                if readme.index(line) == len(readme) - 1:
                    readme.append(new_line)
        except Exception as e:
            unzip_errors.append(f"fall of getting info from codechalleng.es:\n[{traceback.format_exc()[:-1]}]")
            continue
        with zipfile.ZipFile(file) as zip_file:
            try:
                zip_file.extractall(num)
            except Exception as e:
                unzip_errors.append(f"fall of unzipping:\n[{traceback.format_exc()[:-1]}]")
                continue
        files_unzipped.append(file)
        files_to_unzip.remove(file)
        try:
            os.remove(file)
            os.remove(os.path.join(num, "git.txt"))
            os.remove(os.path.join(num, "README.md"))
        except Exception as e:
            unzip_errors.append(f"fall of deleting *.zip or git.txt/README.md in new dir:"
                                "\n[{traceback.format_exc()[:-1]}]")
        try:
            for py_file in glob.glob(os.path.join(num, "*.py")):
                if f"{os.path.sep}test_" in py_file:
                    continue
                with open(py_file, "r") as f:
                    data = "# TODO: to beat\n" + f.read()
                with open(py_file, "w") as f:
                    f.write(data)
        except Exception as e:
            unzip_errors.append(f"fall of adding \"to beat\" to new py-file:\n[{traceback.format_exc()[:-1]}]")

if files_unzipped:
    print("Unzipped:")
    for i, file in enumerate(files_unzipped):
        print(f"{i + 1}) {file}")


if files_to_unzip:
    print("Not unzipped (file - reason):")
    for i, (file, reason) in enumerate(zip(files_to_unzip, unzip_errors)):
        print(f"{i + 1}) {file} - {reason}")


if not files_unzipped and not files_to_unzip:
    print("Nothing to process")
elif readme:
    with open("README.md", "w") as f:
        f.write("\n".join(readme))
