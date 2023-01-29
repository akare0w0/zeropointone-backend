from fastapi import APIRouter
# 导入加密库
# 切记一定要像这样引用 不然会出问题
from ..sha.sha import to_sha256
# 导入数据库
from ..db.db import get_client
# 导入验证器
from ..db.data_filter import is_vaild_str

router = APIRouter(prefix='/login')

@router.get('/')
async def login(account: str, password: str):
    result = {
        'valid':  True,
        'exists': True,
        'wrong':  False,
        'user':   None,
    }
    if not is_vaild_str(account) or not is_vaild_str(password):
        result['valid'] = False
    else:
        col = get_client().get_database('users').get_collection('users')
        data = col.find_one({ 'account': account }, { '_id': 0, 'account': 1, 'password': 1, 'nickname': 1 })
        print(to_sha256(password))
        if data == None:
            result['exists'] = False
        elif data['password'] != to_sha256(password):
            result['wrong'] = True
        else:
            result['user'] = data
    return result