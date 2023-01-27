from fastapi import APIRouter
# 导入加密库
# 切记一定要像这样引用 不然会出问题
from ...sha.sha import to_sha256
# 导入数据库
from ...db.db import get_db
# 导入验证器
from ...db.data_filter import is_vaild_str

router = APIRouter(prefix='/login')

# 当用get方法访问这个router的根（/）时
# 就会调用这个函数
@router.get('/')
async def login(account: str, password: str):
    # 返回值
    result = {
        # 字符串是否合法
        'vaild':  True,
        # 用户是否存在
        'exists': True,
        # 用户名所对应的密码是否错误
        'wrong':  False,
        # 用户的具体信息
        'user':   None,
    }
    if (not is_vaild_str(account)) or (not is_vaild_str(password)):
        result['vaild'] = False
    else:
        # MongoDB 的 document 差不多可以理解为python中的object和json
        document = {
            'account': account,
            'password': to_sha256(password), #加密重要信息
        }
        # 获取指定数据库（db@1_22)中的指定collection（集合）
        col = get_db().get_collection('users')
        # 查找跟上面的document信息一样的数据
        data = col.find_one(document)
        # 为空 -> 不存在
        if data == None:
            result['exists'] = False
        # 密码不一样
        elif col.find_one({ 'account': account }).password != password:
            result['wrong'] = True
        # 全部通过 返回用户具体信息
        else:
            result['user'] = data
    # 返回值
    return result