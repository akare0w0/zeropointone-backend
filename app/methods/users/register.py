from fastapi import APIRouter
from ...db.data_filter import isVaildEmail, isVaildStr
from ...db.db import get_db
from ...sha.sha import toSha256

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
        'beforeRegister_exists': False,
    }
    if not isVaildEmail(email): #判断邮箱是否合法
        result['email_vaild'] = False
    elif (not isVaildStr(account)) or (not isVaildStr(password)): #判断用户名和密码是否合法
        result['vaild'] = False
    elif password != confirm_password:
        result['confirmed'] = False
    else:
        document = {
            'account': account
        }
        col = get_db().get_collection('users')
        data = col.find_one(document)
        if data == None: #判断用户是否已经存在
            col.insert_one({'account':account, 'password':toSha256(password)})
        else:
            result['beforeRegister_exists'] = True
    
    return result