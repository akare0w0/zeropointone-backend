from typing import List

filters = (
    '<', '>', '#', '^', '&',
)

def is_vaild_str(string: str) -> bool:
    for i in string:
        if i in filters:
            return False
    return True

def is_vaild_strs(strings: List[str]) -> bool:
    for i in strings:
        if not is_vaild_str(i):
            return False
    return True
