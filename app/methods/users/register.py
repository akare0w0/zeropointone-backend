from fastapi import APIRouter
from ...db.data_filter import isVaildEmail, is_vaild_str
from ...db.db import get_client
from ...sha.sha import to_sha256

router = APIRouter(prefix="/register")

@router.post('/')
async def register(email: str, account: str, password: str, confirm_password: str):
    result = {
        #邮箱是否合法
        'email_vaild': True,
        # account,password是否合法
        'vaild': True,
        #判断密码和确认密码是否一致
        'confirmed': True,
        # 注册之前该用户是否存在
        'exists': False,
    }
    if not isVaildEmail(email): #判断邮箱是否合法
        result['email_vaild'] = False
    elif (not is_vaild_str(account)) or (not is_vaild_str(password)): #判断用户名和密码是否合法
        result['vaild'] = False
    elif password != confirm_password:
        result['confirmed'] = False
    else:
        document = {
            'account': account
        }
        users_db = get_client()["users"]
        col = users_db.get_collection("users")
        data = col.find_one(document)
        if data == None: #判断用户是否已经存在
            col.insert_one({'account':account, 'password':to_sha256(password)}) 
        else:
            result['exists'] = True
    
    return result