from fastapi    import APIRouter
from ...db.db   import get_db
from ...sha.sha import to_sha256

router = APIRouter(prefix='/init_user')

@router.post('/')
def init_user(account: str, password: str, user_name: str, ) -> None:
    col = get_db().get_collection('users')
    col.insert_one({
        'account':     account,
        'password':    to_sha256(password),
        'user_name':   user_name,
        'level':       0,
    })