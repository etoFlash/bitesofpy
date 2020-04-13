from distutils.version import StrictVersion


def _extract_req_dict(reqs: str) -> dict:
   return dict(
      s.split("==") for s in reqs.strip().splitlines(keepends=False)
   )


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = _extract_req_dict(old_reqs)
    new = _extract_req_dict(new_reqs)
    for k, v in old.items():
       if StrictVersion(new[k]) > StrictVersion(v):
          yield k
