# author: @Flash (https://github.com/etoFlash)
# TODO: 1) extract title, level and tags by requests by regex from codechalleng.es (example:
#  re.search(r"Bite ([0-9]{1,3}.*?)</title>", str(r.content))
# TODO: 2) add info about bite to solved_bites.md
# TODO: 3) add to top in py-file in new folder comment "# TODO: beat it" for made more easy search not solved bites
import glob
import re
import os
import requests
import zipfile
import traceback
files_to_unzip = []
files_unzipped = []
unzip_errors = []
num = 0
pat_filename = r".*?([0-9]{1,3})\.zip"
pat_title = r"<title>.*?(([0-9]{1,3}).*?)</title>"
pat_tags = r"<a class=\"tag\" href=\"(.*?)\">(.*?)</a>"
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
            print(bite_page)
            r = requests.get(bite_page)
            re_title = re.search(pat_title, str(r.content))
            assert num == re_title.group(2), f"Title and file Bite's numbers should be match"
            title = re_title.group(1)
            list_tags = re.findall(pat_tags, str(r.content))
            tags = ", ".join(t for _, t in list_tags if t != "+")
            level = re.search(pat_level, str(r.content)).group(1)
            print(f"title={title}; tags={tags}; level={level}")
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
        os.remove(file)

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
