from fastapi import APIRouter
from ..db.data_filter import is_vaild_str
from ..db.db import get_client
from ..sha.sha import to_sha256

router = APIRouter(prefix="/register")

@router.post('/')
async def register(account: str, password: str, confirm_password: str, nickname: str):
    result = {
        'vaild':     True,
        'confirmed': True,
        'exists':    False,
        'success':   True,
    }
    if (not is_vaild_str(account)) or (not is_vaild_str(password)):
        result['vaild'] = False
    elif password != confirm_password:
        result['confirmed'] = False
    else:
        col = get_client().get_database('users').get_collection('users')
        data = col.find_one({ 'account': account })
        if data == None:
            col.insert_one({
                'account':  account,
                'password': to_sha256(password),
                'nickname': nickname,
                'description': '这个人还没有简介欸O(∩_∩)O',
                'level': 1,
                'videos': [],
            })
        else:
            result['exists'] = True
    return result