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

def isVaildEmail(string: str):
    if not string.find("@"): #检测是否含有@
        return False
    elif len(string.split("@")) != 2: #检测是否有多个@
        return False
    elif string[-1] == "@": #检测是否以@结尾
        return False
    elif not string.find("."): #检测是否含 .
        return False
    elif string[string.find("@") + 1] == ".": #检测@后面是否为 .
        return False
    return True