import re

IN_CODE_COMMENT = '  #'
THREE_QUOTE = '"""'


def _remove_start_comment(code: str) -> str:
    if code.lstrip().startswith(THREE_QUOTE):
        return re.sub(rf'{THREE_QUOTE}.*?{THREE_QUOTE}\n', r'', code, count=1, flags=re.S)
    return code


def _remove_in_code_comment(code: str) -> str:
    return re.sub(rf'(.*){IN_CODE_COMMENT}.*', r'\1', code)


def strip_comments(code):
    # see Bite description
    result = _remove_start_comment(code)
    lines = []
    is_multiline_comment = False
    for line in result.splitlines():
        if is_multiline_comment:
            if line.endswith(THREE_QUOTE):
                is_multiline_comment = False
            continue
        if line.lstrip().startswith('#'):
            continue
        if line.startswith(' ') and line.lstrip().startswith(THREE_QUOTE):
            if not line.endswith(THREE_QUOTE) or len(line.lstrip()) == 3:
                is_multiline_comment = True
            continue
        lines.append(line)
    result = '\n'.join(lines)
    result = _remove_in_code_comment(result)

    return result
