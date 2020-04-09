def _extract_req_dict(reqs: str) -> dict:
   return dict(
      s.split("==") for s in reqs.strip().splitlines(keepends=False)
   )


def _extract_version_tuple(version: str) -> tuple:
   return tuple(map(int, version.split(".")))


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    result = []
    old_reqs_dict = _extract_req_dict(old_reqs)
    new_reqs_dict = _extract_req_dict(new_reqs)
    for k, v in old_reqs_dict.items():
       if _extract_version_tuple(new_reqs_dict[k]) > \
           _extract_version_tuple(v):
          result.append(k)

    return result
