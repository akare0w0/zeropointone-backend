import hashlib

def to_sha256(string: str) -> str:
    sh = hashlib.sha256()
    sh.update(string.encode('utf-8'))
    return sh.hexdigest()