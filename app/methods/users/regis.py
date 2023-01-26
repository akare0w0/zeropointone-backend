# 不要看这个
from fastapi           import APIRouter
from .init             import init_user
from ...db.data_filter import is_vaild_strs

router = APIRouter(prefix='/regis')

@router.get('/')
async def regis(account: str, password: str, password1: str, user_name: str):
    result = {
        'equals':  True,
        'vaild':   True,
        'success': True,
    }
    if password != password1:
        result['equals'] = False
    elif not is_vaild_strs([account, password, user_name]):
        result['vaild']  = False
    else:
        pass
    return result